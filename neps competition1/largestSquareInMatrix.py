# v3 trying to make v2 faster
# import time
size = int(input())
# start = time.time()
# elapsed = 0
tablesizes = [[0,0,size,size]]
nOfTrees = int(input())
for i in range(nOfTrees):
    xTree, yTree = [int(x)-1 for x in input().split()]
    # lastinputtime = time.time()
    tablesizesDel = []
    for tableIndex, table in enumerate(tablesizes):
        if (table[0] <= xTree < (table[0]+table[2])) and (table[1] <= yTree < (table[1]+table[3])):
            tablesizesDel += [tableIndex]
            newSection = [table[0],table[1],table[2],yTree - table[1]]
            if (newSection[2] > 0) and (newSection[3] > 0): tablesizes += [newSection]
            newSection = [table[0],table[1],xTree - table[0],table[3]]
            if (newSection[2] > 0) and (newSection[3] > 0): tablesizes += [newSection]
            newSection = [xTree + 1,table[1],table[2] - (xTree + 1) + table[0],table[3]]
            if (newSection[2] > 0) and (newSection[3] > 0): tablesizes += [newSection]
            newSection = [table[0],yTree + 1,table[2],table[3] - (yTree + 1) + table[1]]
            if (newSection[2] > 0) and (newSection[3] > 0): tablesizes += [newSection]
    for i in range(len(tablesizesDel)-1,-1,-1): tablesizes.pop(tablesizesDel[i])
    # elapsed += time.time() - lastinputtime
print(f"{max(min(x[2:]) for x in tablesizes)}")
# print(time.time() - start)
# print(time.time() - lastinputtime)
# print(elapsed)

# #v2 each tree breaks table it appears on into 4 tables. Don't really need the actual matrix, only the size.
# size = int(input())
# tablesizes = [[0,0,size,size]] #startingx, startingy, maxx, maxy
# # print(tablesizes)
# nOfTrees = int(input())
# for i in range(nOfTrees):
#     # print("INSERTING TREE")
#     xTree, yTree = [int(x)-1 for x in input().split()]
#     #determine what existing table size is the position in
#     tablesizesDel = []
#     for tableIndex, table in enumerate(tablesizes):
#         if (table[0] <= xTree < (table[0]+table[2])) and (table[1] <= yTree < (table[1]+table[3])):
#             # print("tree within range of", table)
#             tablesizesDel += [tableIndex]
#             upperSection = [table[0],table[1],table[2],yTree - table[1]]
#             leftSection = [table[0],table[1],xTree - table[0],table[3]]
#             rightSection = [xTree + 1,table[1],table[2] - (xTree + 1) + table[0],table[3]]
#             bottomSection = [table[0],yTree + 1,table[2],table[3] - (yTree + 1) + table[1]]
#             # print("adding: ", upperSection, leftSection, rightSection, bottomSection)
#             tablesizes += [upperSection, leftSection, rightSection, bottomSection]
#             #should skip creating sections with size <= 0  
#             # print(tablesizes)
#     # print("deleting: ", tablesizesDel)
#     for i in range(len(tablesizesDel)-1,-1,-1): tablesizes.pop(tablesizesDel[i])
# # print(tablesizes)
# print(f"{max(min(x[2:]) for x in tablesizes)}")

## v1 max size for each cell
# size = int(input())
# table = [[-1 for _ in range(size)] for _ in range(size)]
# nOfTrees = int(input())
# for i in range(nOfTrees):
#     tr, tc = [int(x)-1 for x in input().split()]
#     table[tr][tc] = 0

# for rowi in range(size):
#     lengthSinceLast = 0
#     sqIndex = -1
#     for square in table[rowi]+[0]:
#         sqIndex += 1
#         if square == 0:
#             if lengthSinceLast > 0:
#                 table[rowi][sqIndex-lengthSinceLast:sqIndex] = list(range(lengthSinceLast,0,-1))
#             lengthSinceLast = 0
#         else:
#             lengthSinceLast += 1

# #table print, remove this
# # for i in table: print(" ".join(f"{x:3d}" for x in i))

# for rowi in range(size):
#     for coli in range(size):
#         sizeLimit = min(table[rowi][coli], size - rowi)
#         searchSize = 2
#         while searchSize <= sizeLimit:
#             freecols = table[rowi + searchSize - 1][coli]
#             if freecols < sizeLimit: 
#                 sizeLimit = max(freecols, searchSize - 1)
#             searchSize += 1
#         table[rowi][coli] = sizeLimit

# # #table print, remove this
# # print("max size at each origin:")
# # for i in table: print(" ".join(f"{x:3d}" for x in i))

# print(max(max(x) for x in table))