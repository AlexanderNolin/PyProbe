# Program to learn scapy with
from scapy.all import *


def doARP(targetIP):
    ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=targetIP), timeout=2)

    ans.summary(lambda s,r: r.sprintf("%Ether.src% %ARP.psrc%") )

doARP("10.20.18.2")