from scapy.all import *
packet = IP(dst="www.example.com")/ICMP()
