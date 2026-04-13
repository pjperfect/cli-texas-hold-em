class Card():
    def __init__(self, suite, rank):
        ...

        accepted_suits = ['HEARTS', 'DIAMONDS', 'CLUBS', 'SPADES']
        accepted_ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'JACK', 'QUEEN', 'KING', 'ACE']

        if not isinstance(suite, str):
            raise TypeError(f"Suite must be a string. Got {type(suite).__name__} instead.")
        if not isinstance(rank, str):
            raise TypeError(f"Rank must be a string. Got {type(rank).__name__} instead.")
        
        suite_upper = suite.upper()
        rank_upper = rank.upper()

        if suite_upper not in accepted_suits:
            raise ValueError(f"Invalid suite '{suite}'. Accepted suites are: {', '.join(accepted_suits)}.")
        if rank_upper not in accepted_ranks:
            raise ValueError(f"Invalid rank '{rank}'. Accepted ranks are: {', '.join(accepted_ranks)}.")

        self.suite = suite
        self.rank = rank

    def print_card(self):
        print(f"{self.rank} of {self.suite}")

if __name__ == "__main__":
    card1 = Card("Hearts", "Ace")
    card2 = Card("Spades", "10")
    card3 = Card("Diamonds", "Queen")
    # Testing an error case
    try:
        invalid_card = Card("Stars", "11")
        invalid_card.print_card()
    except ValueError as e:
        print(e)  # Output: Invalid suite 'Stars'. Accepted suites are: HEARTS

    card1.print_card()  # Output: Ace of Hearts
    card2.print_card()  # Output: 10 of Spades
    card3.print_card()  # Output: Queen of Diamonds