cards = []
num_of_cards = len(cards)
combinations = []
counter = 0
sets = []

def set(cards):
    test = [0, 0, 0, 0]

    for i in range(0, 4):
        for card in cards:
            test[i] += card[i]

    test = [test[0]%3, test[1]%3, test[2]%3, test[3]%3]

    if test == [0, 0, 0, 0]:
        return True
    return False

for o in range(0, num_of_cards):
    for i in range(0, num_of_cards):
        for u in range(0, num_of_cards):
            if o != i and i != u and o != u:
                test = [o, i, u]
                test.sort()
                if not test in combinations:
                    combinations.append(test)

for combination in combinations:
    pick = [cards[combination[0]], cards[combination[1]], cards[combination[2]]]

    if set(pick):
        counter += 1
        sets.append(pick)

print(sets)
print(counter)