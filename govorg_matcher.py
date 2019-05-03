#!/usr/bin/env python3
"""Iterates through a bunch of docs and creates a list of GOV_ORG entities for each doc.
Usage:
    python3 govorg_matcher.py df
"""

import get_govorg_list
import spacy
from spacy_lookup import Entity


# stuff to run always here such as class/def
def text_gov_org_match(text, lookup):

    return ["government digital service", "Government Digital Service"]


def main():
    # print(GOV_ORG)
    pass


if __name__ == '__main__':  # our module is being executed as a program
    # stuff only to run when not called via 'import' here
    # get lookup list
    GOV_ORG = get_govorg_list.main()
    # load english language model
    nlp = spacy.load('en_core_web_sm')
    # look through text
    main()

