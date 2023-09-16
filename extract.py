'''This modules imports 2 lists from the parse_pcap module:
    a list for the source IP addresses and a list for the
    destination IP addresses. It counts how many packets
    where sent from and to each ip address'''

import collections
from parse_pcap import source_ip_list, destination_ip_list


def extract_ip():
    '''
    Creates a dictionary out of the source & destination list so
    there is no repeated values and then counts each repeated value
    '''
    source_counter = {}
    destination_counter = {}
    source_counter = dict(collections.Counter(source_ip_list))
    print('\nCounting how many packets were sent from IP address... \n')
    for value, key in sorted(source_counter.items(), key=lambda item: item[1], reverse=True):
        print(f'{key} packets sent from: {value}')
    print('\n')
    destination_counter = dict(collections.Counter(destination_ip_list))
    print('Counting how many packets were sent to IP address... \n')
    for value, key in sorted(destination_counter.items(), key=lambda item: item[1], reverse=True):
        print(f'{key} packets sent to: {value}')
    print('\n')
    return(source_counter, destination_counter)
