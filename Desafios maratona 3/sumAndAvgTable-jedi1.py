# v4 cheating no matrix, just ignore everything and do op at input time
#run 0.08s
operation = input()
if operation == "S":
    answer = 0
    for _ in range(12): input()
    for i in range(1,6):
        for _ in range(12-i): input()
        for _ in range(i): answer += float(input())
    for i in range(5,0,-1):
        for _ in range(12-i): input()
        for _ in range(i): answer += float(input())
    for _ in range(12): input()
    print(answer)
elif operation == "M":
    answer = 1
    for _ in range(12): input()
    for i in range(1,6):
        for _ in range(12-i): input()
        for _ in range(i): answer = answer * float(input())
    for i in range(5,0,-1):
        for _ in range(12-i): input()
        for _ in range(i): answer = answer * float(input())
    for _ in range(12): input()
    print(answer)

# v3 zero ifs, zero repetition over unused cells
operation = input()
table = [[input() for _ in [""]*12] for _ in [""]*12]

if operation == "S":
    answer = 0
    for row in range(1,6):
        for cell in range(11,11-row,-1):
            answer += float(table[row][cell])
    for row in range(6,11):
        for cell in range(11,row,-1):
            answer += float(table[row][cell])
    print(answer)
elif operation == "M":
    answer = 1
    for row in range(1,6):
        for cell in range(11,11-row,-1):
            answer = answer * float(table[row][cell])
    for row in range(6,11):
        for cell in range(11,row,-1):
            answer = answer * float(table[row][cell])
    print(answer)


#v3 in the makes
operation = input()
table = [[input() for _ in [""]*12] for _ in [""]*12]

if operation == "S":
    answer = 0
    for row in range(1,6):
        for cell in range(1,row+1):
            answer += float(table[row][12-cell])
    for row in range(6,11):
        for cell in range(1,12-row):
            answer += float(table[row][12-cell])
    print(answer)
elif operation == "M":
    answer = 1
    for row in range(1,6):
        for cell in range(1,row+1):
            answer = answer * float(table[row][12-cell])
    for row in range(6,11):
        for cell in range(1,12-row):
            answer = answer * float(table[row][12-cell])
    print(answer)



# v2 one less if
operation = input()
table = [[input() for _ in [""]*12] for _ in [""]*12]

if operation == "S":
    answer = 0
    for rowi in range(1,6):
        for celli in range(7,12):
            if celli >= (12 - rowi):
                answer += float(table[rowi][celli])
    for rowi in range(6,11):
        for celli in range(7,12):
            if celli >= (12 + rowi - 11):
                answer += float(table[rowi][celli])
    print(answer)
elif operation == "M":
    answer = 1
    for rowi in range(1,6):
        for celli in range(7,12):
            if celli >= (12 - rowi):
                answer = answer * float(table[rowi][celli])
    for rowi in range(6,11):
        for celli in range(7,12):
            if celli >= (12 + rowi - 11):
                answer = answer * float(table[rowi][celli])
    print(answer)

# v1 accepted
# operation = input()
# table = [[input() for _ in [""]*12] for _ in [""]*12]

# if operation == "S":
#     answer = 0
#     for rowi in range(1,11):
#         for celli in range(7,12):
#             if rowi <=5:
#                 if celli >= (12 - rowi):
#                     answer += float(table[rowi][celli])
#             else:
#                 if celli >= (12 + rowi - 11):
#                     answer += float(table[rowi][celli])
#     print(answer)
# elif operation == "M":
#     answer = 1
#     for rowi in range(1,11):
#         for celli in range(7,12):
#             if rowi <=5:
#                 if celli >= (12 - rowi):
#                     answer = answer * float(table[rowi][celli])
#             else:
#                 if celli >= (12 + rowi - 11):
#                     answer = answer * float(table[rowi][celli])
#     print(answer)
