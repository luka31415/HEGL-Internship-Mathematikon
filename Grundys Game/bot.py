A = [1, 1, 0, 1]
for i in range(0, 32):
    A.append(0)
    A.append(0)
    A.append(1)

piles = []
f = int(input("Are you the first person to move? (1 or 0 for True or False) "))
n = int(input("How big is the first pile? "))
piles.append(n)
if f == 0:
    m = int(input("How big is the second pile? "))
    piles.append(m)
finished_game = False
pos = [A[piles[0]-1]]
turns = 0

while not finished_game:
    turns += 1
    pos = [0] * len(piles)
    for i in range(0, len(piles)):
        pos[i] = A[piles[i]-1]

    if 0 in pos:
        if piles[pos.index(0)] % 3 == 0:
            piles[pos.index(0)] -= 2
            piles.append(2)
            print(f"You should take two coins from pile {pos.index(0)+1}")
        elif piles[pos.index(0)] % 3 == 2:
            piles[pos.index(0)] -= 1
            piles.append(1)
            print(f"You should take one coin from pile {pos.index(0)+1}")
    else:
        piles[0] -= 1
        piles.append(1)
        print("You should take one coin from the first pile.")

    piles.sort()
    piles.reverse()

    print("")
    print(piles)
    print("")

    finished_game = True
    for i in range(0, len(piles)):
        if not piles[i] == 1 and not piles[i] == 2:
            finished_game = False
    if finished_game:
        break

    pile = int(input("Which pile did your opponent change? "))
    num = int(input("How many coins did your opponent take from the pile? "))
    while num == piles[pile-1]/2 or num == 0:
        pile = int(input("Which pile did your opponent change? "))
        num = int(input("How many coins did your opponent take from the pile? "))
    piles[pile-1] -= num
    piles.append(num)

    piles.sort()
    piles.reverse()

    print("")
    print(piles)
    turns += 1

    finished_game = True
    for i in range(0, len(piles)):
        if not piles[i] == 1 and not piles[i] == 2:
            finished_game = False
        
if turns % 2 == 1:
    print("Player 1 has won the game!")
else:
    print("Player 2 has won the game!")