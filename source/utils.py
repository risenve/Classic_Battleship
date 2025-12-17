import csv

board_size = 10 
empty = "."
hit = "X"
miss = "O"


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
