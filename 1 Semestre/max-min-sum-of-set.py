def numberInput(textPrompt):
    while True:
        niInput = input(textPrompt)
        try:
            niInput = float(niInput)
        except ValueError:
            print("That's not a number!")
        except:
            print("Error")
        else:
            return niInput

n1 = numberInput("Digite um número: ")    
maxN = n1
minN = n1
sumNs = n1

while True:
    newNumber = numberInput("Digite um número ou 0 para terminar: ")
    if newNumber == 0:
        break
    maxN = max(newNumber, maxN)
    minN = min(newNumber, minN)
    sumNs += newNumber

print(f"Largest number was: {maxN}")
print(f"Smallest number was: {minN}")
print(f"Sum of all numbers was: {sumNs}")
