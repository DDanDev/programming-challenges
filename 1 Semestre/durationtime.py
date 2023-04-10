
tt = [[int(x) for x in input("HH MM SS: ").split()] for _ in [""]*2]
print(sum([(tt[1][i]-tt[0][i])*(60**x) for i, x in enumerate(range(2,-1,-1))]))