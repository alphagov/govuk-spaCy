import govorg_matcher
import get_govorg_list

GOV_ORG = get_govorg_list.main()


def test_text_gov_org_match():
    assert govorg_matcher.text_gov_org_match(text=u"The government digital service is an awesome place to work",
                                             lookup=GOV_ORG) ==\
           ["government digital service", "Government Digital Service"]
