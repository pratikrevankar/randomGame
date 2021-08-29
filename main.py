import random


def kill():
    print("Pleasure playing with you!")
    exit()


def gameWin(comp, you):
    if comp == you:
        return None

    # Check for all possibilities when computer choose 's'
    elif comp == 's':
        if you == 'w':
            return False
        if you == 'g':
            return True
    # Check for all possibilities when computer choose 'w'
    elif comp == 'w':
        if you == 'g':
            return False
        if you == 's':
            return True
    # Check for all possibilities when computer choose 'g'
    elif comp == 'g':
        if you == 's':
            return False
        if you == 'w':
            return True


print("Comp turn: Snake(s) Water(w) or Gun(g)?")
randomNo = random.randint(1, 3)
# print(randomNo)
if randomNo == 1:
    comp = 's'
elif randomNo == 2:
    comp = 'w'
elif randomNo == 3:
    comp = 'g'

while True:
    you = input("Your turn: Snake(s) Water(w) Gun(g) or Exit(e)? ")
    if you.lower() == 'e':
        kill()

    while you.lower() not in {"s", "w", "g", "e"}:
        you = input(
            "Your turn, choose correct option among: Snake(s) Water(w) Gun(g) or Exit(e)? ")
        if you.lower() == 'e':
            kill()

    print(f"You choose '{you}' & Computer chose '{comp}'")

    a = gameWin(comp, you)

    if a == None:
        print("The game is a tie!")
    elif a:
        print("You Win!")
    else:
        print("You lose!")
