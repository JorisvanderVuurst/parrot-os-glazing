import argparse
import sys
from attacks import available_attacks
from scanning import available_scans
from utils import print_warning, print_stats, load_proxies

def main():
    print_warning()
    parser = argparse.ArgumentParser(
        description="Educational DoS & Scanning Tool for Parrot OS - For learning and testing only!"
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--attack", choices=available_attacks(), help="Type of DoS attack to launch"
    )
    group.add_argument(
        "--scan", choices=available_scans(), help="Type of scan to perform"
    )
    parser.add_argument("target", help="Target IP, domain, or network prefix (for scan)")
    parser.add_argument("-p", "--port", type=int, default=None, help="Target port (if applicable)")
    parser.add_argument("-t", "--threads", type=int, default=10, help="Number of threads (default: 10)")
    parser.add_argument("--test", action="store_true", help="Run in test mode (no real attack/scan)")
    parser.add_argument("--duration", type=int, default=10, help="Duration in seconds (default: 10)")
    parser.add_argument("--proxy-file", type=str, default=None, help="File with list of proxies (ip:port)")
    parser.add_argument("--agent", action="store_true", help="Run in agent mode (wait for controller commands)")
    parser.add_argument("--controller", action="store_true", help="Run in controller mode (send commands to agents)")
    args = parser.parse_args()

    if not confirm_educational():
        print("Aborted.")
        sys.exit(0)

    proxies = load_proxies(args.proxy_file) if args.proxy_file else None

    if args.agent:
        print("[i] Agent mode not yet implemented. (Planned for educational distributed testing)")
        sys.exit(0)
    if args.controller:
        print("[i] Controller mode not yet implemented. (Planned for educational distributed testing)")
        sys.exit(0)

    if args.attack:
        attack_func = available_attacks()[args.attack]
        attack_func(
            target=args.target,
            port=args.port,
            threads=args.threads,
            test_mode=args.test,
            duration=args.duration,
            proxies=proxies
        )
    elif args.scan:
        scan_func = available_scans()[args.scan]
        if args.scan == "host_discovery":
            scan_func(
                network_prefix=args.target,
                threads=args.threads,
                test_mode=args.test
            )
        else:
            scan_func(
                target=args.target,
                threads=args.threads,
                test_mode=args.test
            )
    print_stats()

def confirm_educational():
    resp = input("This tool is for educational use only. Do you agree? (yes/no): ")
    return resp.strip().lower() == "yes"

if __name__ == "__main__":
    main()
