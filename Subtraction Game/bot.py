n = int(input("What is the initial number of coins? "))
S = []
num_of_moves = int(input("How many numbers are there to choose from? "))

for i in range(0, num_of_moves):
    S.append(int(input(f"What is the {i+1}. number one can subtract? ")))

S = list(dict.fromkeys(S))
num_of_moves = len(S)
P = []
Q = []

for i in range(0, n+1):
    P.append([i, 0])

for p in range(0, n+1):
    Q = []

    for s in S:
        if p + s <= n:
            Q.append(p + s)
    
    for q in Q:
        for s in S:
            if q - s >= 0:
                if P[q - s][1] == 0:
                    P[q][1] = 1
                    break
                P[q][1] = 0

print("")
print("P: " + str(P))
print("S: " + str(S))
print("")

if P[-1][1] == 1:
    print("The player beginning will win!")
else:
    print("The player beginning will lose!")

m = n

while m != 0:
    R = []
    T = []

    for s in S:
        if m - s >= 0:
            R.append(m - s)

    for r in R:
        if P[r][1] == P[m][1]:
            T.append(r)

    for t in T:
        R.remove(t)
        
    print(R)
    m = int(input("What is the current number of coins? "))