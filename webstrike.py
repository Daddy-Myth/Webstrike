import argparse
from urllib.parse import urlparse
from scanner import crawler, xss, sqli, portscan

def main():
    parser = argparse.ArgumentParser(description="WebStrike - Website Vulnerability Scanner")
    parser.add_argument('--url', required=True, help='Target website URL (e.g., https://example.com)')
    args = parser.parse_args()

    print(f"[+] Crawling {args.url}")
    urls = crawler.crawl(args.url)

    print(f"[+] Scanning for XSS...")
    xss_vulns = xss.detect_xss(urls)

    print(f"[+] Scanning for SQL Injection...")
    sqli_vulns = sqli.detect_sqli(urls)

    hostname = urlparse(args.url).hostname
    print(f"[+] Scanning open ports on {hostname}...")
    open_ports = portscan.scan_ports(hostname)

    print("\n========= SCAN RESULTS =========")
    print("\n[!] XSS Vulnerabilities:")
    for v in xss_vulns:
        print(f"  [+] {v}")

    print("\n[!] SQL Injection Vulnerabilities:")
    for v in sqli_vulns:
        print(f"  [+] {v}")

    print("\n[!] Open Ports:")
    for p in open_ports:
        print(f"  [+] Port {p} is open")

if __name__ == '__main__':
    main()
