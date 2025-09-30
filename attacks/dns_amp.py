import threading
import time

def dns_amp(target, port=53, threads=10, test_mode=True, duration=10):
    print("[!] DNS Amplification - For educational use only! (Test mode only in this demo)")
    stop_time = time.time() + duration
    def flood():
        while time.time() < stop_time:
            print(f"[TEST] Would send spoofed DNS request to open resolver targeting {target}:{port}")
    thread_list = []
    for _ in range(threads):
        t = threading.Thread(target=flood)
        t.start()
        thread_list.append(t)
    for t in thread_list:
        t.join()
    print("[+] DNS Amplification completed.")
