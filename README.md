# 🛡️ Webstrike - Advanced Web Vulnerability Scanner

![Webstrike Banner](https://img.shields.io/badge/Webstrike-Kali%20Ready-red?style=flat-square&logo=linux)

**Webstrike** is a modular, open-source web vulnerability scanner built with Python for penetration testers and cybersecurity researchers. It detects common web security flaws like XSS, SQLi, CSRF, server misconfigurations, and more — all from the command line.

---

## 🚀 What It Does

Webstrike crawls target websites, discovers internal links, and runs a suite of automated vulnerability checks against common web attack surfaces using both custom logic and powerful tools like `nmap` and `nikto`.

---

## ⚙️ Features

- ✅ **Crawling**: Automatically discovers internal links on the target site  
- 🔎 **XSS Detection**: Injects payloads into parameters and detects reflected/scripted outputs  
- 🔓 **SQL Injection Detection**: Fuzzes parameters and looks for SQL error patterns  
- 🔐 **CSRF Detection**: Scans for POST forms that lack CSRF tokens  
- 🧱 **Server Misconfiguration Detection**: Runs `nmap` and `nikto` to find outdated software, missing headers, open services  
- 🌐 **Port Scanner**: Scans common ports using sockets  
- 📦 **Modular Codebase**: Each scanner is its own file, easily extensible  
- 🧪 Designed for use on Kali Linux
---


## 📦 Tools Used in Webstrike

| Tool         | Description                                                      |
|--------------|------------------------------------------------------------------|
| **Python Requests** | Handles all HTTP requests and responses                   |
| **BeautifulSoup**   | Parses HTML to extract links and form fields              |
| **Nmap**            | Scans open ports, service versions, OS info               |
| **Nikto**           | Scans web server for misconfigurations and known issues   |
| **Socket**          | Custom TCP port scanner to detect open services           |
| **argparse**        | Command-line argument handling for ease of use            |

---

## 🧪 How to Use

### ✅ Prerequisites

- Python 3.x  
- Kali Linux or any Linux distro  
- Tools: `nmap`, `nikto`

### 🔧 Installation

```bash
git clone https://github.com/Daddy-Myth/Webstrike.git
cd Webstrike
python3 -m venv scanenv
source scanenv/bin/activate
pip install -r requirements.txt
```

Install tools if not already present
```bash
sudo apt install nmap nikto -y
```

---

### ▶️ Running a Scan

```bash
python webstrike.py --url http://testphp.vulnweb.com
```
Change the URL to your target (only test legal and safe targets).

### 📄 Output
```bash
──(scanenv)─(root㉿kali)-[/home/shogun/Webstrike]
└─# python webstrike.py --url http://testphp.vulnweb.com
[+] Crawling http://testphp.vulnweb.com
[+] Scanning for XSS...
[+] Scanning for SQL Injection...
[+] Scanning for CSRF...
[+] Scanning ports on testphp.vulnweb.com...
[+] Running Nmap scan...
[+] Running Nikto scan...

========= SCAN RESULTS =========

[!] XSS Vulnerabilities:
  [+] http://target.com/page.php?query=<script>alert(1)</script>

[!] SQL Injection Vulnerabilities:
  [+] http://testphp.vulnweb.com/listproducts.php?cat=3' OR '1'='1
  [+] http://testphp.vulnweb.com/product.php?pic=3' OR '1'='1
  [+] http://testphp.vulnweb.com/artists.php?artist=2' OR '1'='1
  [+] http://testphp.vulnweb.com/artists.php?artist=3' OR '1'='1
  [+] http://testphp.vulnweb.com/listproducts.php?artist=1' OR '1'='1
  [+] http://testphp.vulnweb.com/product.php?pic=2' OR '1'='1
  [+] http://testphp.vulnweb.com/listproducts.php?artist=3' OR '1'='1
  [+] http://testphp.vulnweb.com/artists.php?artist=1' OR '1'='1
  [+] http://testphp.vulnweb.com/product.php?pic=1' OR '1'='1
  [+] http://testphp.vulnweb.com/listproducts.php?cat=2' OR '1'='1
  [+] http://testphp.vulnweb.com/listproducts.php?cat=4' OR '1'='1
  [+] http://testphp.vulnweb.com/product.php?pic=7' OR '1'='1
  [+] http://testphp.vulnweb.com/product.php?pic=6' OR '1'='1
  [+] http://testphp.vulnweb.com/listproducts.php?artist=2' OR '1'='1
  [+] http://testphp.vulnweb.com/product.php?pic=4' OR '1'='1
  [+] http://testphp.vulnweb.com/product.php?pic=5' OR '1'='1
  [+] http://testphp.vulnweb.com/listproducts.php?cat=1' OR '1'='1

[!] CSRF Issues (POST forms missing token):
  [+] http://testphp.vulnweb.com/search.php?test=query

[!] Open Ports:
  [+] Port 21 is open
  [+] Port 80 is open

[!] Nmap Service & Version Detection:
Starting Nmap 7.95 ( https://nmap.org ) at 2025-07-13 16:02 IST
Nmap scan report for testphp.vulnweb.com (44.228.249.3)
Host is up (0.033s latency).
rDNS record for 44.228.249.3: ec2-44-228-249-3.us-west-2.compute.amazonaws.com
Not shown: 996 filtered tcp ports (no-response)
PORT     STATE SERVICE    VERSION
21/tcp   open  tcpwrapped
80/tcp   open  tcpwrapped
554/tcp  open  tcpwrapped
1723/tcp open  tcpwrapped

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 31.57 seconds


[!] Nikto Web Server Misconfiguration Scan:
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          44.228.249.3
+ Target Hostname:    testphp.vulnweb.com
+ Target Port:        80
+ Start Time:         2025-07-01 17:47:29 (GMT)

+ Server: Apache/2.2.8 (Ubuntu)
+ Retrieved x-powered-by header: PHP/5.2.4-2ubuntu5.10
+ The X-Frame-Options header is not set. This could allow clickjacking attacks.
+ The X-Content-Type-Options header is not set. This could allow MIME-type sniffing.
+ OSVDB-3268: /admin/: Directory indexing found.
+ OSVDB-3092: /phpinfo.php: PHP configuration file is accessible.
+ OSVDB-3092: /test/: Default test directory found.
+ OSVDB-112004: /icons/: Directory indexing enabled.
+ Cookie PHPSESSID created without the HttpOnly flag.
+ Uncommon header 'x-powered-by' found, which can reveal tech stack info.
+ Allowed HTTP Methods: GET, HEAD, POST, OPTIONS, TRACE 
+ WebDAV is enabled on the server.
+ Scan completed at 2025-07-01 17:47:59 (30 seconds)
---------------------------------------------------------------------------

+ 1 host(s) tested

```


---

## 🧩 Module Descriptions

Each scanner module is located in the `scanners/` folder. Below is a description of what each module scans for and what the associated vulnerability means.

| Module File     | What It Scans For                                       | Explanation |
|------------------|----------------------------------------------------------|-------------|
| `crawler.py`     | Crawls the target site and collects all internal links  | Identifies reachable pages on the same domain so other modules can scan them. It enables working of xxs, sqli and csrf modules|
| `xss.py`         | Cross-Site Scripting (XSS)                               | XSS occurs when an attacker injects malicious JavaScript into a page, which then runs in the victim’s browser. The module injects test payloads and looks for reflected scripts in the response. |
| `sqli.py`        | SQL Injection (SQLi)                                     | SQLi allows attackers to manipulate SQL queries by injecting special characters (`' OR '1'='1`). This module checks for database errors or suspicious responses after injecting such payloads. |
| `csrf.py`        | Missing CSRF Token Protection                            | CSRF tricks logged-in users into submitting unwanted actions (e.g. changing a password). This module finds POST forms and flags ones that don’t include a CSRF token field. |
| `portscan.py`    | Open TCP ports                                           | Open ports may expose unnecessary or vulnerable services. This module checks ports like 21, 22, 80, 443, 3306 using raw TCP socket connections. |
| `misconfig.py`   | Web server misconfigurations via Nikto & Nmap           | Uses external tools to identify missing security headers, outdated software, open services, and misconfigured directories like `/admin/` or `/phpinfo.php`. |

> Each module feeds its results back to `webstrike.py`, which prints a structured summary.

---

## 📁 Project Structure
```
Webstrike/
├── scanners/
│ ├── xss.py
│ ├── sqli.py
│ ├── csrf.py
│ ├── portscan.py
│ ├── misconfig.py
│ └── crawler.py
├── webstrike.py
├── requirements.txt
├── README.md
```
Each module in the `scanners/` folder handles a specific type of vulnerability. `webstrike.py` is the main entry point that coordinates the entire scan.

---

## 👨‍💻 Author

**Archit Yadav**  
🛠️ Cybersecurity Intern at [@HackTech](https://hacktech.co.in)
🔗 GitHub: [@Daddy-Myth](https://github.com/Daddy-Myth)

---

## 📄 License

This project is licensed under the **MIT License**.  
You are free to use, modify, and distribute this software under open-source terms.

---

## 🚧 Roadmap / Upcoming Features

- 📈 Improve the efficiency of these automated tools to match those of maual tools like burpsuit, owasp zap, nessus, acunetics
- 📄 Export scan results to **HTML reports**
- 🌐 Develop a **Web-based GUI** for launching scans and viewing results

---
