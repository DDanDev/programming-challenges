def valorPagamento(value, daysLate):
    if daysLate < 1:
        return value
    else:
        return value + (value * 0.03) + (value * 0.001 * daysLate)

def main():
    valor = float(input())
    dias = int(input())
    print(valorPagamento(valor,dias))
main()