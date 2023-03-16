coefA = float(input("?x²"))
coefB = float(input("?x"))
coefC = float(input("+?"))

if (coefA == 0):
    print("Não há equação de 2o grau")
else:
    delta = ((coefB) ** 2) - (4*coefA*coefC)
    if delta < 0:
        print("Não existem raizes reais")
    else:
        raiz1 = (-coefB + (delta**(1/2)))/(2*coefA)
        if delta > 0:
            raiz2 = (-coefB - (delta**(1/2)))/(2*coefA)
            print(f"Raízes : x1 = {raiz1} e x2 = {raiz2}")
        else:
            print(f"Raíz : x = {raiz1}")

