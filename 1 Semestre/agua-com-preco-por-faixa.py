consumo = float(input("consumo: "))

franquia = 10
precoFranquia = 7

threshold1 = 30
threshold2 = 100

priceFtoT1 = 1
priceT1T2 = 2
priceT2toInf = 5

conta = 7
if consumo > franquia:
    conta += min(consumo - franquia, threshold1 - franquia) * priceFtoT1
if consumo > threshold1:
    conta += min(consumo - threshold1, threshold2 - threshold1) * priceT1T2
if consumo > threshold2:
    conta += (consumo - threshold2) * priceT2toInf

print(conta)
