import requests

def detect_sqli(urls):
    payload = "' OR '1'='1"
    vulnerable = []

    for url in urls:
        if "?" not in url:
            continue
        test_url = url + payload
        try:
            r = requests.get(test_url, timeout=5)
            if any(err in r.text.lower() for err in ["sql", "syntax", "mysql", "error in your sql"]):
                vulnerable.append(test_url)
        except:
            continue
    return vulnerable
