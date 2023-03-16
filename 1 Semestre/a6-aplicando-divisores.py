def numberInput(textPrompt):
    while True:
        niInput = input(textPrompt)
        try:
            niInput = int(niInput)
        except ValueError:
            print("That's not a number!")
        except:
            print("Error")
        else:
            if (niInput < 1):
                print("VALOR INVÁLIDO")
                continue
            else:
                return niInput
            
nbase = numberInput("")

for divisor in range(1,nbase+1):
    if (nbase % divisor == 0):
        print(divisor, end=" ")
