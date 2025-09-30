from .http_flood import http_flood
from .udp_flood import udp_flood
from .syn_flood import syn_flood
from .slowloris import slowloris
from .icmp_flood import icmp_flood
from .dns_amp import dns_amp

def available_attacks():
    return {
        "http_flood": http_flood,
        "udp_flood": udp_flood,
        "syn_flood": syn_flood,
        "slowloris": slowloris,
        "icmp_flood": icmp_flood,
        "dns_amp": dns_amp,
    }
