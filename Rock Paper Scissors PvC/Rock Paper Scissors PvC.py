'''
Basic as Rock Paper Scissors but in a different look,
Because now computer have to make the decision
(which I just use random) and player have to play against computer
'''
from random import randint

def playerComp():
    luck = randint(1,3)
    if luck == 1:
        return "r"
    elif luck == 2:
        return "p"
    else:
        return "s"
    
def playerOne():
    P1 = input("Rock (R)\nPaper (P)\nScissors (S)\nMake your choice: ").lower()
    while P1 not in ["r","p","s"]:
        P1 = input("Entered Wrong Value, Try Again: ").lower()
    return P1

def main(P1,P2):
    if P1 == "r" and P2 == "s" or P1 == "s" and P2 == "p" or P1 == "p" and P2 == "r":
        print("#\n#\n#\n#\n#\n#")
        print(f"Player = {P1} vs Computer = {P2}\nPlayer Wins.")
    elif P2 == "r" and P1 == "s" or P2 == "s" and P1 == "p" or P2 == "p" and P1 == "r":
        print("#\n#\n#\n#\n#\n#")
        print(f"Player = {P1} vs Computer = {P2}\nComputer Wins.")
    else:
        print("#\n#\n#\n#\n#\n#")
        print(f"{P1} vs {P2}\nDraw. Nice Try.")

main(playerOne(),playerComp())