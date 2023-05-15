def importPaths(colonyIndex, trackShortestToIndex, shortestSoFar):
    shortestPathStillUnexplored = False
    importingPaths = []
    skippedImporting = []
    for tunnel in coloniesNotImportedPaths[colonyIndex]:
        if tunnel[0] == trackShortestToIndex:
            if tunnel[1] < shortestSoFar or shortestSoFar == False:
                shortestSoFar = tunnel[1]
            skippedImporting.append(tunnel)
            continue
        firstIteration = True
        for _ in range(2):
            colonies = coloniesNotImportedPaths if firstIteration else coloniesImportedPaths
            for otherTunnel in colonies[tunnel[0]]:
                if otherTunnel[0] == colonyIndex: continue
                if otherTunnel[1] == False: continue
                totalLength = otherTunnel[1] + tunnel[1]
                if otherTunnel[0] == trackShortestToIndex: 
                    if ((totalLength < shortestSoFar) or shortestSoFar == False):
                        shortestSoFar = totalLength
                importingPaths.append([otherTunnel[0],totalLength])
            firstIteration = False

    for importThis in coloniesNotImportedPaths[colonyIndex]:
        prevLength = coloniesImportedPaths[colonyIndex][importThis[0]][1]
        if importThis[1] < prevLength or prevLength == False: 
            coloniesImportedPaths[colonyIndex][importThis[0]] = importThis

    coloniesNotImportedPaths[colonyIndex] = []
    importingPaths += skippedImporting
    for unimportedDestination in importingPaths:
        prevLength = coloniesImportedPaths[colonyIndex][unimportedDestination[0]][1]
        if unimportedDestination[1] < prevLength or prevLength == False:
            coloniesNotImportedPaths[colonyIndex].append(unimportedDestination)
            shortestPathStillUnexplored = unimportedDestination[1] if (unimportedDestination[1] < shortestPathStillUnexplored or shortestPathStillUnexplored == False) else shortestPathStillUnexplored

    return [shortestPathStillUnexplored, shortestSoFar]

while True:
    coloniesQty = int(input())
    if coloniesQty == 0: break
    
    connectsTo, pathLength = [int(x) for x in input().split()]
    coloniesNotImportedPaths = [[[1, pathLength]],[[connectsTo, pathLength]]]
    for i in range(2, coloniesQty):
        connectsTo, pathLength = [int(x) for x in input().split()]
        coloniesNotImportedPaths.append([[connectsTo, pathLength]])
        coloniesNotImportedPaths[connectsTo].append([i,pathLength])
    
    coloniesImportedPaths = [[[x, False] for x in range(coloniesQty)] for _ in range(coloniesQty)]

    queriesQty = int(input())
    queryResults = []
    for qI in range(queriesQty):
        qStart, qDestination = [int(x) for x in input().split()]

        shortestSoFar = coloniesImportedPaths[qStart][qDestination][1]

        if len(coloniesNotImportedPaths[qStart]):
            shortestPathStillUnexplored = min([x[1] for x in coloniesNotImportedPaths[qStart]]) 
            while (((shortestPathStillUnexplored + 1) < shortestSoFar) and shortestPathStillUnexplored != False) or shortestSoFar == False:
                shortestPathStillUnexplored, shortestSoFar = importPaths(qStart, qDestination, shortestSoFar)
        
        queryResults.append(str(shortestSoFar))
    print(" ".join(queryResults))







# # debugging = False

# def importPaths(colonyIndex, trackShortestToIndex, shortestSoFar): #sends all currently in notImported to Imported (excpet any destination tunnels, would be unnecessary to import their subpaths now and can't flag them as imported if didnt import their subpaths, that would break future queries), imports subpaths into that colony's notimported, returns shortest unimported(so if a path is already found to destination and is smaller than what's still possible, we can stop making the connections), and shortest to destination if any.
#     shortestPathStillUnexplored = False
#     importingPaths = []
#     skippedImporting = []
#     for tunnel in coloniesNotImportedPaths[colonyIndex]:
#         if tunnel[0] == trackShortestToIndex:
#             if tunnel[1] < shortestSoFar or shortestSoFar == False:
#                 shortestSoFar = tunnel[1]
#             skippedImporting.append(tunnel)
#             continue
#         firstIteration = True
#         for _ in range(2):
#             colonies = coloniesNotImportedPaths if firstIteration else coloniesImportedPaths
#             for otherTunnel in colonies[tunnel[0]]:
#                 if otherTunnel[0] == colonyIndex: continue
#                 if otherTunnel[1] == False: continue
#                 totalLength = otherTunnel[1] + tunnel[1]
#                 if otherTunnel[0] == trackShortestToIndex: 
#                     if ((totalLength < shortestSoFar) or shortestSoFar == False):
#                         shortestSoFar = totalLength
#                 importingPaths.append([otherTunnel[0],totalLength])
#             firstIteration = False

