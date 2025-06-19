import requests
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
import html

def inject_payload(url, param, payload):
    parsed = urlparse(url)
    query_params = parse_qs(parsed.query)

    if param not in query_params:
        return None

    # Replace the target parameter with the payload
    query_params[param] = payload

    # Rebuild query string
    new_query = urlencode(query_params, doseq=True)

    # Construct new URL with modified query
    modified_url = urlunparse(
        (parsed.scheme, parsed.netloc, parsed.path, parsed.params, new_query, parsed.fragment)
    )

    return modified_url

def detect_xss(urls):
    payload = "<script>alert(1)</script>"
    encoded_payload = html.escape(payload)  # &lt;script&gt;alert(1)&lt;/script&gt;

    vulnerable = []

    for url in urls:
        parsed = urlparse(url)
        params = parse_qs(parsed.query)

        if not params:
            continue  # Skip if no parameters

        for param in params:
            test_url = inject_payload(url, param, payload)
            if not test_url:
                continue

            try:
                r = requests.get(test_url, timeout=5)
                # Check if payload (raw or escaped) is reflected
                if payload in r.text or encoded_payload in r.text:
                    vulnerable.append(test_url)
                    break
            except:
                continue

    return vulnerable
