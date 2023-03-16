def toInt(x):
    try:
        return int(x)
    except:
        return x

def main():
    numberOfDestinations = int(input())-1
    ramsInEach = list(map(toInt, input().split()))

    stealingFromNext = 0
    wasStolenFrom = []
    for i in range(numberOfDestinations + 1):
        wasStolenFrom.append(False)

    while not((stealingFromNext > numberOfDestinations) or (stealingFromNext < 0)):
        currentLocation = stealingFromNext
        if ramsInEach[currentLocation] % 2 == 1:
            stealingFromNext += 1
        else:
            stealingFromNext -= 1
        
        if ramsInEach[currentLocation] > 0:
            wasStolenFrom[currentLocation] = True
            ramsInEach[currentLocation] -= 1

    finalRams = 0
    for qt in ramsInEach:
        finalRams += qt
    # stolenDestinations = wasStolenFrom.count(True)
    print(f"{wasStolenFrom.count(True)} {finalRams}")
main()