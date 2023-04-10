nx = int(input())
ny = int(input())

if (nx == 0 or ny == 0): print("eixos")
elif (ny > 0):
    if (nx > 0): print("Q1")
    else: print("Q2")
elif (ny < 0):
    if (nx > 0): print("Q4")
    else: print("Q3")