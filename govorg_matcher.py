#!/usr/bin/env python3
"""
Named Entities are matched using the python module spacy-lookup,
 and looks up in the data provided by different dictionaries.

Iterates through a bunch of docs and creates a list of GOV_ORG entities for each doc.
Usage:
    python3 govorg_matcher.py df
"""

import get_govorg_list
import spacy
from spacy_lookup import Entity


# stuff to run always here such as class/def
# if we call the function after import, need nlp defined
nlp = spacy.load('en_core_web_sm')
# get lookup
GOV_ORG = get_govorg_list.main()
# Create custom entity list
entity = Entity(keywords_list=GOV_ORG, label='GOV_ORG')
# happens after other processing steps
nlp.add_pipe(entity, last=True)


def text_gov_org_match(text):
    """Return a list of GOV_ORG entities found at least once in a str."""
    doc = nlp(text)
    # remove any duplicates because dictionaries cannot have duplicate keys
    list_of_gov_org_entities_with_duplicates = [token._.canonical for token in doc if token._.is_entity]
    list_no_duplicates = list(dict.fromkeys(list_of_gov_org_entities_with_duplicates))
    return list_no_duplicates


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

