from source.ship_input import get_player_ships
from source.bot_generation import generate_bot_ships
from source.gameplay import game


def main():
    get_player_ships()
    generate_bot_ships()
    game()


if __name__ == "__main__":
    main()