import random
qtyNumbers = int(input("Quantos números aleatórios? "))
sum = 0
print("Números gerados: ", end = "")
for ct in range(qtyNumbers):
    genN = random.randint(1,10)
    if ct == (qtyNumbers - 1):
        print(genN)
    else:
        print(genN, end = ", ")
    sum += genN
print(f"\nE a soma destes é: {sum}")