import requests
from bs4 import BeautifulSoup

def detect_csrf_forms(url):
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        forms = soup.find_all("form")

        potential_vulns = []

        for form in forms:
            if form.get("method", "").lower() == "post":
                inputs = form.find_all("input")
                has_token = any("csrf" in (i.get("name") or "").lower() for i in inputs)

                if not has_token:
                    action = form.get("action") or url
                    full_action = requests.compat.urljoin(url, action)
                    potential_vulns.append(full_action)

        return potential_vulns

    except Exception as e:
        return []
