'''This module opens a pcap file by importing the open_file function
    and then looks for email addresses in the from: and to: fields in
    the find_email function. In addition it prints the uri requests'''

import re
import dpkt
from openpcap import open_file

file = 'evidence-packet-analysis.pcap'
pcap = open_file(file)


def find_email():
    '''
    Finds any email addresses present in fields from: and to: by
    using regular expressions
    '''
    to_mail = []
    to_mail_dic = {}
    from_mail = []
    from_mail_dic = {}
    print('\n Now looking for email addresses in {file}...')

    for time, pkts in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(pkts)
            ip = eth.data
            tcp =  ip.data
            # Converts tcp.data to string so we can use regex on it
            smtp = str(tcp.data).lower()
            # If field 'to:' is present then look for email addresses
            to_search = re.search(r'to:', smtp)
            if to_search:
                match = re.search(r'[\w\.-]+@[\w\.-]+', smtp)
                if match:
                    to_mail.append(match.group(0))
                    to_mail_dic = list( dict.fromkeys(to_mail) )
            # If field 'from:' is present then look for email addresses
            from_search = re.search(r'from:', smtp)
            if from_search:
                match = re.search(r'[\w\.-]+@[\w\.-]+', smtp)
                if match:
                    from_mail.append(match.group(0))
                    from_mail_dic = list( dict.fromkeys(from_mail) )
        except Exception as err:
            print(f'Exception!: ({err.__class__.__name__}): {err}')
    
    print('\nUnique EMAIL addresses found in [FROM:] field: ')
    for items in from_mail_dic:
        print(f'[*]{items}')
    print('\nUnique EMAIL addresses found in [TO:] field: ')
    for items in to_mail_dic:
        print(f'[*]{items}')


def findDownload(pcap):
    '''
    In current form, finds any gif, png or jpeg files downloaded and prints
    the URI and file name
    '''

    found = False
    for time, buf in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            tcp = ip.data
            http = dpkt.http.Request(tcp.data)
            if http.method == 'GET':
                uri = http.uri.lower()
                # If the tcp.data is an http & GET request:
                if '.gif' in uri:
                    # Extracts the download file name
                    firstpos = uri.rfind("/")
                    lastpos = uri.rfind(".")
                    file_name = uri[firstpos+1:lastpos]
                    print(f'\nGIF [!]  {uri} -- [FILE NAME]: {file_name}\n')
                    found = True
                if '.png' in uri:
                    # Extracts the download file name
                    firstpos = uri.rfind("/")
                    lastpos = uri.rfind(".")
                    file_name = uri[firstpos+1:lastpos]
                    print(f'PNG [!]  {uri} -- [FILE NAME]: {file_name}')
                    found = True
                if '.jpg' in uri:
                    # Extracts the download file name
                    firstpos = uri.rfind("/")
                    lastpos = uri.rfind(".")
                    file_name = uri[firstpos+1:lastpos]
                    print(f'\nJPEG [!]  {uri} -- [FILE NAME]: {file_name}\n')
                    found = True
        except Exception:
            pass
    return found


def print_downloads():
    '''
    Opens the pcap file and calls the above function and prints the
    results. If no resultsd are found, it prints a no downloads found
    message
    '''
    file = 'evidence-packet-analysis.pcap'
    pcap = open_file(file)
    print(f'\n Analysing {file} for PNG, GIF and JPEG files')
    # Call findDownload which prints results
    result = findDownload(pcap)
    if result is False:
        print('No downloads found in this file')
