'''This module imports multiple variables and lists from the parse_pcap
    module. It takes in those variables to create a table in order to
    summarise the contents'''

import collections
from prettytable import PrettyTable
from parse_pcap import counter, tcpcounter, udpcounter, igmpcounter
from parse_pcap import TCP_timestamps, UDP_timestamps, IGMP_timestamps
from parse_pcap import tcp_len, igmp_len, udp_len

def table_out():
    '''Imports counters for tcp, igmp, udp and 'other' packets from the
    parse_pcap moduleand creates a table. Th other counter is
    calculated by substracting all the other counters to the total
    counter
    '''
    othercounter = counter - (tcpcounter + udpcounter + igmpcounter)
    headers = ['Packet type', 'Number of packets', 'First timestamp', 'Last timestamp', 'Mean packet length']
    # Create header
    table = PrettyTable(headers)
    # Gets mean packet length for each packet type
    # Formats result to only to decimal points
    tcp_len_counter = dict(collections.Counter(tcp_len))
    tcpavg = sum(k*v for k,v in tcp_len_counter.items()) / tcpcounter
    formatted_tcpavg = '{:.2f}'.format(tcpavg)

    udp_len_counter = dict(collections.Counter(udp_len))
    udpavg = sum(k*v for k,v in udp_len_counter.items()) / udpcounter
    formatted_udpavg = '{:.2f}'.format(udpavg)

    igmp_len_counter = dict(collections.Counter(igmp_len))
    igmpavg = sum(k*v for k,v in igmp_len_counter.items()) / igmpcounter
    formatted_igmpavg = '{:.2f}'.format(igmpavg)

    # Add records to table
    table.add_row(['TCP', tcpcounter, TCP_timestamps[0], TCP_timestamps[-1], formatted_tcpavg])
    table.add_row(['UDP', udpcounter, UDP_timestamps[0], UDP_timestamps[-1], formatted_udpavg])
    table.add_row(['IGMP', igmpcounter, IGMP_timestamps[0], IGMP_timestamps[-1], formatted_igmpavg])
    table.add_row(['OTHER', othercounter, '-', '-', '-'])


    print('\n Total number of ETHERNET packets in the PCAP file :', counter)
    print(table, '\n ...table created successfully')
