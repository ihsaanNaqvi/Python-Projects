import requests
from bs4 import BeautifulSoup
import time
from urllib.parse import urljoin, urlparse
import random

class WikipediaSixDegrees:
    def __init__(self, rate_limit=5):
        self.rate_limit = rate_limit  # requests per second
        self.last_request_time = 0
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'WikipediaSixDegrees/1.0 (https://github.com/example)'
        })
        
    def _rate_limit(self):
        """Enforce rate limiting"""
        elapsed = time.time() - self.last_request_time
        if elapsed < 1.0 / self.rate_limit:
            time.sleep((1.0 / self.rate_limit) - elapsed)
        self.last_request_time = time.time()
        
    def get_random_article(self):
        """Get a random Wikipedia article URL"""
        self._rate_limit()
        response = self.session.get("https://en.wikipedia.org/wiki/Special:Random", allow_redirects=True)
        return response.url
        
    def get_article_links(self, url):
        """Extract all Wikipedia article links from the main content of a page"""
        self._rate_limit()
        try:
            response = self.session.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Get the main content div
            content = soup.find(id="mw-content-text")
            if not content:
                return []
                
            # Find all links that are:
            # 1. In the main content (not navboxes, etc.)
            # 2. Point to other Wikipedia articles (not external links)
            # 3. Don't have "class=new" (red links to non-existent articles)
            links = []
            for a in content.select('div.mw-parser-output a[href^="/wiki/"]:not([href*=":"]):not(.new)'):
                href = a.get('href')
                if href and not href.startswith('/wiki/Special:'):
                    full_url = urljoin("https://en.wikipedia.org", href)
                    # Remove fragment identifiers
                    full_url = full_url.split('#')[0]
                    links.append(full_url)
                    
            return list(set(links))  # Remove duplicates
            
        except Exception as e:
            print(f"Error processing {url}: {e}")
            return []
            
    def find_path(self, start_url, end_url, max_depth=5):
        """Find a path between two Wikipedia articles using BFS"""
        if start_url == end_url:
            return [start_url]
            
        # Bidirectional BFS
        forward_queue = [(start_url, [start_url])]
        backward_queue = [(end_url, [end_url])]
        forward_visited = {start_url: [start_url]}
        backward_visited = {end_url: [end_url]}
        
        while forward_queue or backward_queue:
            # Forward BFS step
            if forward_queue:
                current_url, path = forward_queue.pop(0)
                if len(path) >= max_depth:
                    continue
                    
                links = self.get_article_links(current_url)
                for link in links:
                    if link in backward_visited:
                        # Found intersection
                        backward_path = backward_visited[link]
                        return path + backward_path[::-1]
                    if link not in forward_visited:
                        forward_visited[link] = path + [link]
                        forward_queue.append((link, path + [link]))
                        
            # Backward BFS step
            if backward_queue:
                current_url, path = backward_queue.pop(0)
                if len(path) >= max_depth:
                    continue
                    
                links = self.get_article_links(current_url)
                for link in links:
                    if link in forward_visited:
                        # Found intersection
                        forward_path = forward_visited[link]
                        return forward_path + path[::-1]
                    if link not in backward_visited:
                        backward_visited[link] = path + [link]
                        backward_queue.append((link, path + [link]))
                        
        return None
        
    def run_test(self):
        """Run the test with two random articles"""
        print("Getting two random Wikipedia articles...")
        url1 = self.get_random_article()
        time.sleep(1)  # Ensure we get a different random article
        url2 = self.get_random_article()
        
        print(f"Finding path between:\n{url1}\nand\n{url2}")
        
        path = self.find_path(url1, url2)
        
        if path:
            print("\nPath found:")
            for i, url in enumerate(path):
                if i == 0:
                    print(f"url1 => {url}")
                elif i == len(path) - 1:
                    print(f"=> {url} <= url2")
                else:
                    print(f"=> {url}")
            print(f"\nDegrees of separation: {len(path)-1}")
        else:
            print("\nNo path found within 5 degrees of separation")

if __name__ == "__main__":
    # Initialize with rate limit (default 5 requests per second)
    finder = WikipediaSixDegrees(rate_limit=5)
    finder.run_test()