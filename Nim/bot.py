import random

piles = []
random_piles = int(input("Do you want to play with random piles? ")) # 0: No random piles; 1: Random piles
num_of_piles = int(input("How many piles should the game have? "))
player = 2
winner = 0
nim_sum = 0

if random_piles == 0:
    for i in range(1, num_of_piles+1):
        piles.append(int(input(f"How big should pile {i} be? ")))
else:
    min = int(input("What should the minimum amount of coins in each pile be? "))
    max = int(input("What should the maximum amount of coins in each pile be? "))
    
    for i in range(0, num_of_piles):
        piles.append(random.randint(min, max))

def turn(piles, choose, num):
    piles[choose] -= num

    return piles

def XOR(num1, num2):
    num = ""

    while len(num1) < len(num2):
        num1 = "0" + num1
    while len(num1) > len(num2):
        num2 = "0" + num2

    for i in range(0, len(num1)):
        if int(num1[i]) + int(num2[i]) == 2:
            num = num + "0"
        else:
            num = num + str(int(num1[i]) + int(num2[i]))
        
    return num

def nimSum(piles):
    bin_piles = []
    for i in range(0, len(piles)):
        bin_piles.append(int(str(bin(piles[i])[2:])))
    nim_sum = str(bin_piles[0])
    for i in range(1, len(bin_piles)):
        nim_sum = XOR(nim_sum, str(bin_piles[i]))
    return int(nim_sum)

def bot_turn(piles, nim_sum):
    if nim_sum == 0:
        piles[-1] -= 1
    else:
        for l in range(0, len(piles)):
            for i in range(1, piles[l]+1):
                piles[l] -= i
                if nimSum(piles) == 0:
                    break
                piles[l] += i
    return piles

while True:
    if player == 2:
        player = 1
    else:
        player = 2

    valid_turn = False
    nim_sum = nimSum(piles)
    bin_piles = []
    for i in range(0, num_of_piles):
        bin_piles.append(int(str(bin(piles[i])[2:])))
    piles.sort()
    
    print(piles)

    print("Player: " + str(player))

    if player == 1:
        while not valid_turn:
            choose = int(input("Choose the pile you want to take from: "))-1
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
    else:
        piles = bot_turn(piles, nim_sum)

    if piles == ([0] * num_of_piles):
        winner = player
        break

print("The winner is: Player " + str(winner))