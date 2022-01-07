from collections import namedtuple
from typing import List

Card = namedtuple("Card", ("rank", "suit"))


class FrenchDeck:
    ranks: List[str] = [str(n) for n in range(2, 11)] + list("JQKA")
    suits: List[str] = "spades diamonds clubs hearts".split()
    suit_values = {"spades": 0, "hearts": 3, "diamonds": 2, "clubs": 1}

    def __init__(self) -> None:
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self) -> int:
        return len(self._cards)

    def __getitem__(self, position) -> Card:
        return self._cards[position]

    def spades_high(self, card: Card) -> int:
        rank_value = self.ranks.index(card.rank)
        return rank_value * len(self.suit_values) + self.suit_values[card.suit]

    def sort(self, reverse: bool = False) -> "FrenchDeck":
        if reverse:
            self._cards = reversed(sorted(self, key=self.spades_high))
        else:
            self._cards = sorted(self, key=self.spades_high)
        return self
