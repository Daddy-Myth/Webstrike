import requests
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
import html

def inject_payload(url, param, payload):
    parsed = urlparse(url)
    query_params = parse_qs(parsed.query)
    query_params[param] = payload
    new_query = urlencode(query_params, doseq=True)
    return urlunparse((parsed.scheme, parsed.netloc, parsed.path, parsed.params, new_query, parsed.fragment))

def detect_xss(urls):
    payload = "<script>alert(1)</script>"
    encoded = html.escape(payload)
    vulnerable = []

    for url in urls:
        parsed = urlparse(url)
        params = parse_qs(parsed.query)
        if not params:
            continue

        for param in params:
            test_url = inject_payload(url, param, payload)
            try:
                r = requests.get(test_url, timeout=5)
                if payload in r.text or encoded in r.text:
                    vulnerable.append(test_url)
                    break
            except:
                continue
    return vulnerable