#     for importThis in coloniesNotImportedPaths[colonyIndex]:
#         prevLength = coloniesImportedPaths[colonyIndex][importThis[0]][1]
#         if importThis[1] < prevLength or prevLength == False: 
#             coloniesImportedPaths[colonyIndex][importThis[0]] = importThis

#     coloniesNotImportedPaths[colonyIndex] = []
#     importingPaths += skippedImporting
#     for unimportedDestination in importingPaths:
#         prevLength = coloniesImportedPaths[colonyIndex][unimportedDestination[0]][1]
#         if unimportedDestination[1] < prevLength or prevLength == False:
#             coloniesNotImportedPaths[colonyIndex].append(unimportedDestination)
#             shortestPathStillUnexplored = unimportedDestination[1] if (unimportedDestination[1] < shortestPathStillUnexplored or shortestPathStillUnexplored == False) else shortestPathStillUnexplored

#     return [shortestPathStillUnexplored, shortestSoFar]

# # caseN = 0 # Print all at once at the end
# # queryResultsAll = [] # Print all at once at the end
# while True:
#     coloniesQty = int(input())
#     if coloniesQty == 0: break
#     # queryResultsAll.append([]) # Print all at once at the end
    
#     connectsTo, pathLength = [int(x) for x in input().split()]
#     coloniesNotImportedPaths = [[[1, pathLength]],[[connectsTo, pathLength]]]
#     for i in range(2, coloniesQty):
#         connectsTo, pathLength = [int(x) for x in input().split()]
#         coloniesNotImportedPaths.append([[connectsTo, pathLength]])
#         coloniesNotImportedPaths[connectsTo].append([i,pathLength])
#     # if debugging: [print(f"colony {cI}: {colony}") for cI, colony in enumerate(coloniesNotImportedPaths)]
    
#     coloniesImportedPaths = [[[x, False] for x in range(coloniesQty)] for _ in range(coloniesQty)]
#     # if debugging: print(coloniesImportedPaths)

#     queriesQty = int(input())
#     queryResults = []
#     for qI in range(queriesQty):
#         qStart, qDestination = [int(x) for x in input().split()]

#         shortestSoFar = coloniesImportedPaths[qStart][qDestination][1]

#         if len(coloniesNotImportedPaths[qStart]):
#             shortestPathStillUnexplored = min([x[1] for x in coloniesNotImportedPaths[qStart]]) 
        
#             # if debugging: print(f'init colony {qStart}: {coloniesImportedPaths[qStart]} and {coloniesNotImportedPaths[qStart]}')
#             while (((shortestPathStillUnexplored + 1) < shortestSoFar) and shortestPathStillUnexplored != False) or shortestSoFar == False:
#                 shortestPathStillUnexplored, shortestSoFar = importPaths(qStart, qDestination, shortestSoFar)
#                 # if debugging: print(f'done colony {qStart}: {coloniesImportedPaths[qStart]} and {coloniesNotImportedPaths[qStart]} un: {shortestPathStillUnexplored} sh: {shortestSoFar}')
        
#         # if debugging: print(shortestSoFar)
#         # queryResultsAll[caseN].append(str(shortestSoFar)) # Print all at once at the end
#         queryResults.append(str(shortestSoFar))
#     print(" ".join(queryResults))
#     # if debugging: print("-------")
#     # if debugging: [print(f"colony {i}: {coloniesImportedPaths[i]} and unimported: {coloniesNotImportedPaths[i]}") for i in range(coloniesQty)]
#     # caseN += 1 # Print all at once at the end

# # [print(" ".join(x)) for x in queryResultsAll] # Print all at once at the end






