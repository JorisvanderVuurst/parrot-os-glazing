import os
import platform
import threading

def host_discovery(network_prefix, start=1, end=254, threads=10, test_mode=False, duration=None):
    print("[!] Host Discovery (Ping Sweep) - For educational use only!")
    live_hosts = []
    def ping(ip):
        if test_mode:
            print(f"[TEST] Would ping {ip}")
            return
        param = '-n' if platform.system().lower()=='windows' else '-c'
        command = f"ping {param} 1 {ip} > nul 2>&1" if platform.system().lower()=='windows' else f"ping {param} 1 {ip} > /dev/null 2>&1"
        response = os.system(command)
        if response == 0:
            print(f"[+] Host {ip} is up")
            live_hosts.append(ip)
    threads_list = []
    for i in range(start, end+1):
        ip = f"{network_prefix}.{i}"
        t = threading.Thread(target=ping, args=(ip,))
        t.start()
        threads_list.append(t)
        if len(threads_list) >= threads:
            for t in threads_list:
                t.join()
            threads_list = []
    for t in threads_list:
        t.join()
    print("[i] Host discovery completed.")
    if not test_mode:
        print(f"Live hosts: {live_hosts}")
