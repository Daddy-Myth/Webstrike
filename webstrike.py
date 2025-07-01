import argparse
import requests
import socket
import html
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
from bs4 import BeautifulSoup

# ===================== CRAWLER =====================

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

# ===================== XSS DETECTION =====================

def inject_xss_payload(url, param, payload):
    parsed = urlparse(url)
    query_params = parse_qs(parsed.query)

    if param not in query_params:
        return None

    query_params[param] = payload
    new_query = urlencode(query_params, doseq=True)
    modified_url = urlunparse((parsed.scheme, parsed.netloc, parsed.path, parsed.params, new_query, parsed.fragment))
    return modified_url

def detect_xss(urls):
    payload = "<script>alert(1)</script>"
    encoded_payload = html.escape(payload)
    vulnerable = []

    for url in urls:
        parsed = urlparse(url)
        params = parse_qs(parsed.query)

        if not params:
            continue

        for param in params:
            test_url = inject_xss_payload(url, param, payload)
            if not test_url:
                continue
            try:
                r = requests.get(test_url, timeout=5)
                if payload in r.text or encoded_payload in r.text:
                    vulnerable.append(test_url)
                    break
            except:
                continue
    return vulnerable

# ===================== SQL INJECTION =====================

def detect_sqli(urls):
    payload = "' OR '1'='1"
    vulnerable = []

    for url in urls:
        if "?" not in url:
            continue
        test_url = url + payload
        try:
            r = requests.get(test_url, timeout=5)
            if any(error in r.text.lower() for error in ["sql", "syntax", "mysql", "error in your sql"]):
                vulnerable.append(test_url)
        except:
            continue
    return vulnerable

# ===================== PORT SCANNER =====================

def scan_ports(host, ports=[21, 22, 80, 443, 3306, 8080]):
    open_ports = []
    for port in ports:
        try:
            sock = socket.socket()
            sock.settimeout(1)
            sock.connect((host, port))
            open_ports.append(port)
            sock.close()
        except:
            pass
    return open_ports

# ===================== MAIN =====================

def main():
    parser = argparse.ArgumentParser(description="Webstrike - Web Vulnerability Scanner")
    parser.add_argument('--url', required=True, help='Target URL (e.g., https://example.com)')
    args = parser.parse_args()

    print(f"[+] Crawling {args.url}")
    urls = crawl(args.url)

    print(f"[+] Scanning for XSS...")
    xss_vulns = detect_xss(urls)

    print(f"[+] Scanning for SQL Injection...")
    sqli_vulns = detect_sqli(urls)

    hostname = urlparse(args.url).hostname
    print(f"[+] Scanning open ports on {hostname}...")
    open_ports = scan_ports(hostname)

    # ===================== REPORT =====================
    print("\n========= SCAN RESULTS =========\n")

    print("[!] XSS Vulnerabilities:")
    if xss_vulns:
        for v in xss_vulns:
            print(f"  [+] {v}")
    else:
        print("  [-] None found")

    print("\n[!] SQL Injection Vulnerabilities:")
    if sqli_vulns:
        for v in sqli_vulns:
            print(f"  [+] {v}")
    else:
        print("  [-] None found")

    print("\n[!] Open Ports:")
    if open_ports:
        for port in open_ports:
            print(f"  [+] Port {port} is open")
    else:
        print("  [-] No common ports open")

if __name__ == '__main__':
    main()
