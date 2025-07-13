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
  [-] None found

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
+ 0 host(s) tested
```


---

## 🧩 Module Descriptions

Each scanner module is stored in the `scanners/` folder. Every file is independent, focused, and reusable across other Python-based security tools.

| Module File         | Description                                                   | Tools Used                  |
|---------------------|---------------------------------------------------------------|-----------------------------|
| `crawler.py`        | Crawls the target website and collects internal URLs          | `requests`, `BeautifulSoup` |
| `xss.py`            | Detects reflected Cross-Site Scripting vulnerabilities        | `requests`, `html`          |
| `sqli.py`           | Tests for SQL Injection using basic fuzzing and error matching| `requests`                  |
| `csrf.py`           | Identifies POST forms missing CSRF tokens                     | `requests`, `BeautifulSoup` |
| `portscan.py`       | Scans for open TCP ports on the target host                   | `socket`                    |
| `misconfig.py`      | Runs Nmap and Nikto to detect server misconfigurations        | `subprocess`, `nmap`, `nikto` |

> These modules return structured results to `webstrike.py` for clean output and future reporting.

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
