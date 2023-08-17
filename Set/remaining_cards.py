import random
import matplotlib.pyplot as plt

results = []
test = [0, 0, 0, 0, 0, 0, 0, 0]
num_of_tries = 10000

def set(cards):
    test = [0, 0, 0, 0]

    for i in range(4):
        for card in cards:
            test[i] += card[i]

    test = [test[0]%3, test[1]%3, test[2]%3, test[3]%3]

    if test == [0, 0, 0, 0]:
        return True
    return False

for l in range(0, num_of_tries):
    if l % (num_of_tries // 100) == 0:
        print(str(int((l/num_of_tries)*100)) + "%")

    all_cards = []
    cards = []
    num_of_cards = 12
    end_game = False

    for i in range(0, 3):
        for m in range(0, 3):
            for n in range(0, 3):
                for k in range(0, 3):
                    all_cards.append([i, m, n, k])

    random.shuffle(all_cards)

    for i in range(0, num_of_cards):
        cards.append(all_cards[-1])
        all_cards.pop()

    while not end_game:
        num_of_cards = len(cards)
        combinations = []
        found_set = False

        for i in range(0, num_of_cards):
            for k in range(0 ,num_of_cards):
                for n in range(0, num_of_cards):
                    if i != k and i != n and k != n:
                        combinations.append([i, k, n])

        for combination in combinations:
            pick = [cards[combination[0]], cards[combination[1]], cards[combination[2]]]

            if set(pick):
                for card in pick:
                    cards.remove(card)
                found_set = True
                break

        for i in range(0, 3):
            try:
                cards.append(all_cards[-1])
                all_cards.pop()
            except:
                if not found_set:
                    end_game = True
                pass

    results.append(len(cards))

for result in results:
    test[int(result/3)] += 1

for i in range(0, len(test)-1):
    test[i] = test[i]/num_of_tries

print("")
print("")

for i in range(0, len(test)):
    print(str(3*i) + ": " + str(test[i]*100) + "%")

plt.bar([0, 3, 6, 9, 12, 15, 18, 21], test)
plt.show()
