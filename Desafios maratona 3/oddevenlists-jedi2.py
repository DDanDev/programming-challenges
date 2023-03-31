def printlist(array,text):
    for index, item in enumerate(array):
        print(f"{text}[{index}] = {item}")
odds = []; evens = []
for _ in range(15):
    inp = int(input())
    if inp % 2 == 0: 
        evens.append(inp)
        if len(evens) == 5: 
            printlist(evens,"par")
            evens = []
    else:
        odds.append(inp)
        if len(odds) == 5: 
            printlist(odds,"impar")
            odds = []
printlist(odds,"impar")
printlist(evens,"par")

