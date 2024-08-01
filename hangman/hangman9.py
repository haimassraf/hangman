def choose_word(file_path: str, index: int) -> tuple:
    """
    pick the secret word
    :param file_path: str
    :param index: int
    :return: tuple
    """
    with open(file_path, 'r') as file:
        txt = file.read()
        secret_words_list = txt.split()
        if index > len(secret_words_list):
            index = index % len(secret_words_list)
        secret_word = secret_words_list[index - 1]
        return len(secret_words_list), secret_word

