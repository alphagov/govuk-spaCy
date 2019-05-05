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


def get_orgid_dict(url='https://government-organisation.register.gov.uk/records.csv?page-size=5000'):
    """Get a dictionary of Government Organisation key (name) and values (id) from the GDS Register.

    This let's us look up the id based on the name of the organisation.
    """
    orgs = requests.get(url)

    orgs = orgs.text
    orgs = StringIO(orgs)
    df = read_csv(orgs)

    # Set unique Register's org ID as key and name as value
    keys = df['name'].values
    values = df['government-organisation'].values
    dictionary = dict(zip(keys, values))

    gov_orgs_dict = dictionary

    return gov_orgs_dict


if __name__ == '__main__':  # our module is being executed as a program
    main()
