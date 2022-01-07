from collections import ChainMap, defaultdict

import pytest


def test_default_factory_missing_raises_key_error():
    test_dict = defaultdict()
    test_dict["name"] = "Maciej"

    with pytest.raises(KeyError):
        test_dict["last_name"]


def test_default_factory_is_used_when_dict_key_is_missing():
    def get_default():
        return "Default value"

    test_dict = defaultdict(get_default)
    test_dict.update(**{"first_name": "Maciej", "last_name": "Rogosz"})

    assert test_dict["job"] == "Default value"


def test_custom_default_dict_items_are_retrieved(default_dict):
    assert default_dict[2] == "two" == default_dict.get(2)
    assert default_dict[4] == "four" == default_dict.get(4)
    assert default_dict.get(1, "N/A") == "N/A"


def test_custom_default_dict_non_existing_key_raises_error(default_dict):
    with pytest.raises(KeyError):
        default_dict[1]


def test_items_are_looked_up_in_chain_map():
    dict_1 = {"first_name": "Maciej", "last_name": "Rogosz"}
    dict_2 = {"position": "developer", "email": "test@example.com"}

    chain_map = ChainMap(dict_1, dict_2)

    assert chain_map["first_name"] == "Maciej"
    assert chain_map["last_name"] == "Rogosz"
    assert chain_map["position"] == "developer"
    assert chain_map["email"] == "test@example.com"


def test_sets_intersection():
    list_1 = ["test@example.com", "test1@example.com", "test2@example.com"]
    list_2 = [
        "test1@example.com",
        "test2@example.com",
        "test3@example.com",
        "test4@example.com",
        "test5@example.com",
        "test6@example.com",
        "test7@example.com",
        "test8@example.com",
        "test9@example.com",
        "test10@example.com",
    ]
    needles = set(list_1)
    haystack = set(list_2)

    occurences = needles & haystack
    occurences_2 = set(list_1).intersection(list_2)

    assert len(occurences) == 2 == len(occurences_2)
    assert occurences == set(["test1@example.com", "test2@example.com"]) == occurences_2


def test_set_literals():
    pass
