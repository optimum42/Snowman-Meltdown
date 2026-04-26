import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


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


def play_game():
    """
    paying loop
    the loop end if either the secret word is guessed (win)
    or the snowman is melding down (lose)
    """
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")

    # game loop
    while mistakes < len(STAGES):
        if display_game_state(mistakes, secret_word, guessed_letters):
            break
        guess = input("\nGuess a letter: ").lower()
        if guess in guessed_letters:
            print("You already guessed that letter!")
        else:
            guessed_letters.append(guess)
        if guess not in secret_word:
            mistakes += 1

    if mistakes == len(STAGES):
        print("Sorry, snowman melted down...")
    else:
        print("Congrats! You guessed the word!")

