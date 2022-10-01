import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper and 's' for scissors\n")
    computer = random.choice(["r", "p", "s"])

    if user == computer:
        return 'Its a tie'

    if is_win:
        return 'You won'
    else:
        return 'You lost'

def is_win(player, opponent):
    if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

print(play())