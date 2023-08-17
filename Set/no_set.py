import random
import matplotlib.pyplot as plt

num_of_tries = 10000
max = 0
good_cards = []
all_cards = []
cards = []
results = []
test = [0, 0, 0, 0, 0, 0, 0]

def third_card(cards):
    third = [0, 0, 0, 0]

    for i in range(0, 4):
        third[i] = (0 - cards[0][i] - cards[1][i])%3

    return third

def run(card, cards, all_cards):
    for car in cards:
        try:
            all_cards.remove(third_card([card, car]))
        except:
            pass

for i in range(0, num_of_tries):
    if i % 100 == 0:
        print(i)
    for c in range(0, 3):
        for n in range(0, 3):
            for s in range(0, 3):
                for f in range(0, 3):
                    all_cards.append([c, n, s, f])
    cards = []
    cards.append(random.choice(all_cards))
    all_cards.remove(cards[0])
    pick = random.choice(all_cards)
    all_cards.remove(pick)

    while all_cards != []:
        for card in cards:
            run(pick, cards, all_cards)
        cards.append(pick)
        if all_cards != []:
            pick = random.choice(all_cards)
            all_cards.remove(pick)

    results.append(len(cards))

    if len(cards) > max:
        good_cards.append(cards)
        max = len(cards)

for result in results:
    test[result-15] += 1

for i in range(0, len(test)-1):
    test[i] = test[i]/num_of_tries

results.sort()
good_cards = good_cards[-1]

print(results[0])
print(results[-1])
print(good_cards)

plt.bar([15, 16, 17, 18, 19, 20, 21], test)
plt.show()
