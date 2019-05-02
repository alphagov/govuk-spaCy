#!/usr/bin/env python3
"""Get a list of str of Government Organisation names from the GDS Register.
Usage:
    python3 get_govorg_list.py
"""

import requests
from pandas import read_csv
from io import StringIO


def main(url='https://government-organisation.register.gov.uk/records.csv?page-size=5000'):
    """Get a list of str of Government Organisation names from the GDS Register."""
    orgs = requests.get(url)

    orgs = orgs.text
    orgs = StringIO(orgs)
    df = read_csv(orgs)
    # print(df.name.values)

    gov_orgs = list(df.name.values)

    return gov_orgs


if __name__ == '__main__':  # our module is being executed as a program
    main()
