#coloring squares in a stripe acording to the shortest distance to a square already colored with color 0, up to 10 different colors
input()
lengthSinceLast = 0
fixJobs = []
sqIndex = -1
firstbatch = True
def handle(square):
    global sqIndex, lengthSinceLast, firstbatch
    sqIndex += 1
    square = int(square)
    if square == 0:
        if firstbatch:
            if lengthSinceLast > 0:
                fixJobs.append([min(lengthSinceLast, 8), sqIndex]) #length to fix, index to start fixing at steps -1
            firstbatch = False
        elif lengthSinceLast > 1:
            fixJobs.append([min(lengthSinceLast // 2, 8), sqIndex])
        lengthSinceLast = 0
        return 0
    else:
        lengthSinceLast += 1
        if firstbatch: return 9
        return lengthSinceLast if lengthSinceLast < 10 else 9

stripe = [handle(x) for x in input().split()]

for job in fixJobs:
    stripe[job[1]-job[0]:job[1]] = list(range(job[0],0,-1))

print(" ".join(str(x) for x in stripe))
