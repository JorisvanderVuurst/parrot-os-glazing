def print_warning():
    print("""
[!] WARNING: This tool is for educational and testing purposes only.\n"""
          "Unauthorized use against systems you do not own is illegal.\n"
          "Always have permission before testing.\n")

def print_stats():
    print("[i] Attack finished. (Stats feature coming soon)")

def load_proxies(proxy_file):
    proxies = []
    try:
        with open(proxy_file, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    proxies.append(line)
    except Exception as e:
        print(f"[!] Could not load proxies: {e}")
    return proxies
