#v2 don't check every rule for every group, discard rules that were already verified, and stop all of it when there are no more rules left to verify
tRlen = int(input())
togetherRestrictions = [input().split() for _ in range(tRlen)]
sRlen = int(input())
separatedRestrictions = [input().split() for _ in range(sRlen)]
groups = [input().split() for _ in range(int(input()))]

violatedCount = 0

for gp in groups:
    if tRlen == 0 and sRlen == 0: break
    
    verifiedIndexes = []
    for checkI in range(tRlen):
        if togetherRestrictions[checkI][0] in gp:
            verifiedIndexes.append(checkI)
            if togetherRestrictions[checkI][1] not in gp:
                violatedCount += 1
    popCount = 0
    for delI in verifiedIndexes: 
        togetherRestrictions.pop(delI - popCount)
        tRlen -= 1
        popCount += 1

    verifiedIndexes = []
    for checkI in range(sRlen):
        if separatedRestrictions[checkI][0] in gp:
            verifiedIndexes.append(checkI)
            if separatedRestrictions[checkI][1] in gp:
                violatedCount += 1
    popCount = 0
    for delI in verifiedIndexes:
        separatedRestrictions.pop(delI - popCount)
        sRlen -= 1
        popCount += 1

print(violatedCount)

#v1
# togetherRestrictions = [input().split() for _ in range(int(input()))]
# separatedRestrictions = [input().split() for _ in range(int(input()))]
# groups = [input().split() for _ in range(int(input()))]
# violatedCount = 0

# for gp in groups:
#     for tR in togetherRestrictions:
#         if tR[0] in gp:
#             if tR[1] not in gp: violatedCount += 1
#     for sR in separatedRestrictions:
#         if sR[0] in gp:
#             if sR[1] in gp: violatedCount += 1

# print(violatedCount)
