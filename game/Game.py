from Deck import Deck
from Player import Player


class Game:

    def __init__(self):
        self.pot = 0
        self.community_cards = []

        deck = Deck()
        deck.shuffle()

        human_cards = [deck.give_card(), deck.give_card()]
        pc_cards = [deck.give_card(), deck.give_card()]

        self.human = Player(type="human", cards=human_cards, bet=0, name="John", amount=2000)
        self.pc = Player(type="pc", cards=pc_cards, bet=0, name="Stockfish", amount=2000)

        self._turn = self.human
        self.deck = deck

    @property
    def turn(self):
        return self._turn

    @turn.setter
    def turn(self, player):
        if not isinstance(player, Player):
            raise ValueError("Turn must be assigned to a Player object.")
        self._turn = player

    def deal_flop(self):
        """Deal 3 community cards (the flop)."""
        self.deck.burn_card()
        self.community_cards = [self.deck.give_card() for _ in range(3)]

    def deal_turn(self):
        """Deal the 4th community card (the turn)."""
        self.deck.burn_card()
        self.community_cards.append(self.deck.give_card())

    def deal_river(self):
        """Deal the 5th community card (the river)."""
        self.deck.burn_card()
        self.community_cards.append(self.deck.give_card())

    def show_community_cards(self):
        if not self.community_cards:
            print("No community cards dealt yet.")
            return
        print("\nCommunity Cards:")
        for card in self.community_cards:
            print(f"  {card}")

    def show_pot(self):
        print(f"\n  Pot: ${self.pot}")


if __name__ == "__main__":
    game = Game()
    print("=== Game Initialized ===")
    game.human.show_cards()
    game.pc.show_cards()
    game.deal_flop()
    game.show_community_cards()