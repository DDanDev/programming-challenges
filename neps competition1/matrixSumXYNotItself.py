##v4 might be possible to take some kind of shortcut in analyzing this matrix but I couldn't think of one in a reasonable time.
## they all actually iterate once more than what's listed because of split(), can't input each whitespace instead of newline in python.
##v3 iterates 4x over size (minimum possible, since needs to finish building matrix before summing)
size = int(input())
maxW = 0
sumrow = [0]*size
sumcol = [0]*size

def makerow(row):
    return list(map(lambda cell,column: handle(row,column,cell),input().split(),range(size)))
def handle(row,column,cell):
    cell = int(cell)
    sumrow[row] += cell
    sumcol[column] += cell
    return cell
table = list(map(makerow, range(size)))

for row in range(size):
    for column in range(size):
        weight = sumcol[column] + sumrow[row] - (2 * table[row][column])
        if (weight > maxW): maxW = weight
        
print(maxW)

##v2 iterates 6x over size
# size = int(input())
# table = [[int(x) for x in input().split()] for _ in [0]*size]
# maxW = 0
# sumrow = [0]*size
# sumcol = [0]*size

# for row in range(size):
#     for column in range(size):
#         cell = table[row][column]
#         sumrow[row] += cell
#         sumcol[column] += cell

# for row in range(size):
#     for column in range(size):
#         weight = sumcol[column] + sumrow[row] - (2 * table[row][column])
#         if (weight > maxW): maxW = weight
        
# print(maxW)



##v1 iterates 10x over size
# size = int(input())
# table = [[int(x) for x in input().split()] for _ in [0]*size]
# maxW = 0
# sumrow = [0]*size
# sumcol = [0]*size

# rotate = [[0]*size for _ in [""]*size]
# for row in range(size):
#     sumrow[row] = sum(table[row])
#     for column in range(size):
#         rotate[row][column] = table[column][row]

# for column in range(size):
#     sumcol[column] = sum(rotate[column])
#     for cell in range(size):
#         weight = sumcol[column] + sumrow[cell] - (2 * rotate[column][cell])
#         if (weight > maxW): maxW = weight
        
# print(maxW)


