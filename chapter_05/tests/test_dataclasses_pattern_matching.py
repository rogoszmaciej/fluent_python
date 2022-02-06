from typing import List

import pytest
from chapter_05.dataclasses import City

cities = [
    City("Asia", "Tokyo", "JP"),
    City("Asia", "Osaka", "JP"),
    City("Asia", "Delhi", "IN"),
    City("North America", "Mexico City", "MX"),
    City("North America", "New York", "US"),
    City("South America", "São Paulo", "BR"),
]


def test_dataclasses_are_matched_by_attribute_value():
    def match_cities(cities: List[City]):
        results = []
        for city in cities:
            match city:  # noqa E999
                case City(continent="Asia", name=name):
                    # In this case name variable gets the instance name attribute value
                    results.append(name)
        return results

    results = match_cities(cities=cities)

    assert len(results) == 3
    assert results == ["Tokyo", "Osaka", "Delhi"]


def test_dataclasses_are_matched_by_multiple_attributes():
    def match_cities(cities: List[City]):
        results = []
        for city in cities:
            match city:  # noqa E999
                case City(continent="Asia", country="JP"):
                    results.append(city)
        return results

    results = match_cities(cities=cities)

    assert len(results) == 2
