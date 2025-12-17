from utils import is_inside, get_neighbors, save_ships_to_csv
ship_sizes = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]

def parse_input(line):
    cells = []
    parts = line.split(",")

    for part in parts:
        r, c = part.split("-")
        cells.append((int(r), int(c)))
    return cells

def validate_ship(cells, occupied, size):
    if len(cells) != size:
        return False, #wrong size of thr board
    for cell in cells:
        r = cell[0]
        c = cell[1]

        if not is_inside(r, c):
            return False, #out of bounds
        if cell in occupied:
            return False, #overlap
        neighbors = get_neighbors(r, c)
        for neighbor in neighbors:
            if neighbor in occupied:
                return False, #tships are touching each other - ploho
    return True, ""

def get_player_ships():
    ships = {}
    occupied = set()
    ship_id = 1

    print("__________ Player places ships on the board __________")
    print("Enter ship cells in the format: row1-col1,row2-col2,...")

    for size in ship_sizes:
        while True:
            line = input(f"Enter cells for ship of size {size}: ")
            cells = parse_input(line)
            valid, msg = validate_ship(cells, occupied, size) 
            if not valid:
                print("Invalid ship placement:", msg) 
                continue
            ships[ship_id] = cells
            for cell in cells:
                occupied.add(cell)
            ship_id += 1
            break
    save_ships_to_csv("data/player_ships.csv", ships)
    print("\nAll ships placed successfully!")   

    



