'''This module opens a pcap file by importing a function and parses it.
    It extracts TCP, UDP and IGMP packets as well as all timestamps
    and IP addresses (source and destination)'''

import socket
import datetime
import dpkt
from openpcap import open_file

file = 'evidence-packet-analysis.pcap'
print(f' opening {file} ... \n')
pcap = open_file(file)

# Counter definitions for all packets and different packet types
counter=0
ipcounter=0
tcpcounter=0
udpcounter=0
igmpcounter=0

# Lists definition for packet types, source & destination IP addresses
source_ip_list =[]
destination_ip_list = []
TCP_timestamps = []
IGMP_timestamps = []
UDP_timestamps = []
all_timestamps = []
tcp_len = []
udp_len = []
igmp_len = []
other_len = []

for ts,pkt in pcap:
    counter+=1
    try:
        # Parse ethernet packet
        eth=dpkt.ethernet.Ethernet(pkt)
        ip=eth.data
        src = socket.inet_ntoa(ip.src)
        dst = socket.inet_ntoa(ip.dst)
        tcp = ip.data
        all_timestamps.append(ts)
        source_ip_list.append(src)
        destination_ip_list.append(dst)
        #extract TCP packets
        if ip.p==dpkt.ip.IP_PROTO_TCP:
            tcpcounter+=1
            tcp = ip.data
            #converts unix time stamps to datetime objects
            TCP_timestamps.append(datetime.datetime.fromtimestamp(ts))
            tcp_len.append(len(pkt))
        #extract UDP packets
        if ip.p==dpkt.ip.IP_PROTO_UDP:
            udpcounter+=1
            udp=ip.data
            #converts unix time stamps to datetime objects
            UDP_timestamps.append(datetime.datetime.fromtimestamp(ts))
            udp_len.append(len(pkt))
        #extract IGMP packets
        if ip.p==dpkt.ip.IP_PROTO_IGMP:
            igmpcounter+=1
            igmp=ip.data
            #converts unix time stamps to datetime objects
            IGMP_timestamps.append(datetime.datetime.fromtimestamp(ts))
            igmp_len.append(len(pkt))
    except Exception as err:
        print(f'Exception!: ({err.__class__.__name__}): {err}')
