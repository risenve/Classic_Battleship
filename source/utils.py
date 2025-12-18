import csv

BOARD_SIZE = 10
EMPTY = "."
HIT = "X"
MISS = "O"


def is_in_bounds(r, c):
    return 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE


def get_neighbors(r, c):
    neighbors = []
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if abs(dr) + abs(dc) != 1:
                continue
            nr, nc = r + dr, c + dc
            if is_in_bounds(nr, nc):
                neighbors.append((nr, nc))
    return neighbors


def create_empty_board():
    return [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]


def print_board(board, title=""):
    if title:
        print(title)
    print("  " + " ".join(str(i) for i in range(BOARD_SIZE)))
    for i, row in enumerate(board):
        print(i, " ".join(row))


def save_ships_to_csv(filepath, ships):
    with open(filepath, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ship_id", "row", "col"])
        for ship_id, cells in ships.items():
            for r, c in cells:
                writer.writerow([ship_id, r, c])


def load_ships_from_csv(filepath):
    ships = {}
    with open(filepath, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            ship_id = int(row["ship_id"])
            cell = (int(row["row"]), int(row["col"]))
            ships.setdefault(ship_id, []).append(cell)
    return ships