import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from collections import deque

WIKI_BASE = "https://en.wikipedia.org"

def get_links(url, limit=20):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        content_div = soup.find("div", {"id": "bodyContent"})
        links = content_div.find_all("a", href=True)

        urls = []
        for link in links:
            href = link.get("href")
            if href.startswith("/wiki/") and ":" not in href:
                full_url = urljoin(WIKI_BASE, href)
                if full_url not in urls:
                    urls.append(full_url)
            if len(urls) >= limit:
                break
        return urls
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return []

def find_chain(start_url, target_url, max_depth=5):
    visited = set()
    queue = deque()
    queue.append((start_url, [start_url]))

    while queue:
        current_url, path = queue.popleft()
        print(f"Visiting ({len(path) - 1}): {current_url}")
        if current_url == target_url:
            return path
        if current_url in visited:
            continue
        visited.add(current_url)

        if len(path) > max_depth:
            continue

        for link in get_links(current_url, limit=20):
            if link not in visited:
                queue.append((link, path + [link]))

    return None

def main():
    start_url = "https://en.wikipedia.org/wiki/Arab_U23_Athletics_Championships"
    target_url = "https://en.wikipedia.org/wiki/Irish_Boundary_Commission"

    print("Starting URL:", start_url)
    print("Target URL:", target_url)
    path = find_chain(start_url, target_url, max_depth=5)

    if path:
        print("\n✅ Path found:")
        for i, url in enumerate(path):
            print(f"Step {i}: {url}")
    else:
        print("\n❌ Target URL is unreachable within 5 transitions.")

if __name__ == "__main__":
    main()
