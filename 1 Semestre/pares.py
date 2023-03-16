limit = int(input("pares até: "))

curr = 0

while curr <= limit:
    if curr % 2 == 0:
        print(curr)
    curr += 1

print("regressivo: ")

curr = limit
while curr >= 0:
    if curr % 2 == 0:
        print(curr)
    curr -= 1
