while True:
    cars, capacity = [int(x) for x in input().split()]
    if cars == capacity == 0: break
    parkLine = []
    brokeat = False

    for carNumber in range(cars):
        carin, carout = [int(x) for x in input().split()]        
        
        #remove cars that exited up to car in
        while len(parkLine) > 0:
            if parkLine[-1] <= carin:
                parkLine.pop(-1)
                continue
            break

        #add car if parking is empty
        if len(parkLine) == 0:
            parkLine += [carout]
            continue
            
        #cant add car if:
        #this car plans to leave later than the car in front
        if carout > parkLine[-1]: brokeat = carNumber; break

        #capacity (cars exited)
        if len(parkLine) == capacity: brokeat = carNumber; break

        #ok, add the car
        parkLine += [carout]

    if brokeat:
        for _ in range(brokeat+1, cars): input()
        print("Nao")
    else: print("Sim")