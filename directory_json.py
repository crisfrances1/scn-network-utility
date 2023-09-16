'''This module imports 2 lists from another module and creates a dictionary
    out of both. It then tries to create a new subdirectory in the current
    working directory where the 2 dictionaries will be stored'''

import os
import os.path
import json
import shutil
import collections
from parse_pcap import source_ip_list, destination_ip_list


source_counter = dict(collections.Counter(source_ip_list))
destination_counter = dict(collections.Counter(destination_ip_list))

current_directory = os.getcwd()
NEW_SUBDIRECTORY = 'Results Subdirectory'
NEW_FILE = 'dataFile.txt'
path_directory = os.path.join(current_directory, NEW_SUBDIRECTORY)
path_file = os.path.join(NEW_SUBDIRECTORY, NEW_FILE)

def write_to_file():
    '''
    Function that opens a file as outfile and dumps the source and
    destination ip addresses
    '''
    try :
        with open(path_file, 'w') as outfile:
            outfile.write('\n - SOURCE IP ADDRESSES - \n')
            outfile.write(' - ip address : packets sent - \n')
            json.dump(source_counter, outfile, indent=4)
            outfile.write('\n - DESTINATION IP ADDRESSES - \n')
            outfile.write(' - ip address : packets received - \n')
            # Dumps the source_counter dictionary in the file
            json.dump(destination_counter, outfile, indent=4)
    except IOError as err :
        print(f'IOError! : {err}')


def directory_file():
    '''
    Gets current directory and sets two variables for the subdirectory
    and JSON file to be created
    '''

    # Standard output
    print(f'\nAttempting to create [{NEW_SUBDIRECTORY}] in current directory:')
    print(f'{current_directory}')

    # Checks if path_directory exists
    check_exists = os.path.exists(NEW_SUBDIRECTORY)

    # If the path exists, program deletes it in order to create the new one
    if check_exists:
        print(f'\nA subdirectory [{NEW_SUBDIRECTORY}] was found.')
        print('Deleting to create new one...')
        shutil.rmtree(NEW_SUBDIRECTORY) # Deletes the already existing subdirectory
        os.mkdir(NEW_SUBDIRECTORY) # Creates subdirectory in current one
        print(f'\nNew [{NEW_SUBDIRECTORY}] created')
        print('Now creating text file for results...')
        print(f'[{NEW_FILE}] was created and IP addresses were succesfully added')
        write_to_file()

    # If the path does not exist, program lets the user know and creates it
    if not check_exists:
        print(f'{path_directory} does not exist, succesfully creating subdirectory...')
        os.mkdir(NEW_SUBDIRECTORY) # Creates subdirectory in current one
        print('\n')
         # Joins path from subdiretory created and the JSON file in order to create it
        print(f'{NEW_FILE} for results created and data was succesfully added')
        write_to_file()
        