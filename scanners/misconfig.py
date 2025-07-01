import subprocess

def run_nmap(host):
    try:
        result = subprocess.run(
            ["nmap", "-sV", "-T4", "-Pn", host],
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            timeout=60
        )
        return result.stdout.decode()
    except Exception as e:
        return f"[!] Nmap error: {e}"

def run_nikto(host):
    try:
        result = subprocess.run(
            ["nikto", "-host", host],
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            timeout=90
        )
        return result.stdout.decode()
    except Exception as e:
        return f"[!] Nikto error: {e}"
