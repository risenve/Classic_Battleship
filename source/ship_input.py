from .utils import is_in_bounds, get_neighbors, save_ships_to_csv, BOARD_SIZE

ship_config = {
    4: 1,
    3: 2,
    2: 3,
    1: 4
}


def print_board(board):
    print("  " + " ".join(str(i) for i in range(BOARD_SIZE)))
    for i, row in enumerate(board):
        print(i, " ".join(row))


def build_ship_cells(r, c, size, direction):
    cells = []
    for i in range(size):
        if direction == "h":
            cells.append((r, c + i))
        else:
            cells.append((r + i, c))
    return cells


def validate_ship(cells, occupied):
    for r, c in cells:
        if not is_in_bounds(r, c):
            return False, "ship goes out of bounds"
        if (r, c) in occupied:
            return False, "ship overlaps another ship"
        for n in get_neighbors(r, c):
            if n in occupied:
                return False, "ships cannot touch each other"
    return True, "OK"


def get_player_ships():
    ships = {}
    occupied = set()
    ship_id = 1

    board = [["·" for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

    print("========== Ship placement ==========")
    print("Enter ship position as: row col direction")
    print("Direction: h (horizontal) or v (vertical)")
    print("Example: 3 2 h\n")

    for size, count in ship_config.items():
        for _ in range(count):
            while True:
                print_board(board)
                user_input = input(f"Place ship of size {size}: ").split()

                if len(user_input) != 3:
                    print("Invalid input format.")
                    continue

                try:
                    r, c = int(user_input[0]), int(user_input[1])
                    direction = user_input[2].lower()
                except:
                    print("Invalid input values.")
                    continue

                if direction not in ("h", "v"):
                    print("Direction must be 'h' or 'v'.")
                    continue

                cells = build_ship_cells(r, c, size, direction)
                valid, msg = validate_ship(cells, occupied)

                if not valid:
                    print(f"Error: {msg}.")
                    continue

                for cell in cells:
                    board[cell[0]][cell[1]] = "#"
                    occupied.add(cell)

                ships[ship_id] = cells
                ship_id += 1
                break

    save_ships_to_csv("data/player_ships.csv", ships)
    print("\nAll ships placed successfully.")