import random


def rock_paper_scissors_game():
    game = input('welcome to a rock_scissors_game \n input any letter from... (R, S, P)   R as rock, S as scissors, '
                 'P as paper: ')
    options = ['R', 'P', 'S']

    if game == random.choice(options):
        print('Tie')
        rock_paper_scissors_game()
    if game not in options:
        print('Sorry You chose the wrong option try again')
        rock_paper_scissors_game()
    else:
        if game in options:
            try:
                if game == 'R' and random.choice(options) == 'P':
                    print('Computer: Paper  \n You Lost')
                elif game == 'R' and random.choice(options) == 'S':
                    print('Computer: Scissors  \n You Winnnnn....')
                elif game == 'P' and random.choice(options) == 'S':
                    print('Computer: Scissors  \n You lost....')
                elif game == 'P' and random.choice(options) == 'R':
                    print('Computer: Rock  \n You Winnnnn....')
                elif game == 'S' and random.choice(options) == 'P':
                    print('Computer: Paper  \n You Winnnnn....')
                elif game == 'S' and random.choice(options) == 'R':
                    print('Computer: Scissors  \n You lost....')
            except game not in options:
                print('Sorry You chose the wrong option try again')


rock_paper_scissors_game()