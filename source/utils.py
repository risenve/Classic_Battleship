import csv

board_size = 10 
empty = "."
hit = "X"
miss = "O"

def is_in_bounds(r, c):
    if r<0 or r>= board_size:
        return False
    if c<0 or c>= board_size:
        return False
    return True

def get_neighbors(r, c):
    neighbord = []
    # 4 directions: up, down, left, right
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if abs(dr) + abs(dc) != 1: # skip diagonals and self cell
                continue
            nr = r + dr
            nc = c + dc

            if is_in_bounds(nr, nc):
                neighbord.append((nr, nc))
    return neighbord

def create_empty_board ():
    board = []
    for r in range(board_size):
        row = []
        for c in range(board_size):
            row.append(empty)
        board.append(row)
    return board

def print_board(board, title=""):
    if title:
        print(title)
    header = "  " + " ".join([str(c) for c in range(board_size)])
    print(header)
    for r in range(board_size):
        row_str = str(r) + " " + " ".join(board[r])
        print(row_str)

def save_ships_to_csv(filepath, ships):
    with open(filepath, mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ship_id", "row", "col"])

        for ship_id in ships:
            for cell in ships[ship_id]:
                writer.writerow([ship_id, cell[0], cell[1]])


def load_ships_from_csv(filepath):
    ships = {}
    
    with open(filepath, newLine="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            ship_id = int(row["ship_id"])
            r = int(row["row"])
            c = int(row["col"])

            if ship_id not in ships:
                ships[ship_id] = []
            
            ships[ship_id].append((r, c))
    return ships
