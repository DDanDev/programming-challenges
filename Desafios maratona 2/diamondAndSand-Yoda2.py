# 2 better, 1x reps, text one iteration only start to finish, done
#not really, same runtimes on beecrowd.
def main():
    reps = int(input())
    for i in range(reps):
        mine = input()
        openD = count = 0
        for char in mine:
            if char == "<":
                openD += 1
            elif char == ".":
                continue
            elif char == ">" and openD > 0:
                count += 1
                openD -= 1
        print(count)


main()

# 1 accepted - iterations: 1x reps, 3x (kind of, up to 3) text
# reps = int(input())
# for i in range(reps):
#     mine = input().replace(".", "")
#     count = 0
#     while True:
#         try:
#             mine.index("<>")
#             mine = mine.replace("<>", "", 1)
#             count += 1
#         except:
#             break
#     print(count)
