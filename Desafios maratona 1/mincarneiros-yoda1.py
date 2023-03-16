def it(x):
    try:
        return int(x)
    except:
        return x

def main():
    d = int(input())-1
    r = list(map(it, input().split()))

    n = 0
    w = []
    for i in range(d + 1):
        w.append(False)

    while not((n > d) or (n < 0)):
        c = n
        if r[c] % 2 == 1:
            n += 1
        else:
            n -= 1
        
        if r[c] > 0:
            w[c] = True
            r[c] -= 1

    f = 0
    for q in r:
        f += q
    # stolenDestinations = wasStolenFrom.count(True)
    print(f"{w.count(True)} {f}")
main()