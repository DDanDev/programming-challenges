def main():
    numberOfDestinations = int(input())
    ramsInEach = list(map(int, input().split()))
    
    foundEven = False
    onesFound = 0
    totalRams = 0
    count = 0

    for currN in ramsInEach:
        if currN % 2 == 1 and not foundEven:
            count += 1            
            totalRams += currN            
            if currN == 1:
                onesFound += 1                
        elif currN % 2 == 0 and not foundEven:
            foundEven = True            
            stolenRams = ((count * 2) + (1 if currN != 0 else 0)) - onesFound            
            visitedDests = count + 1            
            totalRams += currN            
        elif foundEven:
            totalRams += currN            
        ramsInEach = ramsInEach[len(str(currN)) + 1:]        
    if foundEven:
        print(f"{visitedDests} {totalRams - stolenRams}")
    else:
        print(f"{count} {totalRams-count}")

main()
