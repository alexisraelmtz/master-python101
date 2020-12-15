import collections  # import namedtuple
import random


French = collections.namedtuple("Card", ["Suit", "Rank"])


class FrenchDeck:
    Card = collections.namedtuple("Card", ["Suit", "Rank"])
    ranks = [str(n) for n in range(2, 11)] + list("JQRA")
    suits = ("clubs dimonds hearts spades").upper().split()

    def __init__(self):
        self._cards = [
            self.Card(suit, rank) for suit in self.suits for rank in self.ranks
        ]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return f"Card | Suit: {(self._cards[position][0])} | Rank: {self._cards[position][1]}"

    # def __iter__(self):
    #     for card in self._cards:
    #         print(f"Card | Suit: {(card[0]).upper()} | Rank: {card[1]}")

    # def __repr__(self):
    # return f"Card | Suit: {(self._cards[0]).upper()} | Rank: {self._cards[1]}"


# beer_card = French("diamonds", "7")
# print(f"French {beer_card}")

# print(FrenchDeck.ranks)
# print(FrenchDeck.suits)
# print(f"{deck[38]}\n")

deck = FrenchDeck()
print(f"Length of Deck is: {len(deck)} cards.")

# print(random.choice(deck))
# print(random.choice(deck))
# print(random.choice(deck))

for card in deck:
    print(card)