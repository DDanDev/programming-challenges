#unfinished, did NOT do this one.

priority0 = ["^"]
priority1 = ["*","/"]
priority2 = ["+","-"]
parenthesis = ["(",")"]


for _ in range(int(input())):
    infix = input()
    postfix = ""
    opLine = []
    operand = ""
    currParLevel = 0
    currPriority = 2
    for char in infix:
        if char in priority0: opLine += [char]
        if char in priority1: opLine += [char]
        if char in priority2: opLine += [char]
        if char == ")": postfix += operand + "".join(opLine)
        try:
            int(char)
            operand += char
        except:
            operand += char
    
    print(postfix)

