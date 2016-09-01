import rpsFunctions
from rpsGUI import *
import random

r_count = 0
p_count = 0
s_count = 0
draw_count = 0
x = 0
comp_wins = -1
user_wins = 0

while x < 30:
    action, input_string = rpsFunctions.getUserAction()

    r_count, p_count, s_count = rpsFunctions.userActionRecord(action, r_count, p_count, s_count)

    r, p, s, total = rpsFunctions.computerNextMove(r_count, p_count, s_count)

    # print(r, p, s, total)
    # print(r+p+s)


    number = random.random()
    # print (number)

    if number <= r:
        comp_wins, user_wins, draw_count = rpsFunctions.winLoss("p", action, comp_wins, user_wins, draw_count)
        print("Computers move: p" + "\nComputer Wins: " + str(comp_wins) + "\nUser Wins: " +
              str(user_wins) + "\nDraws: " + str(draw_count))
    elif r < number <= (r + p):
        comp_wins, user_wins, draw_count = rpsFunctions.winLoss("s", action, comp_wins, user_wins, draw_count)
        print("Computers move: s" + "\nComputer Wins: " + str(comp_wins) + "\nUser Wins: " +
              str(user_wins) + "\nDraws: " + str(draw_count))
    else:
        comp_wins, user_wins, draw_count = rpsFunctions.winLoss("r", action, comp_wins, user_wins, draw_count)
        print("Computers move: r" + "\nComputer Wins: " + str(comp_wins) + "\nUser Wins: " +
              str(user_wins) + "\nDraws: " + str(draw_count))

    x += 1
