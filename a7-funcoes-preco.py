def main():
    oldValue = float(input())
    newValue = atualiza_preco(oldValue)
    fee = taxa(newValue)
    print(f"{newValue:.2f}")
    print(f"{fee:.2f}")

def atualiza_preco(value):
    return value * 1.1

def taxa(value):
    return value * 0.025

main()