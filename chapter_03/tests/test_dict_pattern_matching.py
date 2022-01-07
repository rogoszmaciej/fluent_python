from collections import OrderedDict

import pytest


@pytest.mark.parametrize(
    "pattern, expected_result",
    (
        ({"type": "book", "api": 2, "authors": ["Maciej", "Artur"]}, ["Maciej", "Artur"]),
        (OrderedDict(**{"type": "book", "api": 1, "author": "Maciej"}), ["Maciej"]),
        ({"type": "book"}, "Invalid 'book' record"),
        ({"type": "movie", "director": "Michał"}, ["Michał"]),
        ({"invalid_key": "value"}, "Invalid record"),
    ),
)
def test_dict_is_matched_using_pattern_matching(pattern, expected_result):
    def match_dict(pattern_to_match: dict) -> str:
        match pattern_to_match:  # noqa E999
            case {"type": "book", "api": 2, "authors": [*names]}:
                return names
            case {"type": "book", "api": 1, "author": name}:
                return [name]
            case {"type": "book"}:
                return "Invalid 'book' record"
            case {"type": "movie", "director": name}:
                return [name]
            case _:
                return "Invalid record"

    assert match_dict(pattern_to_match=pattern) == expected_result
