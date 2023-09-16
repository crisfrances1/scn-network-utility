'''This module imports a list with all packet timestamps (all_timestamps)
    from the parse_pcap module in order to group packet counts by
    interval length and then create a line chart'''

import time
import os
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from parse_pcap import all_timestamps
from directory_json import path_directory


def unix_to_date_string(unix_timestamp):
    ''' Formats string from unix timestamp to YYYY-MM-DD HH:MM:SS'''
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(unix_timestamp))


def create_graph():
    '''
    For every timestamp in all_timestamps, if the timestamp is smaller
    than the next timestamp + the interval, a packet is added to the
    counter
    '''
    interval = 13
    start_ts = all_timestamps[0]
    myTimeDict = {}
    counter = 0 # Counter of packets per interval
    print(f'\nNow counting packets in {interval}s intervals and creating line chart...\n')
    
    for date in all_timestamps:
        if date < (start_ts + interval):
            counter += 1
        else:
            myTimeDict[unix_to_date_string(start_ts)] = counter
            counter = 1
            start_ts += interval

    # Prints the keys and values in dictionary
    for key, value in myTimeDict.items():
        print(key, ' : ', value)
    # Creates a sorted list out of the dictionary
    chart_list = sorted(myTimeDict.items())
    x, y = zip(*chart_list)

    # Create figure
    fig, ax = plt.subplots()
    plt.plot(x, y)

    # Set title for both axes
    ax.set_title('Number of packets against time')
    ax.set_xlabel('timestamps', fontsize='10', fontweight='bold')
    ax.set_ylabel('packet counts', fontsize='10', fontweight='bold')

    # Format timestamps
    ax.fmt_xdata = mdates.DateFormatter('%H:%M:%S')
    plt.gcf().autofmt_xdate()

    # Create legend
    plt.legend(['Packets'])
    # Save graph to subdirectory
    my_file = 'figure.png'
    fig.savefig(os.path.join(path_directory, my_file), dpi=300, bbox_inches='tight')

    # Show figure
    plt.show()
    