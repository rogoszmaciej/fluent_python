from collections import namedtuple
from typing import List

Card = namedtuple("Card", ("rank", "suit"))


class FrenchDeck:
    ranks: List[str] = [str(n) for n in range(2, 11)] + list("JQKA")
    suits: List[str] = "spades diamonds clubs hearts".split()
    suit_values = {"spades": 3, "hearts": 2, "diamonds": 1, "clubs": 0}

    def __init__(self) -> None:
        self._cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]

    def __len__(self) -> int:
        return len(self._cards)

    def __getitem__(self, position) -> Card:
        return self._cards[position]

    def spades_high(self, card: Card) -> int:
        rank_value = self.ranks.index(card.rank)
        return rank_value * len(self.suit_values) + self.suit_values[card.suit]

    def sort(self, reverse: bool = False) -> None:
        if reverse:
            sorted_deck = reversed(sorted(self, key=self.spades_high))
        else:
            sorted_deck = sorted(self, key=self.spades_high)
        for card in sorted_deck:
            print(card)
