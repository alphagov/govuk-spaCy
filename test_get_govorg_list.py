import get_govorg_list


def test_get_govorg_list():
    GOV_ORG = get_govorg_list.main()
    assert isinstance(GOV_ORG, list) is True
