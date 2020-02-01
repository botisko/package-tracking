import sys

import requests
from bs4 import BeautifulSoup
import argparse


class CPostPackage:
    """
    Class for storing Ceska posta package information
    """

    def __init__(self, tracking_number="DR1234567890E"):
        """
        Constructor for CPostPackage class.
        """
        # Create some member animals
        self.tracking_number = tracking_number
        self.tracking_url = "https://www.postaonline.cz/trackandtrace/-/zasilka/cislo?parcelNumbers="


def print_package_status(status):
    """
    Prints package info in nice format base on last status
    :param status: Last package status
    :return:
    """
    # Check if the input is list
    if type(status) is not list:
        raise TypeError

    # Get date and status
    package_no = str(status[0])
    package_date = str(status[1])
    package_status = str(status[2])

    # Get the line length
    current_line = '=' * (len(package_date) + len(package_status) + 7)
    no_line = '=' * int((len(current_line) - len(package_no)) / 2)

    # If the no. of chars in package no. is odd, align the printed table
    if len(no_line) % 2 is 0:
        print("{0}{1}{2}".format(no_line, package_no, no_line))
    else:
        print("{0}{1}{2}=".format(no_line, package_no, no_line))
    print(current_line)
    print("= {0} | {1} =".format(package_date, package_status))
    print(current_line)


def find_package_status(cpost_pkg):
    """
    Gets Ceska posta track and trace page and scrape actual package info based on package no.
    :param cpost_pkg: A CPostPackage class with url and track no.
    :return:
    """
    try:
        r = requests.get(cpost_pkg.tracking_url + cpost_pkg.tracking_number)
    except requests.exceptions.RequestException as e:
        print("{0}".format(e))

    html_doc = r.content

    soup = BeautifulSoup(html_doc, 'html.parser')

    status = []

    for elm in soup.select('[class~=datatable2] tr strong'):
        # print(elm.get_text(strip=True))
        if elm.get_text(strip=True) is not '':
            status.append(elm.get_text(strip=True))

    try:
        print_package_status(status)
    except IndexError as e:
        print("Neexistujici cislo zasilky!".format(e))
        sys.exit(0)


if __name__ == '__main__':
    # Construct the argument parse and parse the arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--package', required=True, help="Package number")
    args = parser.parse_args()

    # Create a new delivery class
    delivery = CPostPackage(args.package)
    find_package_status(delivery)
