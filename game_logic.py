import random
from curses.ascii import isalpha

from ascii_art import STAGES

# List of secret words
WORDS = [
    "apple", "banana", "rocket", "planet", "window", "forest", "bridge",
    "castle", "dragon", "pirate", "wizard", "island", "desert", "camera",
    "pencil", "notebook", "monster", "rabbit", "turtle", "diamond",
    "thunder", "rainbow", "sunshine", "ocean", "volcano", "library",
    "guitar", "helmet", "jungle", "lantern", "magnet", "napkin",
    "orchard", "pillow", "quartz", "robot", "sailor", "temple",
    "unicorn", "village", "whistle", "yogurt", "zebra", "button",
    "candle", "donkey", "engine", "falcon", "garden", "hammer",
    "icicle", "jacket", "kitten", "ladder", "mirror", "needle",
    "orange", "parrot", "quiver", "ranger", "school", "ticket",
    "umpire", "vacuum", "wallet", "xylophone", "yacht", "zipper",
    "anchor", "beacon", "carpet", "dolphin", "emerald", "feather",
    "glacier", "harbor", "insect", "jewel", "koala", "legend",
    "meteor", "nectar", "otter", "pocket", "quicksand", "radar",
    "shadow", "tunnel", "utensil", "voyage", "wanderer", "yogurt",
    "zeppelin", "basket", "compass", "fountain", "galaxy", "horizon",
    "igloo"
]


def cprint(text, color_str=None, end="\n"):
    """
    this function works like 'print' but with color
    """
    color_reset_code = '\033[0m'
    text_colors = {
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m'
    }
    color_code = text_colors.get(color_str, "")
    print(color_code + text + color_reset_code, end=end)


def get_random_word():
    """ Selects a random word from the list of words """
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """
    Displays the current meltdown stage and the secret word state
    with the guessed letters uncovered
    :return: True if the word is completely guessed, False otherwise
    """
    print(STAGES[mistakes])
    masked = [c if c in guessed_letters else '_' for c in secret_word]
    print("Word: " + " ".join(masked))
    return '_' not in masked


def guess_letter():
    """Gets a letter guess from the user and returns it"""
    while True:
        cprint("\nGuess letter: ", "magenta", end="")
        guess = input().strip()
        if len(guess) != 1 or not isalpha(guess):
            cprint("Please enter a letter", "red")
            continue
        return guess.lower()


def play_game():
    """
    paying loop
    the loop end if either the secret word is guessed (win)
    or the snowman is melding down (lose)
    """
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    cprint("Welcome to Snowman Meltdown!", "magenta")

    # game loop
    while mistakes < len(STAGES):
        if display_game_state(mistakes, secret_word, guessed_letters):
            break
        guess = guess_letter()
        if guess in guessed_letters:
            cprint("You already guessed that letter!", "blue")
        else:
            guessed_letters.append(guess)
            if guess not in secret_word:
                mistakes += 1

    # end of the game - show result
    if mistakes == len(STAGES):
        cprint("Sorry, snowman melted down...")
        print(f"The word was: ", end="")
        cprint(f"{secret_word}\n", "cyan")
    else:
        cprint("Congrats! You guessed the word "
               f"with just {mistakes} wrong guesses!\n"
               "Snowman survived ;-)\n", "green")
