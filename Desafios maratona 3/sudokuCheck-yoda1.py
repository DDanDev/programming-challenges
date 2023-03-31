reps = int(input())

def mistakeInSet(sudokuSet, k):
    for subset in sudokuSet:
        if set(subset) != set(range(1,10)): 
            print(f"Instancia {k}\nNAO\n")
            return True
    else: return False


for k in range(1,reps+1):
    table = [[int(x) for x in input().split()] for _ in [""]*9]
    #check lines
    if mistakeInSet(table, k): continue
    
    #list columns
    rotate = [[0]*9 for _ in [""]*9]
    for row in range(9):
        for column in range(9):
            rotate[row][column] = table[column][row]
    #check columns
    if mistakeInSet(rotate, k): continue
    
    #list blocks
    blocks = []
    for j in range(3):
        for i in range(3):
            pieces = [x[i*3:i*3+3] for x in table[j*3:j*3+3]]
            blocks.append([*pieces[0], *pieces[1], *pieces[2]])
    if mistakeInSet(blocks, k): continue
    
    print(f"Instancia {k}\nSIM\n")

