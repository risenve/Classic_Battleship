import random
from utils import is_inside, get_neighbors, save_ships_to_csv
ship_sizes = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]

def can_place(cells, occupied):
    for cell in cells:
        r = cell[0]
        c = cell[1]

        if not is_inside(r, c):
            return False

        if cell in occupied:
            return False

        neighbors = get_neighbors(r, c)
        for n in neighbors:
            if n in occupied:
                return False

    return True

def generate_bot_ships():
    ships = {}
    occupied = set()
    ship_id = 1

    for size in ship_sizes:
        placed = False

        while not placed:
            r = random.randint(0, 9)
            c = random.randint(0, 9)
            orientation = random.randint(0, 1)  # 0 - horizontal, 1 - vertical

            cells = []

            for i in range(size):
                if orientation == 0:
                    cells.append((r, c + i))
                else:
                    cells.append((r + i, c))

            if can_place(cells, occupied):
                ships[ship_id] = cells
                for cell in cells:
                    occupied.add(cell)
                ship_id += 1
                placed = True

    save_ships_to_csv("data/bot_ships.csv", ships)
    print("Bot ships generated successfully!")