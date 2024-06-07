import random

def get_choices():
    player_choice = input("Enter your choice (rock, paper, scissors): ")
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    choices = {'player': player_choice, 'computer': computer_choice}
    return choices

choices = get_choices()

def get_winner(choices):
    player = choices['player']
    computer = choices['computer']
    if player == computer:
        return 'tie'
    elif player == 'rock' and computer == 'scissors':
        return 'player'
    elif player == 'scissors' and computer == 'paper':
        return 'player'
    elif player == 'paper' and computer == 'rock':
        return 'player'
    else:
        return 'computer'

winner = get_winner(choices)
print(f"Player chose {choices['player']}")
print(f"Computer chose {choices['computer']}")
print(f"The winner is {winner}")

