maxNumber = int(input("Exibir números da serie de Fibonacci até o primeiro número maior que: "))

last2Num = 1
lastNum = 1
print("1, 1, ", end = "")
while lastNum <= maxNumber:
    nextNum = lastNum + last2Num
    if nextNum > maxNumber:
        print(nextNum)
    else:
        print(nextNum, end=", ")
    last2Num = lastNum
    lastNum = nextNum


