def show_hidden_word(secret_word: str, old_letters_guessed: list[str]) -> str:
    """
    show the hidden word with the letter that the user guess
    :param secret_word: str
    :param old_letters_guessed: list[str]
    :return: str
    """
    new_str = ""
    for char in secret_word:
        if char in old_letters_guessed:
            new_str += f" {char} "
        else:
            new_str += ' _ '
    return new_str


def check_win(secret_word: str, old_letters_guessed: list[str]) -> bool:
    """
    check if their no ' _ ' in the secret word and if the user won
    :param secret_word:
    :param old_letters_guessed:
    :return:
    """
    if '_' in show_hidden_word(secret_word, old_letters_guessed):
        return False
    return True
