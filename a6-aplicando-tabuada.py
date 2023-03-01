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
            if (niInput > 10 or niInput < 0):
                print("VALOR INVÁLIDO")
                continue
            else:
                return niInput

nbase = numberInput("")

for multiplier in range (1,11):
    print(f"{nbase}x{multiplier}={nbase * multiplier}")