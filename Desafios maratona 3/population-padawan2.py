#v2, i just don't like repeating conditionals
reps = range(int(input()))
for _ in reps:
    popA, popB, growA, growB = [int(x.replace(".","")) for x in input().split()]
    yearsPassed = 0
    while True:
        yearsPassed += 1
        if yearsPassed > 100: 
            print("Mais de 1 seculo.")
            break
        popA += int((popA * growA) / 1000)
        popB += int((popB * growB) / 1000)
        if popA > popB: 
            print(f"{yearsPassed} anos.")
            break

#v1 testing is it faster to use float or to handle it myself with integers
reps = range(int(input()))
for _ in reps:
    popA, popB, growA, growB = [float(x) for x in input().split()]
    yearsPassed = 0
    while popA <= popB:
        yearsPassed += 1
        if yearsPassed > 100: break
        popA += int((popA * growA) / 100)
        popB += int((popB * growB) / 100)
    if yearsPassed > 100: print("Mais de 1 seculo.")
    else: print(f"{yearsPassed} anos.")

#v1 testing is it faster to use float or to handle it myself with integers
#runtime using int/1000 was slightly lower than HALF the runtime using float!! why?
reps = range(int(input()))
for _ in reps:
    popA, popB, growA, growB = [int(x.replace(".","")) for x in input().split()]
    yearsPassed = 0
    while popA <= popB:
        yearsPassed += 1
        if yearsPassed > 100: break
        popA += int((popA * growA) / 1000)
        popB += int((popB * growB) / 1000)
    if yearsPassed > 100: print("Mais de 1 seculo.")
    else: print(f"{yearsPassed} anos.")