def main():
    tableSizeRC = list(map(lambda x: int(x), input().split()))
    table = []
    for i in range(tableSizeRC[0]):
        table.append(list(map(lambda x: int(x), input().split())))

    for x in range(1,tableSizeRC[0]-1):
        foundInXatY = []
        for y, yValue in enumerate(table[x]):
            if y == 0 or y == tableSizeRC[1]-1:
                continue
            if yValue == 42:
                foundInXatY.append(y)
        
        for yFound in foundInXatY:
            if (table[x-1][yFound] == 7 and table[x-1][yFound-1] == 7 and table[x-1][yFound+1] == 7 and table[x][yFound-1] == 7 and table[x][yFound+1] == 7 and table[x+1][yFound-1] == 7 and table[x+1][yFound] == 7 and table[x+1][yFound+1] == 7):
                return print(f"{x+1} {yFound+1}")
            
    return print("0 0")
main()
