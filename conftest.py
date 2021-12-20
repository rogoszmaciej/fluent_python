import pytest
from chapter_01.card_deck import FrenchDeck


@pytest.fixture
def deck() -> "FrenchDeck":
    return FrenchDeck()
