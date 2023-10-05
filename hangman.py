from random import choice

words = ["banana", "computer", "elephant", "guitar", "library", "sunshine", "mountain", "butterfly", "chocolate",
         "telephone"]
correct_characters = []
incorrect_characters = []
attempts = 6
successes = 0
game_finished = False


def select_word(words_list):
    selected_word = choice(words_list)
    unic_characters = len(set(selected_word))
    return selected_word, unic_characters


def request_letter():
    chosen_letter = ''
    is_valid = False
    alphabet = 'abcdefghijklmnñopqrstuvwxyz'

    while not is_valid:
        chosen_letter = input("Choose a letter: ").lower()
        if chosen_letter in alphabet and (len(chosen_letter) == 1):
            is_valid = True
        else:
            print("You have not selected a correct letter")

    return chosen_letter


def show_new_board(selected_word):
    hidden_list = []
    for c in selected_word:
        if c in correct_characters:
            hidden_list.append(c)
        else:
            hidden_list.append('-')

    print(' '.join(hidden_list))


def check_letter(chosen_letter, hidden_word, lives, coincidences):
    end = False
    if chosen_letter in hidden_word:
        correct_characters.append(chosen_letter)
        coincidences += 1
    else:
        incorrect_characters.append(chosen_letter)
        lives -= 1

    if lives == 0:
        end = lost()
    elif coincidences == unic_characters:
        end = win(hidden_word)

    return lives, end, coincidences


def lost():
    print("You have lost all your lives")
    print("The hidden word was: " + word)
    return True


def win(discovered_word):
    show_new_board(discovered_word)
    print("Congratulations! You have discovered the secret word!")
    return True


 # Start Game


word, unic_characters = select_word(words)

while not game_finished:
    print("\n" + '*' * 20 + "\n")
    show_new_board(word)
    print("\n")
    print("Incorrect letters: " + '-'.join(incorrect_characters))
    print(f"Lives: {attempts}")
    print("\n" + '*' * 20 + "\n")
    letter = request_letter()
    attempts, finished, successes = check_letter(letter, word, attempts, successes)
    game_finished = finished

