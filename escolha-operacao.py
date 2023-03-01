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


def opInput():
    while True:
        oiInput = input("Escolha uma operação. Digite + para soma, - subtração, * multiplicação, / divisao ou 0 para sair. \n")
        if oiInput == "0":
            print("Closing")
            exit()
        elif not (oiInput == "+" or oiInput == "-" or oiInput == "*" or oiInput == "/"):
            print("Operação invalida!")
        else:
            return oiInput


while True:
    operacao = opInput()
    n1 = numberInput("Digite o primeiro número: ")
    n2 = numberInput("Digite o segundo número: ")
    if operacao == "+":
        resultado = n1 + n2
    elif operacao == "-":
        resultado = n1 - n2
    elif operacao == "*":
        resultado = n1 * n2
    elif operacao == "/":
        try:
            resultado = n1 / n2
        except ZeroDivisionError:
            resultado = "Não é possível dividir por zero!"
    print(resultado)
