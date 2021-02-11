wins = int(input("enter your winnings"))
draws = int(input("enter your draws"))
losses = int(input("enter your losses"))


def football_points(win, draw, loss):
        if win >= 0 and draw >= 0 and loss >= 0:
            return (win * 3) + (draw * 1) + (loss * 0)
        else:
            return "please enter positive number of wins, draws and losses"


print(football_points(wins, draws, losses))
