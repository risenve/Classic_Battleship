import random
from .utils import is_in_bounds, get_neighbors, save_ships_to_csv

ship_sizes = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]


def can_place(cells, occupied):
    for r, c in cells:
        if not is_in_bounds(r, c):
            return False
        if (r, c) in occupied:
            return False
        for n in get_neighbors(r, c):
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
            orientation = random.randint(0, 1)

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
    print("Bot ships generated successfully.")