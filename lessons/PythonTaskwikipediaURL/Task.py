# import requests
# from bs4 import BeautifulSoup
# from urllib.parse import urljoin, urlparse
# from collections import deque

# WIKI_BASE = "https://en.wikipedia.org"
# RANDOM_PAGE = "https://en.wikipedia.org/wiki/Special:Random"

# def get_random_article():
#     try:
#         response = requests.get(RANDOM_PAGE, allow_redirects=True)
#         final_url = response.url
#         if final_url.startswith(WIKI_BASE + "/wiki/") and ":" not in final_url:
#             return final_url
#         else:
#             return get_random_article()  # Try again if it's not a valid article
#     except Exception as e:
#         print(f"Error getting random article: {e}")
#         return None

# def get_links(url, limit=20):
#     try:
#         response = requests.get(url)
#         soup = BeautifulSoup(response.content, "html.parser")
#         content_div = soup.find("div", {"id": "bodyContent"})
#         links = content_div.find_all("a", href=True)

#         urls = []
#         for link in links:
#             href = link.get("href")
#             if href.startswith("/wiki/") and ":" not in href:
#                 full_url = urljoin(WIKI_BASE, href)
#                 if full_url.startswith(WIKI_BASE + "/wiki/") and full_url not in urls:
#                     urls.append(full_url)
#             if len(urls) >= limit:
#                 break
#         return urls
#     except Exception as e:
#         print(f"Error fetching {url}: {e}")
#         return []

# def find_chain(start_url, target_url, max_depth=5):
#     visited = set()
#     queue = deque()
#     queue.append((start_url, [start_url]))
#     visited.add(start_url)

#     while queue:
#         current_url, path = queue.popleft()
#         print(f"Visiting ({len(path) - 1}): {current_url}")

#         if current_url == target_url:
#             return path

#         if len(path) >= max_depth:
#             continue

#         for link in get_links(current_url, limit=20):
#             if link not in visited:
#                 visited.add(link)
#                 queue.append((link, path + [link]))

#     return None

# def print_path(title, path):
#     print(f"\n✅ {title}")
#     for i, url in enumerate(path):
#         print(f"Step {i}: {url}")

# def main():
#     start_url = get_random_article()
#     target_url = get_random_article()

#     print("🔹 Start URL:", start_url)
#     print("🔹 Target URL:", target_url)
#     # Forward path
#     print("\n➡️ Searching path from START to TARGET")
#     path = find_chain(start_url, target_url, max_depth=5)
#     if path:
#         print_path("Path from Start to Target:", path)
#     else:
#         print("\n❌ Could not find path from Start to Target within 5 steps.")
#      # Reverse path
#     print("\n⬅️ Searching path from TARGET back to START")
#     reverse_path = find_chain(target_url, start_url, max_depth=5)
#     if reverse_path:
#         print_path("Reverse Path from Target to Start:", reverse_path)
#     else:
#         print("\n❌ Could not find reverse path within 5 steps.")

# if __name__ == "__main__":
#     main()

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from collections import deque
import random
import time

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
            # Filter valid English Wikipedia article links
            if href.startswith("/wiki/") and ":" not in href:
                full_url = urljoin(WIKI_BASE, href)
                if full_url.startswith(WIKI_BASE + "/wiki/") and full_url not in urls:
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
            if link not in visited and link.startswith(WIKI_BASE + "/wiki/"):
                queue.append((link, path + [link]))

    return None

def main():
    # Select two different random Wikipedia articles
    start_url = "https://en.wikipedia.org/wiki/Special:Random"
    target_url = "https://en.wikipedia.org/wiki/Special:Random"

    # Ensure different start and target URLs
    while start_url == target_url:
        target_url = "https://en.wikipedia.org/wiki/Special:Random"

    print(f"Randomly Selected Start URL: {start_url}")
    print(f"Randomly Selected Target URL: {target_url}")

    # Check if URLs are valid and reachable
    print("\nChecking if start and target URLs are reachable...")
    start_reachable = requests.get(start_url).status_code == 200
    target_reachable = requests.get(target_url).status_code == 200

    if not start_reachable or not target_reachable:
        print("❌ One or both of the URLs are not reachable!")
        return

    # Perform the BFS search from start to target
    path = find_chain(start_url, target_url, max_depth=5)

    if path:
        print("\n✅ Path found from Start to Target:")
        for i, url in enumerate(path):
            print(f"Step {i}: {url}")
    else:
        print("\n❌ Target URL is unreachable within 5 transitions.")

    # Perform the BFS search from target to start (reverse path)
    reverse_path = find_chain(target_url, start_url, max_depth=5)

    if reverse_path:
        print("\n🔁 Path found from Target to Start:")
        for i, url in enumerate(reverse_path):
            print(f"Step {i}: {url}")
    else:
        print("\n❌ Start URL is unreachable from Target within 5 transitions.")

if __name__ == "__main__":
    main()
