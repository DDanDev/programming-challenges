oldPrice, newPrice = input().split()
oldPrice, newPrice = float(oldPrice), float(newPrice)

print(f"{(((newPrice/oldPrice)-1)*100):.2f}%")