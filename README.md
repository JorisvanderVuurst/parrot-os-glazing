# Parrot OS DoS & Scanning Educational Tool

**WARNING: This tool is for educational and authorized testing purposes only. Unauthorized use against systems you do not own is illegal and unethical.**

## Features
- Modular attack system: HTTP Flood, UDP Flood, SYN Flood (test mode), Slowloris, ICMP Flood (test mode), DNS Amplification (test mode)
- Network scanning: Port scan, Host discovery (ping sweep)
- Proxy support for HTTP/Slowloris attacks (HTTP/SOCKS proxies)
- Planned: Agent/Controller (botnet) mode for distributed educational testing
- Planned: Network user DoS (ARP spoofing, DHCP starvation, deauth, etc.)
- User-friendly CLI
- Test mode for safe learning
- Educational warnings and confirmations
- Easy to extend with new attack or scan modules

## Legal & Ethical Disclaimer
- Only use this tool on systems you own or have explicit permission to test.
- Misuse can result in criminal charges and severe penalties.
- The authors are not responsible for any misuse or damage caused by this tool.

## Setup
1. Install Python 3.7+
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. (Optional) For advanced attacks, install `scapy`:
   ```bash
   pip install scapy
   ```

## Usage
```bash
python main.py --attack <attack> <target> [options]
python main.py --scan <scan> <target> [options]
python main.py --agent
python main.py --controller
```

### Proxy Support
- Use `--proxy-file proxies.txt` to provide a list of proxies (one per line, format: ip:port).
- Supported in HTTP Flood and Slowloris attacks.

### Attack Examples
```bash
python main.py --attack http_flood example.com --threads 20 --duration 30 --proxy-file proxies.txt
python main.py --attack slowloris example.com -p 80 --threads 10 --test --proxy-file proxies.txt
python main.py --attack icmp_flood 192.168.1.1 --test
```

### Scan Examples
```bash
python main.py --scan port_scan 192.168.1.1 --threads 50
python main.py --scan host_discovery 192.168.1 --threads 20 --test
```

### Agent/Controller Mode (Planned)
- `--agent`: Run as agent, waiting for controller commands (for distributed educational testing)
- `--controller`: Run as controller, sending commands to agents

### Options
- `--attack`: Type of attack (`http_flood`, `udp_flood`, `syn_flood`, `slowloris`, `icmp_flood`, `dns_amp`)
- `--scan`: Type of scan (`port_scan`, `host_discovery`)
- `target`: Target IP, domain, or network prefix (for host discovery)
- `-p`, `--port`: Target port (if applicable)
- `-t`, `--threads`: Number of threads (default: 10)
- `--test`: Test mode (no real attack/scan)
- `--duration`: Duration in seconds (default: 10)
- `--proxy-file`: File with list of proxies (ip:port)
- `--agent`: Run in agent mode (planned)
- `--controller`: Run in controller mode (planned)

## Educational Content
- **Denial of Service (DoS)**: An attack meant to make a machine or network resource unavailable to its intended users.
- **Types of Attacks**:
  - **HTTP Flood**: Overwhelms a web server with HTTP requests.
  - **UDP Flood**: Sends large numbers of UDP packets to random ports.
  - **SYN Flood**: Exploits the TCP handshake by sending SYN packets (test mode only here).
  - **Slowloris**: Holds many HTTP connections open to exhaust server resources.
  - **ICMP Flood**: Sends many ICMP echo requests (pings) to a target (test mode only here).
  - **DNS Amplification**: Exploits open DNS resolvers to amplify traffic toward a target (test mode only here).
- **Scanning**:
  - **Port Scan**: Checks which ports are open on a target system.
  - **Host Discovery**: Identifies live hosts on a network (ping sweep).
- **Proxies**: Used to anonymize or distribute attack traffic (for educational demonstration only).
- **Agents/Controllers**: Simulate distributed attacks in a safe, educational environment (planned).
- **Network User DoS**: Techniques like ARP spoofing, DHCP starvation, and deauth attacks can disrupt users on a network. These are dangerous and should only be used in test mode or with explicit permission (planned).

## Extending
Add new attack or scan modules in the `attacks/` or `scanning/` directory and register them in their respective `__init__.py`.

## License
MIT (for educational use only)
