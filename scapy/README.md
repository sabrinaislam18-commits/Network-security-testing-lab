# Scapy Network Security Labs

Hands-on Python and Scapy network security exercises completed in an isolated virtual lab environment as part of Security Testing coursework at RMIT University.

The material has been adapted and sanitised for this cybersecurity portfolio.

## Lab Environment

- SEED Ubuntu Linux
- Docker containers
- Python 3
- Scapy
- Wireshark
- TCP/IP
- Telnet

## Lab Demonstrations

### Telnet Packet Sniffing
**File:** `telnet_packet_sniffing.py`

Used Scapy with a BPF filter to capture TCP port 23 traffic between hosts in an isolated Docker network.

Wireshark was used to independently verify the captured Telnet packets.

### ICMP Packet Sniffing
**File:** `icmp_packet_sniffing.py`

Captured ICMP network traffic using Scapy and inspected packet header information.

### ICMP Spoofing
**File:** `icmp_spoofing_demo.py`

Captured ICMP Echo Requests and constructed corresponding ICMP Echo Replies to demonstrate packet spoofing concepts in an authorised lab environment.

### TCP Session Reset
**File:** `tcp_session_reset_demo.py`

Analysed an active TCP/Telnet session using Wireshark and demonstrated the TCP reset concept using a crafted Scapy packet.

### TCP Session Hijacking
**File:** `tcp_session_hijacking_demo.py`

Analysed TCP sequence and acknowledgement numbers and demonstrated TCP session manipulation using Scapy within an isolated lab environment.

## Skills Demonstrated

`Python` `Scapy` `Wireshark` `Docker` `Linux` `TCP/IP` `Packet Analysis` `Network Security`

## Ethical Use

All demonstrations were performed in an authorised and isolated educational environment.

These examples are provided for educational and defensive cybersecurity purposes only.
