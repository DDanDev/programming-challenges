def main():
    input();r=list(map(int,input().split()));v=s=o=0
    for x in r:
        if x%2==1:v+=1;s+=x-1;o+=x==1
        else:s+=x-1-v+o+sum(r[v+1:]);v+=1;break
    print(v,s)
main()

# def main():
#     whatever = input()
#     ramsInEach = list(map(int, input().split()))
#     visitCount = 0
#     sumRams = 0
#     onesCount = 0
#     for rams in ramsInEach:
#         if rams % 2 == 1:
#             visitCount += 1
#             sumRams += rams - 1
#             onesCount += rams == 1
#         else:
#             sumRams += rams - 1 - visitCount + onesCount + sum(ramsInEach[visitCount+1:])
#             visitCount += 1
#             break
#     return print(visitCount, sumRams)

# main()

# def main():
#     numberOfDestinations = int(input())
#     ramsInEach = list(map(int, input().split()))

#     sumRams = sum(ramsInEach)

#     onesBeforeEven = 0
#     for index in range(numberOfDestinations):
#         rams = ramsInEach[index]
#         if rams % 2 == 0:
#             return print(f"{index + 1} {sumRams-((index*2)+1-onesBeforeEven)}")
#         elif rams == 1:
#             onesBeforeEven += 1
#     print(f"{numberOfDestinations} {sumRams-(numberOfDestinations)}")

# main()

# def main():
#     numberOfDestinations = int(input())
#     ramsInEach = list(map(int, input().split()))

#     sumRams = sum(ramsInEach)
#     nextLocation = 0
#     locationsVisited = set()

#     while 0 <= nextLocation < numberOfDestinations:
#         currentLocation = nextLocation
#         if ramsInEach[currentLocation] % 2 == 0:
#             nextLocation -= 1
#         else:
#             nextLocation += 1
#         if ramsInEach[currentLocation] > 0:
#             locationsVisited.add(currentLocation)
#             ramsInEach[currentLocation] -= 1
#             sumRams -= 1

#     print(f"{len(locationsVisited)} {sumRams}")

# main()
