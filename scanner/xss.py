import requests

def detect_xss(urls):
    payload = "<script>alert(1)</script>"
    vulnerable = []

    for url in urls:
        if "?" in url:
            test_url = url + "&xss=" + payload
            try:
                r = requests.get(test_url, timeout=5)
                if payload in r.text:
                    vulnerable.append(test_url)
            except:
                continue
    return vulnerable
