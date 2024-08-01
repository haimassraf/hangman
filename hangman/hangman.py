import hangman9 as h9
import hangman8 as h8
import hangman7 as h7
import hangman6 as h6
import random

HANGMAN_ASCII_ART = """Welcome to hangmen!
           _    _
          | |  | |
          | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
          |  __  |/ _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\
          | |  | | (_| | | | | (_| | | | | | | (_| | | | |
          |_|  |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                               __/ |
                              |___/"""

print(HANGMAN_ASCII_ART)


MAX_TRIES = 8
print(f"Max tries: {MAX_TRIES}")
print()

failed_number = 0
# the failed numbers of the user

CATEGORY_LIST = ['fruits', 'cars', 'profession', 'countries']
user_choice = input(f"Enter a category ({', '.join(CATEGORY_LIST)}): ").lower()

while user_choice not in CATEGORY_LIST:
    print('Enter a correct category')
    user_choice = input(f"Enter a category ({', '.join(CATEGORY_LIST)}): ").lower()
# not stop until the user enter a correct category

file = f"{user_choice}.txt"
index = random.randint(0, list(h9.choose_word(file, 0))[0] - 1)
# the function choose word return a tuple that the first variable is the len of the text that the user choice

secret_word = list(h9.choose_word(file, index))[1]

print(" _ " * len(secret_word))
# print "_" times the len of the secret word

old_letter_guess = []
# create a list that all the proper guessed letter will be there

print()
letter_guess = input("Enter a letter guess: ")
# the guess of the user

while True:
    if h6.try_update_letter_guessed(letter_guess, old_letter_guess):
        # check the proper of the user letter`s and if it`s already guessed

        if letter_guess.lower() in secret_word:
            # check if the letter guess correct

            if h7.check_win(secret_word, old_letter_guess):
                # check if the user guess all the letters

                print(h7.show_hidden_word(secret_word, old_letter_guess))
                # print the secret word

                print()
                print(f"You Won!\nwith {failed_number} several failures")
                break
        else:
            if failed_number == MAX_TRIES - 1:
                # check if the user lose

                h8.print_hangman(MAX_TRIES)
                # print the hanged man

                print(f"Game over!\nThe word was: {secret_word}")
                break

            failed_number += 1
            # updates the user`s number of failures
            h8.print_hangman(failed_number)
    #         print the progress of the hanged man

    print(h7.show_hidden_word(secret_word, old_letter_guess))
    # print the secret word with the guessed letters

    print()
    letter_guess = input("Enter a letter guess: ")
