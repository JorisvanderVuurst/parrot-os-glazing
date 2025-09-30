import socket
import threading

def port_scan(target, ports=None, threads=10, test_mode=False, duration=None):
    print("[!] Port Scan - For educational use only!")
    if ports is None:
        ports = list(range(1, 1025))
    open_ports = []
    def scan_port(port):
        if test_mode:
            print(f"[TEST] Would scan port {port} on {target}")
            return
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"[+] Port {port} open on {target}")
                open_ports.append(port)
            s.close()
        except Exception:
            pass
    threads_list = []
    for port in ports:
        t = threading.Thread(target=scan_port, args=(port,))
        t.start()
        threads_list.append(t)
        if len(threads_list) >= threads:
            for t in threads_list:
                t.join()
            threads_list = []
    for t in threads_list:
        t.join()
    print("[i] Port scan completed.")
    if not test_mode:
        print(f"Open ports: {open_ports}")
