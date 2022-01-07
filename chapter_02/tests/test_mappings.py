from typing import Any

import pytest


@pytest.mark.parametrize(
    "pattern, expected_result",
    (
        (["BEEPER", 45.0, 5], "BEEPER"),
        (["NECK", 45.0], "ROTATE_NECK"),
        (["LED", "led-1", 2], "SET_LED_BRIGHTNESS"),
        (["LED", "led-2", 255, 125, 200], "SET_LED_COLOR"),
        (["LED", "led-2", 255, 125], "NO_MATCH"),
        ([None], "NO_MATCH"),
    ),
)
def test_patterns_are_matched(pattern: Any, expected_result: str):
    def match_pattern(pattern_to_match: Any) -> str:
        match pattern_to_match:  # noqa E999
            case ["BEEPER", frequency, count]:
                return "BEEPER"
            case ["NECK", angle]:
                return "ROTATE_NECK"
            case ["LED", ident, intensity]:
                return "SET_LED_BRIGHTNESS"
            case ["LED", ident, red, green, blue]:
                return "SET_LED_COLOR"
            case _:
                return "NO_MATCH"

    assert match_pattern(pattern_to_match=pattern) == expected_result


@pytest.mark.parametrize(
    "pattern, expected_result",
    (
        (("Tokyo", "JP", 36.933, (35.689722, 139.691667)), "MATCHED_CITY"),
        (("Delhi NCR", "IN", 21.935), "NO_COORDINATES"),
        (None, "NO_MATCH"),
    ),
)
def test_patterns_containing_tuples_are_matched(pattern: Any, expected_result: str):
    def match_pattern(pattern_to_match: Any) -> str:
        match pattern_to_match:
            case [city, country_code, _, (lat, lon)]:
                return "MATCHED_CITY"
            case [city, country_code, number]:
                return "NO_COORDINATES"
            case _:
                return "NO_MATCH"

    assert match_pattern(pattern_to_match=pattern) == expected_result


@pytest.mark.parametrize(
    "pattern, expected_result",
    (
        (["BEEPER", 45.0, 5], "BEEPER"),
        (["BEEPER", 45.0, "5"], "NO_MATCH"),
        (["BEEPER", 45.0, "asdf"], "NO_MATCH"),
        (["NECK", 45.0], "ROTATE_NECK"),
        (["NECK", "45.0"], "NO_MATCH"),
        (["LED", "led-1", 2], "SET_LED_BRIGHTNESS"),
        (["LED", "led-2", 255, 125, 200], "SET_LED_COLOR"),
        (["LED", 2, 255, 125, 200], "NO_MATCH"),
        (["LED", "led-2", 255, 125], "NO_MATCH"),
        ([None], "NO_MATCH"),
    ),
)
def test_patterns_with_typing_are_matched(pattern: Any, expected_result: str):
    def match_pattern(pattern_to_match: Any) -> str:
        match pattern_to_match:
            case ["BEEPER", float(frequency), int(count)]:
                return "BEEPER"
            case ["NECK", float(angle)]:
                return "ROTATE_NECK"
            case ["LED", str(ident), int(intensity)]:
                return "SET_LED_BRIGHTNESS"
            case ["LED", str(ident), int(red), int(green), int(blue)]:
                return "SET_LED_COLOR"
            case _:
                return "NO_MATCH"

    assert match_pattern(pattern_to_match=pattern) == expected_result
