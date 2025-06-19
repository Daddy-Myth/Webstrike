import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def crawl(url):
    visited = set()
    to_visit = [url]

    while to_visit:
        current = to_visit.pop()
        if current not in visited:
            visited.add(current)
            try:
                resp = requests.get(current, timeout=5)
                soup = BeautifulSoup(resp.text, 'html.parser')
                for link in soup.find_all('a', href=True):
                    full_url = urljoin(current, link['href'])
                    if url in full_url:
                        to_visit.append(full_url)
            except:
                continue
    return visited
