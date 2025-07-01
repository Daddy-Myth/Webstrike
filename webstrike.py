import argparse
from urllib.parse import urlparse
from scanners.xss import detect_xss
from scanners.sqli import detect_sqli
from scanners.portscan import scan_ports
from scanners.csrf import detect_csrf_forms
from scanners.misconfig import run_nmap, run_nikto
from scanners.crawler import crawl

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

    print(f"[+] Running Nmap scan...")
    nmap_result = run_nmap(hostname)

    print(f"[+] Running Nikto scan...")
    nikto_result = run_nikto(hostname)


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

    print("\n[!] Nmap Service & Version Detection:")
    print(nmap_result or "  [-] Nmap returned no output")

    print("\n[!] Nikto Web Server Misconfiguration Scan:")
    print(nikto_result or "  [-] Nikto returned no output")


if __name__ == '__main__':
    main()
