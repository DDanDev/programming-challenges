def entrada_carro():
    global carros
    carros = []
    for i in range(4):
        carros.append(input())

def entrada_consumo():
    global consumos
    consumos = []
    for i in range(4):
        consumos.append(float(input()))

def economico():
    leastLperKM = min(consumos)
    indexOfBest = consumos.index(leastLperKM)
    return carros[indexOfBest]

def main():
    entrada_carro()
    entrada_consumo()
    print(economico())
    
main()