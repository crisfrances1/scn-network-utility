'''This module imports functions from other modules that perform
    specific functions and mnakes them run all together'''

from contents_table import table_out
from find import find_email, print_downloads
from extract import extract_ip
from directory_json import directory_file
from graph import create_graph


def main():
    '''This function runs all the functions imported from other modules'''

    table_out()
    find_email()
    print_downloads()
    extract_ip()
    directory_file()
    create_graph()

if __name__ == '__main__':
    main()
