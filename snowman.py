import game_logic


def main():
    """
    Main loop for recursively calling itself as long as the user hits 'y'
    """
    game_logic.play_game()
    repeat = input("Type 'y' for repeat the game: ").lower()
    if repeat == 'y':
        main()
    else:
        print("Bye.")


if __name__ == "__main__":
    main()