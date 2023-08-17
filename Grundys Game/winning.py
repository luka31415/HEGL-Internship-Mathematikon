P = []
N = []
for i in range(1, 101):
    P.append(i)

for p in range(1, len(P)):
    for i in range(0, p):
        try:
            N.append(P[p]+P[i])
        except:
            pass

    for n in N:
        try:
            P.remove(n)
        except:
            pass

for a in range(1, 101):
    if a in P:
        print(str(a) + ": P")
    elif a in N:
        print(str(a) + ": N")