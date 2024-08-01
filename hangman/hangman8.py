def print_hangman(num_of_tries: int):
    """
    print the user situation
    :param num_of_tries: int
    :return: none
    """
    hangman_photos = {
        1: '''
        x
        |
        |
        |
        |
        |
        ''',
        2: '''
        x-------x
        |
        |
        |
        |
        |
        ''',
        3: '''
        x-------x
        |       |
        |       0
        |
        |
        |
        ''',
        4: '''
        x-------x
        |       |
        |       0
        |       |
        |
        |
        |
        ''',
        5: '''
        x-------x
        |       |
        |       0
        |      /|
        |      
        |
        ''',
        6: '''
        x-------x
        |       |
        |       0
        |      /|\\
        |      
        |
        ''',
        7: '''
        x-------x
        |       |
        |       0
        |      /|\\
        |      /
        |
        
        Last chance
        ''',
        8: '''
        x-------x
        |       |
        |       0
        |      /|\\
        |      / \\
        |
        '''
    }

    print(hangman_photos[num_of_tries])
