# v3 trying to make it faster (didnt really) by not using so many conditional detours. But introduced too many separate iteration loops.

# def sumStr(bar):
#     return sum([int(note) for note in bar])

# def main():
#     inp = input()
#     while inp != "*":
        # print(sum([1 for summed in [sumStr(x) for x in [x.split("n")[:-1] for x in inp[1:-1].replace("W","64n").replace("H","32n").replace("Q","16n").replace("E","8n").replace("S","4n").replace("T","2n").replace("X","1n").split("/")]] if summed == 64]))
#         inp = input()
# main()

#the complex print above separated in steps
# composition = input()
# composition = composition[1:-1].replace("W","64n").replace("H","32n").replace("Q","16n").replace("E","8n").replace("S","4n").replace("T","2n").replace("X","1n").split("/")
# composition = [x.split("n")[:-1] for x in composition]
# composition = [sumStr(x) for x in composition]
# print(composition)

    




#v2 a que deu menor runtime
def main():
    composition = input()
    correctBars = 0
    barlength = 0
    while composition != "*":
        for char in composition[1:]:
            if char == "W": barlength += 64
            elif char == "H": barlength += 32
            elif char == "Q": barlength += 16
            elif char == "E": barlength += 8
            elif char == "S": barlength += 4
            elif char == "T": barlength += 2
            elif char == "X": barlength += 1
            elif char == "/": 
                if barlength == 64: correctBars += 1
                barlength = 0
        print(correctBars)
        correctBars = 0
        composition = input()
main()

#v1
# def main():
#     composition = input().split("/")
#     while composition != ["*"]:
#         correctBars = 0
#         for bar in composition[1:-1]:
#             barlength = 0
#             for char in bar:
#                 if char == "W": barlength += 64
#                 elif char == "H": barlength += 32
#                 elif char == "Q": barlength += 16
#                 elif char == "E": barlength += 8
#                 elif char == "S": barlength += 4
#                 elif char == "T": barlength += 2
#                 elif char == "X": barlength += 1
#             if barlength == 64: correctBars += 1
#         print(correctBars)
#         composition = input().split("/")
# main()

#logica v1, tentando otimizar, depois de ter feito a v3 (um print lindo cheio de list comprehension mas que deu maior tempo runtime)
# def main():
#     composition = input().split("/")
#     while composition != ["*"]:
#         correctBars = 0
        
#         for bar in composition[1:-1]:
#             barlength = 64
#             for char in bar:
#                 if barlength < 0: break
#                 elif char == "W": barlength -= 64
#                 elif char == "H": barlength -= 32
#                 elif char == "Q": barlength -= 16
#                 elif char == "E": barlength -= 8
#                 elif char == "S": barlength -= 4
#                 elif char == "T": barlength -= 2
#                 elif char == "X": barlength -= 1
#             if barlength == 0: correctBars += 1
        
#         print(correctBars)
#         composition = input().split("/")
# main()