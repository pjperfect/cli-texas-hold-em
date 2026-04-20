import random
import time


class Player:

    def __init__(self, type="pc", cards=None, bet=0, name="", amount=0):
        self.name = name
        self.type = type
        self.cards = cards if cards is not None else []
        self._bet = bet
        self.amount = amount
        self.folded = False

    @property
    def bet(self):
        return self._bet

    @bet.setter
    def bet(self, amount):
        if amount < 0:
            raise ValueError("Bet amount cannot be negative.")
        if amount > self.amount:
            raise ValueError(f"Not enough funds. Available: ${self.amount}, tried to bet: ${amount}.")
        self._bet += amount
        self.amount -= amount

    def reset_bet(self):
        """Reset bet at the start of a new round."""
        self._bet = 0

    def show_cards(self):
        print(f"\n{self.name}'s cards:")
        for card in self.cards:
            print(f"  {card}")

    # ─── Human Actions ────────────────────────────────────────────────────────

    def place_initial_bet(self):
        """Prompt the human player to place their opening bet."""
        while True:
            raw = input(f"\n[{self.name}] Place your opening bet (available: ${self.amount}): ")
            if raw.isdigit():
                n = int(raw)
                if 1 <= n <= self.amount:
                    self.bet = n
                    return n
                print(f"  Amount must be between $1 and ${self.amount}. Try again.")
            else:
                print("  Please enter a valid number.")

    def call_fold_raise(self, player):
        """Prompt the human player to call, fold, or raise."""
        while True:
            print(f"\n[{self.name}] Your bet: ${self.bet} | {player.name}'s bet: ${player.bet} | Available: ${self.amount}")
            choice = input("  1 = Call  |  2 = Fold  |  3 = Raise\n  Choice: ").strip()
            if choice == '1':
                return self.call(player)
            elif choice == '2':
                return self.fold()
            elif choice == '3':
                return self.raise_stake(player)
            else:
                print("  Invalid choice. Enter 1, 2, or 3.")

    def call(self, player):
        """Match the opponent's current bet."""
        diff = player.bet - self.bet
        if diff <= 0:
            print(f"  [{self.name}] Already matched. No action needed.")
            return True
        if self.amount < diff:
            print(f"  [{self.name}] Not enough funds to call (need ${diff}, have ${self.amount}). Folding.")
            return self.fold()
        self.bet = diff
        print(f"  [{self.name}] I call. Total bet: ${self.bet}")
        return True

    def fold(self):
        """Fold — player exits the round."""
        self.folded = True
        print(f"  [{self.name}] I fold.")
        return "fold"

    def raise_stake(self, player):
        """Raise the current bet by a chosen amount."""
        while True:
            raw = input(f"  [{self.name}] Enter raise amount (available: ${self.amount}): ")
            if raw.isdigit():
                raise_amount = int(raw)
                if 1 <= raise_amount <= self.amount:
                    self.bet = raise_amount
                    print(f"  [{self.name}] I raise by ${raise_amount}. Total bet: ${self.bet}")
                    return raise_amount
                print(f"  Must be between $1 and ${self.amount}.")
            else:
                print("  Please enter a valid number.")

    # ─── PC Actions ───────────────────────────────────────────────────────────

    def auto_place_initial_bet(self, human_amount):
        """PC automatically matches or raises the human's opening bet."""
        print(f"\n[{self.name}] Thinking...")
        time.sleep(1)

        decision = random.randint(1, 3)
        raise_amount = human_amount + random.randint(10, 250)

        # Force fold if broke
        if self.amount < human_amount:
            print(f"  [{self.name}] Not enough funds. Folding.")
            return self.fold()

        # Force call if can't afford raise
        if decision == 3 and raise_amount > self.amount:
            decision = 1

        if decision == 1 or decision == 2:
            # Call
            self.bet = human_amount
            print(f"  [{self.name}] I match your bet of ${human_amount}.")
            return human_amount
        else:
            # Raise
            self.bet = raise_amount
            print(f"  [{self.name}] I feel lucky. I raise by ${raise_amount}!")
            return raise_amount

    def auto_call_fold_raise(self, player):
        """PC automatically responds to the human's action."""
        print(f"\n[{self.name}] Thinking...")
        time.sleep(1)

        diff = player.bet - self.bet

        if diff <= 0:
            print(f"  [{self.name}] Already matched.")
            return True

        if self.amount < diff:
            print(f"  [{self.name}] Can't afford to call. Folding.")
            return self.fold()

        decision = random.randint(1, 3)
        raise_amount = diff + random.randint(10, 200)

        if decision == 1 or (decision == 3 and raise_amount > self.amount):
            # Call
            self.bet = diff
            print(f"  [{self.name}] I call. Total bet: ${self.bet}")
            return True
        elif decision == 2:
            return self.fold()
        else:
            # Raise
            self.bet = raise_amount
            print(f"  [{self.name}] I raise by ${raise_amount}! Total bet: ${self.bet}")
            return raise_amount