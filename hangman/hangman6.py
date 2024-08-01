def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    if the user guess true it append it to the old letter guess, if not it will print notification accordingly
    :param letter_guessed: str
    :param old_letters_guessed: list[str]
    :return: bool
    """
    if (len(letter_guessed) > 1 or not letter_guessed.isalpha() or not letter_guessed.isascii() or
            letter_guessed.lower() in old_letters_guessed):
        print('X')
        print(' -> '.join(sorted([*old_letters_guessed])))
        return False
    else:
        old_letters_guessed.append(letter_guessed.lower())
        return True
