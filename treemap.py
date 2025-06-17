import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from anytree import Node, RenderTree

visited = set()

def is_same_domain(base_url, target_url):
    return urlparse(base_url).netloc == urlparse(target_url).netloc

def add_to_tree(root, url_path_parts):
    current_node = root
    for part in url_path_parts:
        existing = next((child for child in current_node.children if child.name == part), None)
        if existing:
            current_node = existing
        else:
            new_node = Node(part, parent=current_node)
            current_node = new_node

def crawl(url, base_url, tree_root):
    if url in visited:
        return
    visited.add(url)

    try:
        response = requests.get(url, timeout=5)
        if "text/html" not in response.headers.get("Content-Type", ""):
            return

        soup = BeautifulSoup(response.text, "html.parser")
        path_parts = urlparse(url).path.strip("/").split("/")
        if path_parts != ['']:
            add_to_tree(tree_root, path_parts)

        for link in soup.find_all("a", href=True):
            href = link['href']
            next_url = urljoin(url, href)
            if is_same_domain(base_url, next_url):
                crawl(next_url, base_url, tree_root)

    except requests.RequestException as e:
        print(f"[!] Error fetching {url}: {e}")

if __name__ == "__main__":
    print("########################################")
    print("# Site tree map is running...")
    print("########################################")
    start_url = input("Enter start URL (e.g. https://example.com): ").strip()
    base_domain = urlparse(start_url).netloc
    tree_root = Node(base_domain)

    print("[*] Crawling started...")
    crawl(start_url, start_url, tree_root)

    print("\n📂 Site Tree Map:\n")
    for pre, fill, node in RenderTree(tree_root):
        print("%s%s" % (pre, node.name))
