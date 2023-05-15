for case in range(int(input())):
    input()
    grades = [int(x) for x in input().split()]
    gradesOrdered = grades[:]
    gradesOrdered.sort(reverse=True)
    noShiftcount = 0
    for index in range(len(grades)):
        if grades[index] == gradesOrdered[index]:
            noShiftcount += 1
    print(noShiftcount)
