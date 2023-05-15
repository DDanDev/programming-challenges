#get test case
# allInput = []
# while True:
    # try:
    #     # allInput += [input()]
    # except:
    #     # raise Exception(allInput)
    #     break


#run with cli at root folder of repo
file = open("./desafios 7/x1Case.txt", "r")
allInput = list(file)
file.close()
#replace allInput.pop(0) for input() to run from cli input. Keep as is and lines above to read from huge lines from file.

##solution:
nOfSoldiers = int(allInput.pop(0))
qSoldierSkills = sorted([int(x) for x in allInput.pop(0).split()])
nSoldierSkills = sorted([int(x) for x in allInput.pop(0).split()])

nMaxWins = 0

for nSoldier in nSoldierSkills:
    if nSoldier > qSoldierSkills[0]:
        nMaxWins += 1
        qSoldierSkills.pop(0)

print(nMaxWins)

###trying to make it faster by spliting, converting to integer and sorting all at once, but much slower than built in algorithms:
# def intSort(string):
#     slot = ""
#     result = []
#     charI = 0
#     strlen = len(string)
#     while charI < strlen:
#         char = string[charI]
#         if char != " ":
#             slot += char
#             charI += 1
#             continue
#         result.append(int(slot))
#         slot = ""
#         charI += 1
#         break

#     while charI < strlen:
#         char = string[charI]
#         if char != " ":
#             slot += char
#             charI += 1
#             continue
#         new = int(slot)
#         slot = ""
#         charI += 1

#         insertat = False
#         existingI = 0
#         resultlen = len(result)
#         while existingI < resultlen:
#             if new <= result[existingI]:
#                 insertat = existingI
#                 break
#             existingI += 1
#         if insertat is not False: result.insert(existingI, new)
#         else: result.append(new)

#     new = int(slot)
    
#     insertat = False
#     existingI = 0
#     resultlen = len(result)
#     while existingI < resultlen:
#         if new <= result[existingI]:
#             insertat = existingI
#             break
#         existingI += 1
#     if insertat is not False: result.insert(existingI, new)
#     else: result.append(new)

#     return result

# def intSort(string):
#     array = string.split()
    
#     result = []
#     for item in array:
#         result.append(int(item))

#     return sorted(result)

# nOfSoldiers = int(allInput.pop(0))
# qSoldierSkills = intSort(allInput.pop(0))
# nSoldierSkills = intSort(allInput.pop(0))

# nMaxWins = 0

# for nSoldier in nSoldierSkills:
#     if nSoldier > qSoldierSkills[0]:
#         nMaxWins += 1
#         qSoldierSkills.pop(0)

# print(nMaxWins)



####### lol the following attempts try to match each n soldier to the best q soldier it can defeat.... takes VERY LONG, and it works to simply check the weakest n vs the weakest q not previously defeated by a weaker n (above)
# qSoldierSkills = [0]*nOfSoldiers
# intin = list(allInput.pop(0))
# lenIn = len(intin)
# slot = ""
# charI = 0
# slotI = 0
# while slotI < nOfSoldiers:
#     char = intin.pop(0)
#     if char != " ":
#         slot += char
#         charI += 1
#         if charI != lenIn: continue
#     qSoldierSkills[slotI] = int(slot)
#     slot = ""
#     slotI += 1
#     charI += 1

# intin = list(allInput.pop(0))
# lenIn = len(intin)
# slot = ""
# charI = 0
# slotI = 0
# maxNWins = 0
# while slotI < nOfSoldiers:
#     char = intin.pop(0)
#     if char != " ":
#         slot += char
#         charI += 1
#         if charI != lenIn: continue
#     nSoldier = int(slot)
#     slot = ""
#     slotI += 1
#     charI += 1

#     iQBestKill = False
#     iQ = 0
#     while iQ < nOfSoldiers:
#         qSoldier = qSoldierSkills[iQ]
#         if (not qSoldier) or (qSoldier >= nSoldier):
#             iQ += 1
#             continue
#         iQBestKill = iQ
#         iQ += 1
#         if nSoldier == (qSoldier + 1):
#             break
#     if iQBestKill is not False:
#         maxNWins += 1
#         qSoldierSkills[iQBestKill] = False

# print(maxNWins)

##########
# nOfSoldiers = int(allInput.pop(0))

# qSoldierSkills = [0]*nOfSoldiers
# intin = list(allInput.pop(0))
# lenIn = len(intin)
# slot = ""
# charI = 0
# slotI = 0
# while slotI < nOfSoldiers:
#     char = intin.pop(0)
#     if char != " ":
#         slot += char
#         charI += 1
#         if charI != lenIn: continue
#     qSoldierSkills[slotI] = int(slot)
#     slot = ""
#     slotI += 1
#     charI += 1

# intin = list(allInput.pop(0))
# lenIn = len(intin)
# slot = ""
# charI = 0
# slotI = 0
# maxNWins = 0
# while slotI < nOfSoldiers:
#     char = intin.pop(0)
#     if char != " ":
#         slot += char
#         charI += 1
#         if charI != lenIn: continue
#     nSoldier = int(slot)
#     slot = ""
#     slotI += 1
#     charI += 1

#     iQBestKill = False
#     iQ = 0
#     while iQ < nOfSoldiers:
#         qSoldier = qSoldierSkills[iQ]
#         if (not qSoldier) or (qSoldier >= nSoldier):
#             iQ += 1
#             continue
#         iQBestKill = iQ
#         iQ += 1
#         if nSoldier == (qSoldier + 1):
#             break
#     if iQBestKill is not False:
#         maxNWins += 1
#         qSoldierSkills[iQBestKill] = False

# print(maxNWins)









#########
# maxNWins = 0
# iQ = 0
# while iQ < nOfSoldiers:
#     qSoldier = qSoldierSkills[iQ]
#     iNLeastNecessary = False
#     iN = 0
#     while iN < nOfSoldiers:
#         nSoldier = nSoldierSkills[iN]
#         if nSoldier > qSoldier:
#             iNLeastNecessary = iN
#             if nSoldier == (qSoldier + 1): break
#         iN += 1
#     if iNLeastNecessary is not False:
#         maxNWins += 1
#         nSoldierSkills[iNLeastNecessary] = False
#     iQ += 1

# print(maxNWins)