import argparse
from urllib.parse import urlparse
from scanners.xss import detect_xss
from scanners.sqli import detect_sqli
from scanners.portscan import scan_ports
from scanners.csrf import detect_csrf_forms
from scanners.crawler import crawl  # Optional: if you're using a crawler

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

    print(f"[+] Scanning for CSRF...")
    csrf_vulns = detect_csrf_forms(args.url)

    hostname = urlparse(args.url).hostname
    print(f"[+] Scanning ports on {hostname}...")
    open_ports = scan_ports(hostname)

    # ===================== Results =====================
    print("\n========= SCAN RESULTS =========\n")

    print("[!] XSS Vulnerabilities:")
    print("\n".join(f"  [+] {v}" for v in xss_vulns) if xss_vulns else "  [-] None found")

    print("\n[!] SQL Injection Vulnerabilities:")
    print("\n".join(f"  [+] {v}" for v in sqli_vulns) if sqli_vulns else "  [-] None found")

    print("\n[!] CSRF Issues (POST forms missing token):")
    print("\n".join(f"  [+] {v}" for v in csrf_vulns) if csrf_vulns else "  [-] None found")

    print("\n[!] Open Ports:")
    print("\n".join(f"  [+] Port {p} is open" for p in open_ports) if open_ports else "  [-] None found")

if __name__ == '__main__':
    main()
