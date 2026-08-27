#!/usr/bin/env python3

from scapy.all import *

def print_pkt(pkt):
    print_pkt.counter += 1
    print("------------- packet:", print_pkt.counter, "-------------")
    pkt.show()

print_pkt.counter = 0

pkt = sniff(
    iface="br-bad22f081d4d",
    filter="tcp port 23 and host 10.9.0.5 and host 10.9.0.6",
    prn=print_pkt
)