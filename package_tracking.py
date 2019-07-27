import sys

import requests
from bs4 import BeautifulSoup


class CPostPackage:
    """
    Class for storing Ceska posta package information
    """

    def __init__(self):
        """
        Constructor for CPostPackage class.
        """
        # Create some member animals
        self.tracking_number = sys.argv[1]
        self.tracking_url = "https://www.postaonline.cz/trackandtrace/-/zasilka/cislo?parcelNumbers="


def print_package_status(status):
    """
    Prints package info in nice format base on last status
    :param status: Last package status
    :return:
    """
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


def main(cpost_pkg):
    """
    Gets Ceska posta track and trace page and scrape actual package info based on package no.
    :param cpost_pkg: A CPostPackage class with url and track no.
    :return:
    """
    r = requests.get(cpost_pkg.tracking_url + cpost_pkg.tracking_number)

    html_doc = r.content

    soup = BeautifulSoup(html_doc, 'html.parser')

    status = []

    for elm in soup.select('[class~=datatable2] tr strong'):
        # print(elm.get_text(strip=True))
        if elm.get_text(strip=True) is not '':
            status.append(elm.get_text(strip=True))

    print_package_status(status)


if __name__ == '__main__':
    # Create a new delivery class
    delivery = CPostPackage()

    main(delivery)
