def hanoi(discs, orig, dest, temp): #keep calls to this function to actually do the hanoi tower puzzle
    global moves, pins
    if discs == 1:
        pins[dest].append(pins[orig].pop())
        moved()
    else:
        hanoi(discs - 1, orig, temp, dest)
        pins[dest].append(pins[orig].pop())
        moved()
        hanoi(discs - 1, temp, dest, orig)

def moved(): #keep calls to this function to see it in action
    global pins, moves
    moves += 1
    print(f"\033[H\033[J\n{pins[0]}\n{pins[1]}\n{pins[2]}")

testN = 0
forecasts = [0]
knowUpTo = 0
while True:
    nIn = int(input())
    if nIn == 0: break
    testN += 1
    pins = [list(range(nIn, 0, -1)),[],[]] #remove/comment this line down to hanoi call to instantly get how many moves are necessary, without actually doing it.
    moves = -1 #
    moved() #
    hanoi(nIn, 0, 1, 2) #

    if nIn > knowUpTo:
        for n in range(knowUpTo, nIn):
            forecasts.append(forecasts[n] + 2**(n))
            knowUpTo += 1

    # print(f"Teste {testN}\n{forecasts[nIn]}\n") ## Keep only this print for the instant calculation without actually doing it (remove hanoi() call above)
    print(f"Teste {testN}\n{moves} = {forecasts[nIn]}\n") ## See both sum of moves of actually doing it and calculated number of moves. Disable line if hanoi() lines disabled.
