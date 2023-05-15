#v3 not sorting the entire list, only finding their positions. Still TLE
debug = True
caseN = 0
while True:
    numbersQty, queriesQty = [int(x) for x in input().split()]
    if numbersQty == queriesQty == 0: break
    caseN += 1

    numbers = [0]*numbersQty
    for i in range(numbersQty): numbers[i] = int(input())
    queries = [[0,0]]*queriesQty
    for i in range(queriesQty): queries[i] = [i,int(input())]

    results = [""]*queriesQty
    
    if debug: print(f"numbers: {numbers}\nqueries: {queries}\nresults: {results}\n")

    for q in queries:
        shiftsLeft = 0
        leftmark = 0
        rightmark = numbersQty-1

        #shift left what's smaller and right what's larger than q.
        #keep track where n == q is in list, or if it isn't
        qInNumbers = False
        nAtRMarker = False
        if debug: qInNumbersAt = -1
        while (leftmark + 1) < rightmark:
            while numbers[leftmark] <= q[1]: 
                if numbers[leftmark] == q[1]:
                    qInNumbersAt = leftmark
                    qInNumbers = True
                    if debug: print(f"numbers: {numbers}\nqueries: {queries}\nresults: {results}\nqInNumbersAt: {qInNumbersAt}\n")
                if leftmark + 1 == numbersQty: break #no number larger than queried one
                leftmark += 1
                if debug: print(f"numbers: {numbers}\nqueries: {queries}\nresults: {results}\nleftmark: {leftmark}\n")
            while numbers[rightmark] >= q[1] and rightmark > leftmark + 1:
                nAtRMarker = False
                if numbers[rightmark] == q[1]:
                    nAtRMarker = True
                    qInNumbers = True
                    qInNumbersAt = rightmark
                    if debug: print(f"numbers: {numbers}\nqueries: {queries}\nresults: {results}\nqInNumbersAt: {qInNumbersAt}\n")
                if rightmark - 1 < 0: break #no number smaller than q
                rightmark -= 1
                if debug: print(f"numbers: {numbers}\nqueries: {queries}\nresults: {results}\nrightmark: {rightmark}\n")
            replaced = numbers[leftmark]
            numbers[leftmark] = numbers [rightmark]
            numbers[rightmark] = replaced
            if nAtRMarker: qInNumbersAt = leftmark
            if debug: print(f"numbers: {numbers}\nqueries: {queries}\nresults: {results}\nqInNumbersAt: {qInNumbersAt}\n")
        
        #put q at its position
        if qInNumbers:
            # if not nAtRMarker:
            if debug: print(f"swaping {qInNumbersAt} to {leftmark}")
            numbers.insert(leftmark, numbers.pop(qInNumbersAt))
            results[q[0]] = f"{q[1]} found at {leftmark + 1}"
            if debug: print(f"numbers: {numbers}\nqueries: {queries}\nresults: {results}\nqInNumbersAt: {qInNumbersAt}\n")
        else: results[q[0]] = f"{q[1]} not found"
        if debug: print(f"results: {results}")

    print(f"CASE# {caseN}:")
    for r in results: print(r)

# #v3 not sorting the entire list, only finding their positions. Still TLE
# caseN = 0
# while True:
#     numbersQty, queriesQty = [int(x) for x in input().split()]
#     if numbersQty == queriesQty == 0: break
#     caseN += 1

#     numbers = [int(input()) for _ in range(numbersQty)]
#     queries = [[x, int(input())] for x in range(queriesQty)]
#     queriesLen = queriesQty

#     results = [""]*queriesQty
    
#     for q in queries:
#         shiftsLeft = 0
#         found = False
#         for n in numbers:
#             if n < q[1]: shiftsLeft += 1
#             elif n == q[1]: found = True
#         if found: results[q[0]] = f"{q[1]} found at {shiftsLeft + 1}"
#         else: results[q[0]] = f"{q[1]} not found"

#     print(f"CASE# {caseN}:")
#     for r in results: print(r)

#v2 time limit exceeded still.
# caseN = 0
# while True:
#     numbersQty, queriesQty = [int(x) for x in input().split()]
#     if numbersQty == queriesQty == 0: break
#     caseN += 1

#     numbers = sorted([int(input()) for _ in range(numbersQty)])
#     queries = [[x, int(input())] for x in range(queriesQty)]
#     queriesLen = queriesQty

#     results = [""]*queriesQty
#     nI = -1
#     for n in numbers:
#         nI += 1
#         qI = -1
#         for q in queries:
#             qI += 1
#             if q[1] == n:
#                 results[q[0]] = f"{queries.pop(qI)[1]} found at {nI+1}"
#                 queriesLen -= 1
#                 break
#         if queriesLen == 0: break
#     if queriesLen != 0:
#         for q in queries:
#             results[q[0]] = f"{q[1]} not found"

#     print(f"CASE# {caseN}:")
#     for r in results: print(r)

#v1 time limit exceeded
# caseN = 0
# while True:
#     numbersQty, queriesQty = [int(x) for x in input().split()]
#     if numbersQty == queriesQty == 0: break
#     caseN += 1

#     numbers = sorted([int(input()) for _ in range(numbersQty)])
#     print(f"CASE# {caseN}:")
#     for _ in range(queriesQty):
#         findThis = int(input())
#         try: print(f"{findThis} found at {numbers.index(findThis)+1}")
#         except: print(f"{findThis} not found")
