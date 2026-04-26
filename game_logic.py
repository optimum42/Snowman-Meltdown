import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """
    Displays the current meltdown stage and the secret word state
    with the guessed letters uncovered
    """
    print(STAGES[mistakes])
    masked = [c if c in guessed_letters else '_' for c in secret_word]
    print("Word: " + " ".join(masked))


def play_game():
    secret_word = get_random_word()
    guessed_letters = ['a', 'e', 'i', 's', 'o', 'u']
    mistakes = 0

    print("Welcome to Snowman Meltdown!")
    display_game_state(mistakes, secret_word, guessed_letters)

    # TODO: Build your game loop here.
    # For now, simply prompt the user once:
    guess = input("Guess a letter: ").lower()
    print("You guessed:", guess)

