'''This module has a function called open_file that takes in a file
    as an argument and opens it for later use'''

import dpkt

def open_file(file):
    '''This function opens a pcap file'''
    try:
        opened_file = open(file, 'rb')
        pcap = dpkt.pcap.Reader(opened_file)
    except FileNotFoundError as err:
        print(f'Check file/path: {err}')
    return pcap
