kmPercurso = float(input("Km do percurso: "))
gasPercurso = float(input("Litros de gasolina do percurso: "))

eficiencia = kmPercurso / gasPercurso

if (eficiencia < 8):
    print(f"Venda o carro! Consumo de {eficiencia:.2f}km/l")
elif (eficiencia <= 12):
    print(f"Econômico! Consumo de {eficiencia:.2f}km/l")
else:
    print(f"Supereconômico! Consumo de {eficiencia:.2f}km/l")

