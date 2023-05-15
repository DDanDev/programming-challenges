def populateFib(upto):
    global knowUpTo, fibSequence
    for nbr in range(knowUpTo + 1, upto + 1):
        fibSequence.append([fibSequence[nbr - 1][0] + fibSequence[nbr - 2][0], 1 + fibSequence[nbr - 1][1] + fibSequence[nbr - 2][1]])
    knowUpTo = upto

knowUpTo = 1
fibSequence = [[0, 1], [1, 1]]

nOfCases = int(input())
for i in range(nOfCases):
    nbrCase = int(input())
    if nbrCase > knowUpTo: populateFib(nbrCase)
    print(f"fib({nbrCase}) = {fibSequence[nbrCase][1] - 1} calls = {fibSequence[nbrCase][0]}")