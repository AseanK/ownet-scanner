import scapy.all as scapy
import requests
import config


BROADCAST_MAC = config.Config.BROADCAST_MAC
API_URL = config.Config.API_URL


def mac_lookup(mac_add):
    return requests.get(API_URL.format(mac_add), timeout=3)


def get_ip_addr():
    return f"{scapy.conf.route.route('8.8.8.8')[2]}/24"


def send_packets(ip_addr):
    """Expected parameter: <String> Access point IP address.
    If error, try host device IP address.
    returns <List> of connected devices.
    """
    connected = []

    request = scapy.ARP()

    request.pdst = ip_addr
    broadcast = scapy.Ether()
        
    broadcast.dst = BROADCAST_MAC
        
    request_broadcast = broadcast / request
    clients = scapy.srp(request_broadcast, timeout = 10,verbose = 1)[0]
    for element in clients:
        response = mac_lookup(element[1].hwsrc).json()
        connected.append({"ip": element[1].psrc, 
                        "mac": element[1].hwsrc, 
                        "company": response["company"], 
                        "address": response["address"], 
                        "country": response["country"]
                        })
    return connected