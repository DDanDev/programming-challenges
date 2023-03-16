def main():
    numberOfDestinations = int(input())
    ramsInEach = list(map(int, input().split()))
    
    #skipAll logic:
    #commented previous version 1.1s run time. 
    #New doesn't filter entire array to then access it again to find the index
    #goes through the array only until it finds an even and already saves the index it is found at.
    #new again, no longer filter and count ones later, do it while iterating.
    sumRams = sum(ramsInEach)
    # firstEvenAtPos = 0
    
    onesBeforeEven = 0
    for index, rams in enumerate(ramsInEach):
        if rams % 2 == 0:
            return print(f"{index + 1} {sumRams-((index*2)+1-onesBeforeEven)}")
        elif rams == 1:
            onesBeforeEven += 1
    print(f"{numberOfDestinations} {sumRams-(numberOfDestinations)}")


    # evenRams = list(filter(lambda x: x % 2 == 0, ramsInEach))
    # if firstEvenAtPos:
        # firstEvenAtPos = ramsInEach.index(evenRams[0])+1
        # onesBeforeEven = len(list(filter(lambda x: x == 1, ramsInEach[:firstEvenAtPos])))
        # print(f"{firstEvenAtPos} {sumRams-((((firstEvenAtPos-1)*2)+1)-onesBeforeEven)}")
    # else:
    # print(f"{numberOfDestinations} {sumRams-(numberOfDestinations)}")
    

    # manual logic:
    # numberOfDestinations -= 1
    # stealingFromNext = 0
    # farthestStolen = 0

#     while not ((stealingFromNext > numberOfDestinations) or (stealingFromNext < 0)):
#         currentLocation = stealingFromNext
#         ramsCurLoc = ramsInEach[currentLocation]
#         if ramsCurLoc % 2 == 1:
#             stealingFromNext += 1
#         else:
#             stealingFromNext -= 1

#         if ramsCurLoc > 0:
#             farthestStolen = currentLocation if currentLocation > farthestStolen else farthestStolen
#             ramsInEach[currentLocation] -= 1

#     finalRams = 0
#     for qt in ramsInEach:
#         finalRams += qt
#     return print(f"{farthestStolen+1} {finalRams}")

main()
