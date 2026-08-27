# Network Security Testing Lab

A hands-on cybersecurity portfolio project demonstrating network traffic analysis, packet security testing, TCP/IP concepts and firewall configuration in an isolated virtual lab environment.

## Lab Environment

- Oracle VirtualBox
- SEED Ubuntu Linux
- Docker containers
- Python
- Scapy
- Wireshark
- Linux iptables
- Telnet

## Projects Completed

### 1. Telnet Packet Sniffing
Developed a Python program using Scapy to capture Telnet traffic between hosts in a Docker-based virtual network.

Used Wireshark to verify captured TCP packets and analyse:
- Source and destination IP addresses
- TCP ports
- TCP flags
- Sequence and acknowledgement numbers

### 2. ICMP Sniffing and Spoofing
Used Python and Scapy to capture ICMP echo requests and demonstrate packet spoofing concepts within an isolated lab environment.

### 3. TCP Session Security Testing
Analysed live TCP sessions using Wireshark and explored TCP reset and session hijacking concepts using Scapy.

### 4. Firewall Configuration
Configured Linux iptables firewall rules to:
- Filter ICMP traffic
- Control Telnet access
- Restrict external access to internal systems
- Apply default-deny firewall policies

### 5. Docker Network Lab
Built and managed multi-host cybersecurity environments using Docker containers and SEED Ubuntu.

## Skills Demonstrated

`Python` `Scapy` `Wireshark` `Linux` `Docker` `TCP/IP` `iptables` `Network Security` `Packet Analysis`

## Ethical Use

All security testing documented in this repository was performed in authorised, isolated educational lab environments as part of cybersecurity studies at RMIT University.

The techniques are documented for educational and defensive cybersecurity purposes only.
