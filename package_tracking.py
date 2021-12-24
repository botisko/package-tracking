import argparse
import requests

from bs4 import BeautifulSoup
from datetime import datetime


class CeskaPosta:
    def __init__(self, pkg_tracking_number: str):
        # base URL
        self.base_url = "https://www.postaonline.cz/trackandtrace/-/zasilka/cislo?parcelNumbers="

        # initialize variables for package
        self.pkg_tracking_number = pkg_tracking_number
        self.status_pkg = None
        self.date_pkg = None
        self.psc = None
        self.place = None

        # get the values from Ceska Posta and add them to the variables
        self.initialize()

    def initialize(self):
        try:
            r = requests.get(self.base_url + self.pkg_tracking_number)
        except requests.exceptions.RequestException as e:
            raise e

        html_doc = r.content
        soup = BeautifulSoup(html_doc, 'html.parser')

        # thrown only if the HTML document contains an error, it is almost always an bad number or not a found number
        if soup.select('[class=error]'):
            raise ValueError("Neexistující číslo zásilky!")

        # list comprehension for getting the values from html doc
        status = [
            element.get_text(strip=True)
            for element in soup.select('[class~=datatable2] tr strong')
            if element.get_text(strip=True) != ''
        ]

        self.date_pkg = status[1]
        self.status_pkg = status[2]
        self.psc = status[3]
        self.place = status[4]

        return self

    def date(self) -> datetime.date:
        """Returns datetime object from provided date."""
        return datetime.strptime(self.date_pkg, "%d.%m.%Y").date()

    def status(self):
        """Returns package status."""
        return self.status_pkg

    def tracking_number(self):
        """Returns tracking number of package."""
        return self.pkg_tracking_number

    def postal_code(self):
        """Returns postal code."""
        return self.psc

    def place_arrival(self):
        """Returns place of arrival of the package."""
        return self.place


def print_package_status(delivery: CeskaPosta):
    """
    Prints package info in nice format base on last status
    :param delivery: instance of CeskaPosta
    :return:
    """

    # Get the line length
    current_line = '=' * (len(str(delivery.date())) + len(delivery.status()) + 7)
    no_line = '=' * int((len(current_line) - len(delivery.tracking_number())) / 2)

    # If the no. of chars in package no. is odd, align the printed table
    if len(no_line) % 2 == 0:
        print("{0}{1}{2}".format(no_line, delivery.tracking_number(), no_line))
    else:
        print("{0}{1}{2}=".format(no_line, delivery.tracking_number(), no_line))
    print(current_line)
    print("= {0} | {1} =".format(delivery.date(), delivery.tracking_number()))
    print(current_line)


if __name__ == '__main__':
    # Construct the argument parse and parse the arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--package', required=True, help="Package number")
    args = parser.parse_args()

    # Create a new delivery class
    delivery = CeskaPosta(args.package)
    print_package_status(delivery)
