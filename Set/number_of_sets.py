import matplotlib.pyplot as plt
import random

cards = []
picks = []
combinations = []
counter = 0
test = 0
result = 0
sets = []
histogramm = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
num_of_tries = 10000

for i in range(0, 3):
    for n in range(0, 3):
        for m in range(0, 3):
            for k in range(0, 3):
                cards.append((i, n, m, k))

def set(cards):
    test = [0, 0, 0, 0]

    for i in range(0, 4):
        for card in cards:
            test[i] += card[i]

    test = [test[0]%3, test[1]%3, test[2]%3, test[3]%3]

    if test == [0, 0, 0, 0]:
        return True
    return False

for o in range(0, 12):
    for i in range(0, 12):
        for u in range(0, 12):
            if o != i and i != u and o != u:
                    combinations.append((o, i, u))

for i in range(0, num_of_tries):
    if i % (num_of_tries // 100) == 0:
        print(str(int((i/num_of_tries)*100)) + "%")
        
    random.shuffle(cards)
    picks = []
    counter = 0

    test += 1
   
    for i in range(0, 12):
        picks.append(cards[i])

    for combination in combinations:
        set_pick = [picks[combination[0]], picks[combination[1]], picks[combination[2]]]

        if set(set_pick):
            counter += 1

    sets.append(int(counter/6))

sets.sort()

for set in sets:
    histogramm[set-1] += 1

for i in range(0, len(histogramm)):
    histogramm[i] = histogramm[i]/test

x = histogramm[-1]
histogramm.reverse()
histogramm.append(x)
histogramm.remove(histogramm[0])
histogramm.reverse()
# With certainty the best way to code this part

for i in range(0, len(histogramm)-1):
    print(str(i)+": " + str(histogramm[i]*100) + "%")
    
plt.bar([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],histogramm)
plt.show()
