from collections import deque

import pytest
from chapter_01.card_deck import FrenchDeck
from chapter_01.vector import Vector
from chapter_03.mappings import DefaultDict


@pytest.fixture
def deck() -> "FrenchDeck":
    return FrenchDeck()


@pytest.fixture
def vector() -> "Vector":
    return Vector(x=3, y=4)


@pytest.fixture
def dq() -> "deque":
    return deque(iterable=range(10), maxlen=10)


@pytest.fixture
def default_dict() -> "DefaultDict":
    data = [(2, "two"), (4, "four")]
    return DefaultDict(data)
