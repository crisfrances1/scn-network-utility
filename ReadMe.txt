ReadMe text file for pcap_analyser.py script

Packages Used across all scripts/modules:

Built-in packages:
- os: used for miscellaneous operating system interfaces.
- os.path as part of the os module used for operations on pathnames.
- re: used for regular expression operations.
- socket: used for low-level networking interface.
- json: used to encode and decode the JSON format.
- shutil: used for high-level file operations, including copying.
- time: used for time access and conversions.
- datetime: used for basic date and time types.


Pip installed packages:

- dpkt: pip install dpkt
- prettytable: python -m pip install -U prettytable

Other packages:

- matplotib: to install:
          python -m pip install -U pip
          python -m pip install -U matplotlib

Explanation of files:

The code was divided into different modules that contain from one to multiple
functions in order to future-proof the code.
The main/central script is called pcap_analyser.py. This script imports the
functions from the other modules in order to make them run all together.
In order for teh central script of any of the otehrs to run, the pcap file
needs to be in the same directory as the rest.

  Modules created and what they do:

  - openpcap.py: opens a pcap file.
    PYLINT SCORE: 10/10

  - parse_pcap.py: imports a function from the module above in order to open a
    file and parse its contents.
    PYLINT SCORE: 8.60/10

  - contents_table.py: imports variables from the parse_pcap module in order to
    create a table where the contents of the pcap file will appear summarised.
    PYLINT SCORE: 9.58/10

  - find.py: imports a funciton from the openpcap module and parses the tcp.data
    as a string so that a search using regular expressions can be made to find
    emails in the fields from: and to:.
    PYLINT SCORE: 8.40/10

  - extract.py: imports variables from parse_pcap in order to count how many
    packets where sent from and to each ip address. It does this by creating
    two different dictionaries and counting the repeating ip addresses.
    PYLINT SCORE: 10/10

  - directory_json.py: imports variables from parse_pcap and creates a
    sub-directory in the current working directory. If a directory in the
    current working one already exists with that name, the program deletes the
    old one and creates a new one where a text file will be created. The
    dictionaries created in the module extract.py will then be dumped using the
    json module into the text file.
    PYLINT SCORE: 10/10

  - graph.py: imports a list of timestamps from parse_pcap and iterates
    it in order to get packets counts for each timestamps in a 13s seconds
    interval.
    PYLINT SCORE: 8.57/10


Functionality Requirements not working:

- To create the table where we can see the first and last timestamp for each
  packet type, if the list containing the timestamps for each type is empty,
  the table will not be created.

- I added a row for packet types other than udp, tcp and igmp. However, since
  I was not able to print 'null' or 'none' in case the list was empty for the
  first and last time stamps column and the mean packet length, a '-' was added.

- I was able to plot the graph for packet counts in 13s intervals, however I
  was not able to show the threshold for heavy traffic.


Links:

- Extract filename from Uri:
https://gethowstuff.com/python-extract-file-name-url-path/

- Analyze packets in pcap file:
https://stackoverflow.com/questions/59741466/analyzing-pcap-files-using-dpkt-with-python
asked Jan 14 at 20:39 by TeeGee

- Get first and last timestamps of each traffic type:
https://stackoverflow.com/questions/64989204/getting-the-first-and-last-timestamp-for-a-packet-type-in-a-pcap-file-using-pyth
asked Nov 24 at 15:04 by NI_1402

- Sum function to get mean packet length:
https://www.geeksforgeeks.org/sum-function-python/

- To save a plot from python:
https://problemsolvingwithpython.com/06-Plotting-with-Matplotlib/06.04-Saving-Plots/
