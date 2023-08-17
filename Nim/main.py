import random

piles = [0, 0, 0]
random_piles = int(input("Do you want to play with random piles? ")) # 0: No random piles; 1: Random piles
player = 2
winner = 0

if random_piles == 0:
    piles[0] = int(input("How big should pile 1 be? "))
    piles[1] = int(input("How big should pile 2 be? "))
    piles[2] = int(input("How big should pile 3 be? "))
else:
    min = int(input("What should the minimum amount of coins in each pile be? "))
    max = int(input("What should the maximum amount of coins in each pile be? "))
    
    piles = [random.randint(min, max), random.randint(min, max), random.randint(min, max)]

def turn(piles, choose, num):
    piles[choose] -= num

    return piles

while True:
    if player == 2:
        player = 1
    else:
        player = 2

    valid_turn = False
    
    print(piles)

    print("Player: " + str(player))
    choose = int(input("Choose the pile you want to take from: "))-1

    while not valid_turn:
        num = abs(int(input("Choose the number of coins you want to take: ")))

        if num > piles[choose]:
            print("Player " + str(player) + " is stuuupid!")
            print("Please take less coins!")
        elif -1 < num < 1:
            print("Player " + str(player) + " is stuuupid!")
            print("Please take more coins!")
        else:
            valid_turn = True

    piles = turn(piles, choose, num)

    if piles == [0, 0, 0]:
        winner = player
        break

print("The winner is: Player " + str(winner))