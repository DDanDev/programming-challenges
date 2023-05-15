nOfCases = int(input())

allInput = []
while True:
    try:
        allInput += [int(x) for x in input().split()]
    except:
        break

try:
    for caseN in range(nOfCases):
        nOfYogurts = allInput.pop(0)
        volumeLimit = allInput.pop(0)
        yogurts = [[0.0, 0]]*nOfYogurts
        for i in range(nOfYogurts):
            new = [allInput.pop(0), allInput.pop(0)]
            yogurts[i] = [new[0] / new[1], new[1]]
        yogurts.sort(key=lambda x: x[0] , reverse=True)
        
        filled = 0
        value = 0
        while filled < volumeLimit:
            if not yogurts: break
            fill = min(yogurts[0][1], volumeLimit - filled)
            filled += fill
            value += fill * yogurts[0][0]
            del yogurts[0]
        print(f"{value:.2f}")
except:
    raise Exception(f"nOfCases: {nOfCases} | caseN: {caseN} | nOfYogurts: {nOfYogurts} | volumeLimit: {volumeLimit} | yogurts: {yogurts} | i: {i} | new: {new} | len(new): {len(new)} | filled: {filled} | value: {value} | allInput: {allInput}")