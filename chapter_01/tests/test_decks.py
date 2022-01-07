from random import choice

from chapter_01.card_deck import Card


def test_card_can_be_initiated():
    beer_card = Card("7", "diamonds")

    assert beer_card.rank == "7"
    assert beer_card.suit == "diamonds"


def test_deck_length_is_evaluated(deck):
    assert len(deck) == 52


def test_first_and_last_card_in_deck_are_retrieved(deck):
    first_card = deck[0]
    last_card = deck[-1]

    assert first_card.rank == "2"
    assert first_card.suit == "spades"
    assert last_card.rank == "A"
    assert last_card.suit == "hearts"


def test_random_card_is_retrieved(deck):
    random_card = choice(deck)

    assert isinstance(random_card, Card)
    assert isinstance(random_card.suit, str)
    assert isinstance(random_card.rank, str)


def test_cards_are_retrieved_by_list_slices(deck):
    slice = deck[:3]

    assert len(slice) == 3
    assert slice == [
        Card(rank="2", suit="spades"),
        Card(rank="3", suit="spades"),
        Card(rank="4", suit="spades"),
    ]


def test_deck_is_iterable(deck):
    for card in deck:
        assert isinstance(card, Card)
    for card in reversed(deck):
        assert isinstance(card, Card)


def test_checking_if_card_is_in_deck_is_evaluated(deck):
    assert Card("Q", "hearts") in deck
    assert not Card("7", "beasts") in deck


def test_deck_is_sorted(deck):
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = ["spades", "clubs", "diamonds", "hearts"]
    cards = [Card(rank=rank, suit=suit) for rank in ranks for suit in suits]

    deck.sort()

    for deck_card, card in zip(deck, cards):
        assert deck_card == card
