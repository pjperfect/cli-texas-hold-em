class Card:
    SUITS = ['HEARTS', 'DIAMONDS', 'CLUBS', 'SPADES']
    RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'JACK', 'QUEEN', 'KING', 'ACE']

    def __init__(self, suit, rank):
        if not isinstance(suit, str):
            raise TypeError(f"Suit must be a string. Got {type(suit).__name__} instead.")
        if not isinstance(rank, str):
            raise TypeError(f"Rank must be a string. Got {type(rank).__name__} instead.")

        suit_upper = suit.upper()
        rank_upper = rank.upper()

        if suit_upper not in self.SUITS:
            raise ValueError(f"Invalid suit '{suit}'. Accepted suits are: {', '.join(self.SUITS)}.")
        if rank_upper not in self.RANKS:
            raise ValueError(f"Invalid rank '{rank}'. Accepted ranks are: {', '.join(self.RANKS)}.")

        self.suit = suit_upper
        self.rank = rank_upper

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __repr__(self):
        return f"Card(suit='{self.suit}', rank='{self.rank}')"

    def print_card(self):
        print(self)


if __name__ == "__main__":
    card1 = Card("Hearts", "Ace")
    card2 = Card("Spades", "10")
    card3 = Card("Diamonds", "Queen")

    try:
        invalid_card = Card("Stars", "11")
    except ValueError as e:
        print(f"Error: {e}")

    card1.print_card()  # ACE of HEARTS
    card2.print_card()  # 10 of SPADES
    card3.print_card()  # QUEEN of DIAMONDS