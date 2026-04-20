from Game import Game


def betting_round(human, pc, game, round_name):
    """Run a single betting round between human and PC."""
    print(f"\n{'=' * 40}")
    print(f"  {round_name}")
    print(f"{'=' * 40}")
    game.show_community_cards()
    game.show_pot()

    # Human acts first
    result = human.call_fold_raise(player=pc)
    if result == "fold":
        print(f"\n  {human.name} folded. {pc.name} wins the pot of ${game.pot}!")
        return "human_fold"

    game.pot = human.bet + pc.bet

    # PC responds
    result = pc.auto_call_fold_raise(player=human)
    if result == "fold":
        print(f"\n  {pc.name} folded. {human.name} wins the pot of ${game.pot}!")
        return "pc_fold"

    game.pot = human.bet + pc.bet
    game.show_pot()
    return "continue"


def play_game():
    print("\n" + "=" * 40)
    print("       WELCOME TO POKER")
    print("=" * 40)

    game = Game()
    human = game.human
    pc = game.pc

    # Show human their cards
    human.show_cards()

    # ── Round 1: Opening Bets ─────────────────────────────────────────────────
    print(f"\n{'=' * 40}")
    print("  Opening Bets")
    print(f"{'=' * 40}")

    human_bet = human.place_initial_bet()
    pc_bet = pc.auto_place_initial_bet(human_bet)

    if pc_bet == "fold":
        print(f"\n  {human.name} wins the opening pot!")
        return

    game.pot = human.bet + pc.bet
    game.show_pot()

    # ── Flop ──────────────────────────────────────────────────────────────────
    game.deal_flop()
    result = betting_round(human, pc, game, "The Flop")
    if result in ("human_fold", "pc_fold"):
        return

    # ── Turn ──────────────────────────────────────────────────────────────────
    game.deal_turn()
    result = betting_round(human, pc, game, "The Turn")
    if result in ("human_fold", "pc_fold"):
        return

    # ── River ─────────────────────────────────────────────────────────────────
    game.deal_river()
    result = betting_round(human, pc, game, "The River")
    if result in ("human_fold", "pc_fold"):
        return

    # ── Showdown ──────────────────────────────────────────────────────────────
    print(f"\n{'=' * 40}")
    print("  SHOWDOWN")
    print(f"{'=' * 40}")
    game.show_community_cards()
    human.show_cards()
    pc.show_cards()
    game.show_pot()
    print("\n  (Winner determination coming in next version!)")


if __name__ == "__main__":
    play_game()