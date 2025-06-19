import requests

def detect_sqli(urls):
    payload = "' OR '1'='1"
    vulnerable = []

    for url in urls:
        if "?" in url:
            test_url = url + payload
            try:
                r = requests.get(test_url, timeout=5)
                if "SQL" in r.text or "syntax" in r.text or "mysql" in r.text.lower():
                    vulnerable.append(test_url)
            except:
                continue
    return vulnerable
