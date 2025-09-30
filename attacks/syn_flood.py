import threading
import time

def syn_flood(target, port=80, threads=10, test_mode=True, duration=10):
    print("[!] SYN Flood - For educational use only! (Test mode only in this demo)")
    stop_time = time.time() + duration
    def flood():
        while time.time() < stop_time:
            print(f"[TEST] Would send SYN packet to {target}:{port}")
    thread_list = []
    for _ in range(threads):
        t = threading.Thread(target=flood)
        t.start()
        thread_list.append(t)
    for t in thread_list:
        t.join()
    print("[+] SYN Flood completed.")
