import csv
import random
from .utils import (
    create_empty_board,
    print_board,
    load_ships_from_csv,
    get_neighbors,
    HIT,
    MISS,
    EMPTY
)


def mark_surroundings(ship_cells, board):
    for r, c in ship_cells:
        for nr, nc in get_neighbors(r, c):
            if board[nr][nc] == EMPTY:
                board[nr][nc] = MISS


def is_ship_destroyed(ship_cells, board):
    for r, c in ship_cells:
        if board[r][c] != HIT:
            return False
    return True


def all_ships_destroyed(ships, board):
    for ship_id in ships:
        if not is_ship_destroyed(ships[ship_id], board):
            return False
    return True


def player_turn(bot_ships, board):
    while True:
        move = input("Your move (row-col): ")

        try:
            r, c = map(int, move.split("-"))
        except:
            print("Invalid input format. Use row-col.")
            continue

        if not (0 <= r < 10 and 0 <= c < 10):
            print("Move out of bounds.")
            continue

        if board[r][c] != EMPTY:
            print("You already attacked this cell.")
            continue

        for cells in bot_ships.values():
            if (r, c) in cells:
                print("Hit!")
                board[r][c] = HIT
                if is_ship_destroyed(cells, board):
                    print("Ship destroyed.")
                    mark_surroundings(cells, board)
                return (r, c), "HIT"

        print("Miss.")
        board[r][c] = MISS
        return (r, c), "MISS"


def bot_turn(player_ships, board):
    while True:
        r = random.randint(0, 9)
        c = random.randint(0, 9)
        if board[r][c] == EMPTY:
            break

    print(f"Bot attacks cell {r}-{c}.")

    for cells in player_ships.values():
        if (r, c) in cells:
            print("Bot hit your ship.")
            board[r][c] = HIT
            if is_ship_destroyed(cells, board):
                print("Bot destroyed one of your ships.")
                mark_surroundings(cells, board)
            return (r, c), "HIT"

    print("Bot missed.")
    board[r][c] = MISS
    return (r, c), "MISS"


def game():
    player_ships = load_ships_from_csv("data/player_ships.csv")
    bot_ships = load_ships_from_csv("data/bot_ships.csv")

    player_board = create_empty_board()
    bot_board = create_empty_board()

    print("========== Game started ==========")

    turn = 1
    with open("data/gameplay_log.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["turn", "player_move", "player_result", "bot_move", "bot_result"])

        while True:
            print(f"\n--- Turn {turn} ---\n")
            print_board(player_board, "Your board:")
            print_board(bot_board, "Bot board:")

            pm, pr = player_turn(bot_ships, bot_board)
            if all_ships_destroyed(bot_ships, bot_board):
                print("\nYou win. All enemy ships destroyed.")
                break

            bm, br = bot_turn(player_ships, player_board)
            if all_ships_destroyed(player_ships, player_board):
                print("\nYou lose. All your ships are destroyed.")
                break

            writer.writerow([turn, f"{pm[0]}-{pm[1]}", pr, f"{bm[0]}-{bm[1]}", br])
            turn += 1