'''
Rock Paper Scissors
---
Have 3 different choice per player, these are:
Rock wins against Scissors
Paper wins against Rock
Scissors wins against Paper
---
We need P1, P2 input and comparision choice between of P1 & P2
'''
# Player 1 Choice Stage Function
def playerOne():
    P1 = input("Rock (R)\nPaper (P)\nScissors (S)\nMake your choice Player 1: ").lower()
    while P1 not in ["r","p","s"]:
        P1 = input("Entered Wrong Value, Try Again: ").lower()
    return P1

# Player 2 Choice Stage Function
def playerTwo():
    P2 = input("Rock (R)\nPaper (P)\nScissors (S)\nMake your choice Player 2: ").lower()
    while P2 not in ["r","p","s"]:
        P2 = input("Entered Wrong Value, Try Again: ").lower()
    return P2

# Comparision between choice of players. By using logic gates and "if-elif-else" block.
def main(P1,P2):
    if P1 == "r" and P2 == "s" or P1 == "s" and P2 == "p" or P1 == "p" and P2 == "r":
        print("Player 1 Wins.")
    elif P2 == "r" and P1 == "s" or P2 == "s" and P1 == "p" or P2 == "p" and P1 == "r":
        print("Player 2 Wins.")
    else:
        print("Draw. Nice Round.")

# Running programs main and functions.
main(playerOne(),playerTwo())