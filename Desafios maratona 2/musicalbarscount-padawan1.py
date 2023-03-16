composition = input().split("/")
while composition[0] != "*":
    correctBars = 0
    for bar in composition:
        barlength = 0
        for char in bar:
            if char == "W": barlength += 64
            elif char == "H": barlength += 32
            elif char == "Q": barlength += 16
            elif char == "E": barlength += 8
            elif char == "S": barlength += 4
            elif char == "T": barlength += 2
            elif char == "X": barlength += 1
        if barlength == 64: correctBars += 1
    print(correctBars)
    composition = input().split("/")