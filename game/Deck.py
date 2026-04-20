from Card import Card
import random


class Deck:

    def __init__(self):
        self.deck = [
            Card(suit=suit, rank=rank)
            for rank in Card.RANKS
            for suit in Card.SUITS
        ]

    def shuffle(self):
        random.shuffle(self.deck)

    def give_card(self):
        if not self.deck:
            raise ValueError("No cards left in the deck.")
        return self.deck.pop(0)

    def burn_card(self):
        if not self.deck:
            raise ValueError("No cards left to burn.")
        burned = self.deck.pop(0)
        print(f"Burned: {burned}")

    def print_deck(self):
        print(f"Deck size: {len(self.deck)}")
        print("-" * 20)
        for card in self.deck:
            print(f"  {card}")

    def __len__(self):
        return len(self.deck)


if __name__ == "__main__":
    d = Deck()
    d.shuffle()
    card = d.give_card()
    print(f"Given card: {card}")
    print(f"Remaining: {len(d)} cards")