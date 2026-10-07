# Program to learn scapy with
from scapy.all import *
from scapy.layers.inet import IP


# Do not run at work since will make device appear as ff:ff:ff:ff:ff:ff which gets alerted as MAC spoofing
def doARP(targetIP):
    ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=targetIP), timeout=2)

    ans.summary(lambda s,r: r.sprintf("%Ether.src% %ARP.psrc%") )

#Need to format well
def doPing(targetIP):
    ans, unans = sr(IP(dst=targetIP) / ICMP(), timeout=2)


# Return boolean if target IP is online or not, will use in future
def isTargetOnline(targetIP):
    ans, unans = sr(IP(dst=targetIP) / ICMP(), timeout=2)
    if ans:
        return True
    else:
        return False
