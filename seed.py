"""
seed.py — Populates the database with sample users, games, and game players.
Run with: python seed.py
"""

from prisma import Prisma

db = Prisma()


def seed():
    db.connect()

    # ── Clear existing data (order matters due to foreign keys) ───────────────
    print("Clearing existing data...")
    db.gameplayer.delete_many()
    db.game.delete_many()
    db.user.delete_many()

    # ── Seed Users ────────────────────────────────────────────────────────────
    print("Seeding users...")

    john = db.user.create(
        data={
            "username": "john_doe",
            "email": "john@poker.com",
            "password": "hashed_password_1",  # In production, always hash passwords!
        }
    )

    sasha = db.user.create(
        data={
            "username": "sasha_smith",
            "email": "sasha@poker.com",
            "password": "hashed_password_2",
        }
    )

    stockfish = db.user.create(
        data={
            "username": "stockfish_bot",
            "email": "stockfish@poker.com",
            "password": "hashed_password_3",
        }
    )

    print(f"  Created users: {john.username}, {sasha.username}, {stockfish.username}")

    # ── Seed Games ────────────────────────────────────────────────────────────
    print("Seeding games...")

    game1 = db.game.create(
        data={
            "pot": 500,
            "status": "finished",
            "winner": john.username,
        }
    )

    game2 = db.game.create(
        data={
            "pot": 300,
            "status": "finished",
            "winner": sasha.username,
        }
    )

    game3 = db.game.create(
        data={
            "pot": 0,
            "status": "active",
            "winner": None,
        }
    )

    print(f"  Created games: #{game1.id}, #{game2.id}, #{game3.id}")

    # ── Seed GamePlayers ──────────────────────────────────────────────────────
    print("Seeding game players...")

    # Game 1 — John vs Stockfish (John won)
    db.gameplayer.create(
        data={
            "userId": john.id,
            "gameId": game1.id,
            "bet": 250,
            "amount": 2250,  # Started with 2000, won 500
            "folded": False,
        }
    )
    db.gameplayer.create(
        data={
            "userId": stockfish.id,
            "gameId": game1.id,
            "bet": 250,
            "amount": 1750,  # Started with 2000, lost 250
            "folded": True,
        }
    )

    # Game 2 — Sasha vs Stockfish (Sasha won)
    db.gameplayer.create(
        data={
            "userId": sasha.id,
            "gameId": game2.id,
            "bet": 150,
            "amount": 2150,
            "folded": False,
        }
    )
    db.gameplayer.create(
        data={
            "userId": stockfish.id,
            "gameId": game2.id,
            "bet": 150,
            "amount": 1850,
            "folded": True,
        }
    )

    # Game 3 — John vs Sasha (still active)
    db.gameplayer.create(
        data={
            "userId": john.id,
            "gameId": game3.id,
            "bet": 0,
            "amount": 2000,
            "folded": False,
        }
    )
    db.gameplayer.create(
        data={
            "userId": sasha.id,
            "gameId": game3.id,
            "bet": 0,
            "amount": 2000,
            "folded": False,
        }
    )

    print("  Created game players for all games.")

    db.disconnect()
    print("\nSeeding complete!")


if __name__ == "__main__":
    seed()
