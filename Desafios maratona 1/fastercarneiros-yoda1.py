def main():
    numberOfDestinations = int(input())-1
    ramsInEach = list(map(int, input().split()))

    stealingFromNext = 0
    farthestStolen = 0

    while not ((stealingFromNext > numberOfDestinations) or (stealingFromNext < 0)):
        currentLocation = stealingFromNext
        ramsCurLoc = ramsInEach[currentLocation]
        if ramsCurLoc % 2 == 1:
            stealingFromNext += 1
        else:
            stealingFromNext -= 1

        if ramsCurLoc > 0:
            farthestStolen = currentLocation if currentLocation > farthestStolen else farthestStolen
            ramsInEach[currentLocation] -= 1

    finalRams = 0
    for qt in ramsInEach:
        finalRams += qt
    return print(f"{farthestStolen+1} {finalRams}")

main()
