import csv
import random
from utils import (
    create_empty_board,
    print_board,
    load_ships_from_csv,
    get_neighbors,
    hit,
    miss,
    empty
)

def mark_surroundings(ship_cells, board):
    for cell in ship_cells:
       r = cell[0]
       c = cell[1]
       neighbors = get_neighbors(r, c)
       for n in neighbors:
           nr = n[0]
           nc = n[1]
           if board[nr][nc] == empty:
               board[nr][nc] = miss

def is_ship_destroyed(ship_cells, board):
    for cell in ship_cells:
        r = cell[0]
        c = cell[1]
        if board[r][c] != hit:
            return False
    return True

def all_ship_destroyed(ships, hits):
    for ship_id in ships:
        if not is_ship_destroyed(ships[ship_id], hits):
            return False
    return True
    
def player_turn(bot_ships, player_board, player_hits):
    while True:
        move = input("Enter your move (row-col): ")
        # parse_input
        try:
            r, c = map(int, move.split("-"))
        except:
            print("Invalid input format. Use row-col format.")
            continue

        if r < 0 or r > 9 or c < 0 or c > 9:
            print("Move out of bounds. Try again.")
            continue

        if player_board[r][c] != empty:
            print("You already attacked this cell. Try again.")
            continue

        for ship_id in bot_ships:
            if (r, c) in bot_ships[ship_id]:
                print("It's a hit!")
                player_board[r][c] = hit
                player_hits.add((r, c))

                if is_ship_destroyed(bot_ships[ship_id], player_hits):
                    print("You destroyed a ship!")
                    mark_surroundings(bot_ships[ship_id], player_board)
                break
    print("Failed to hit. It's a miss.")
    player_board[r][c] = miss
    return (r,c), "miss"

def bot_turn(player_ships, bot_board, bot_hits):
    while True:
        r = random.randint(0, 9)
        c = random.randint(0, 9)

        if bot_board[r][c] == empty:
            break

    print(f"Bot attacks cell: {r}-{c}")

    for ship_id in player_ships:
        if (r, c) in player_ships[ship_id]:
            print("Bot hit your ship!")
            bot_board[r][c] = hit
            bot_hits.add((r, c))

            if is_ship_destroyed(player_ships[ship_id], bot_hits):
                print("Bot destroyed one of your ships!")
                mark_surroundings(player_ships[ship_id], bot_board)
            break
    
    print("Bot missed.")
    bot_board[r][c] = miss
    return (r,c), "miss"

def game():
    player_ships = load_ships_from_csv("data/player_ships.csv")
    bot_ships = load_ships_from_csv("data/bot_ships.csv")

    player_board = create_empty_board()
    bot_board = create_empty_board()

    player_hits = set()
    bot_hits = set()

    turn = 1

    print("__________ Game Start! __________")

    with open("data/gameplay_log.csv", mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "turn",
            "player_move",
            "player_result",
            "bot_move",
            "bot_result"
        ])

        while True:
            print(f"\n____ Turn {turn} ____\n")
            print_board(player_board, "Your Board:")
            print_board(bot_board, "Bot's Board:")

            player_move, player_result = player_turn(bot_ships, bot_board, player_hits)
            if all_ship_destroyed(bot_ships, player_hits):
                print("Congratulations! You won! AI will never replace you")
                break

            bot_move, bot_result = bot_turn(player_ships, player_board, bot_hits)
            if all_ship_destroyed(player_ships, bot_hits):
                print("Bot wins! You'll lose your job because of AI.")
                break

            writer.writerow([
                turn,
                f"{player_move[0]}-{player_move[1]}",
                player_result,
                f"{bot_move[0]}-{bot_move[1]}",
                bot_result
            ])

            turn += 1