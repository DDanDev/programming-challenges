qtyFractions = int(input("Quantas fraçoes da série para somar: "))

result = 0
for ct in range(qtyFractions):
    ct += 1
    if (ct == 50):
        print(f"{((ct * 2)-1)}/{ct}", end=" ")
    else:
        print(f"{((ct * 2)-1)}/{ct} +", end=" ")
    result += ((ct * 2)-1)/(ct)
print(f"= {result}")