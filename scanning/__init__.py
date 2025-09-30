from .port_scan import port_scan
from .host_discovery import host_discovery

def available_scans():
    return {
        "port_scan": port_scan,
        "host_discovery": host_discovery,
    }
