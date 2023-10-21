<img align="right" width="33%" height="33%" src="app/static/wifi-logo.png">

# Ownets

Ownets is a powerful application designed to enhance your WiFi security by identifying connected devices and enabling the user to manage potential threats and unwanted connections.

## Features

- **Device Scanning:** Ownets utilizes Python and PyQt to scan and identify devices connected to your WiFi network.
- **Device De-authentication:** The application allows you to de-authenticate unwanted or suspicious devices, enhancing network security.
- **Manufacturer Information:** Ownets fetches the manufacturer information of connected devices using their MAC addresses and displays it for easy identification.
- **User-friendly Interface:** The PyQt-based user interface ensures ease of use and smooth interaction.
- **Save to a file:** You can save the result to your local machine and retrieve data.

## How It Works

1. Ownets employs the Scapy library to detect all devices connected to the WiFi network.
   - ARP request packets are broadcasted to which connected devices respond with ARP reply packets containing their IP and MAC addresses.
   - [Scapy Documentation](https://scapy.readthedocs.io/en/latest/usage.html#arp-ping/)
2. Manufacturer identification is achieved through the [MAC address lookup](https://maclookup.app/) API.
   - The first 3 octets of the MAC address correspond to the manufacturer's unique identifier.
3. De-authentication packets are created using Scapy and sent to the target device.
   - These 802.11 de-authentication packets include a [reason code](https://docu.units.it/dokuwiki/tabelle:wifi_deauth_reason/) (Default is 1, customizable).
   - Network interface must be in monitor mode to send 802.11 packets.
   - [Aircrack-ng](https://aircrack-ng.org/) is used to enable monitor mode.

## Getting Started

1. Install [NPCAP](https://npcap.com/) for Scapy to function correctly.
2. Clone this repository to your local machine. `git@github.com:AseanK/ownet-scanner.git` or `https://github.com:AseanK/ownet-scanner.git`.
3. Create a `.env` file with the following:

```python
BROADCAST_MAC=ff:ff:ff:ff:ff:ff
API_URL=PREFERRED MAC LOOKUP API # https://maclookup.app/ was used but any should work.
```

4. Install required packages by running `pip install -r requirements.txt`.
5. Launch the application with `python app.py`.
6. Note that monitor mode is not required for scanning devices but is necessary for sending de-authentication packets.

- Learn how to enable monitor mode in the [Aircrack-ng documentation](https://www.aircrack-ng.org/doku.php?id=airmon-ng/).
