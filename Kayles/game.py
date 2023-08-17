n = int(input("How many pins should be in the game? "))
P = [1] * n
player = 2
valid_guess = False

while P != [0] * n:
    valid_guess = False
    if player == 1:
        player = 2
    else:
        player = 1

    print("Player " + str(player) + ":")
    print(P)
    while not valid_guess:
        print("")
        num = int(input("How many pins do you want to take? (1 or 2) "))
        spot = int(input("Where do you want to take pins from? "))-1
        
        if num == 1:
            try:
                if P[spot] == 1:
                    valid_guess = True
            except:
                valid_guess = False
                pass
        else:
            try:
                if P[spot] == P[spot+1] == 1:
                    valid_guess = True
            except:
                valid_guess = False
                pass
        if not valid_guess:
            print("That turn wouldn't work, please try again!")

    if num == 1:
        P[spot] = 0
    else:
        P[spot] = 0
        P[spot+1] = 0
    
    print("")

print("Player " + str(player) + " is the winner!")