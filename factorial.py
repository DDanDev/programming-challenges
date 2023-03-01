nInput = int(input("Fatorial de: "))

result = 1
for currN in range(nInput,1,-1):
    result = result * currN
print(f"Result {result}")