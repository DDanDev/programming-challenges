nPlayers = int(input())
goldenTeam = True
goldPlayers = 0

for _ in range(nPlayers):
    points = (int(input())*5)-(int(input())*3)
    if points <= 40: goldenTeam = False
    else: goldPlayers += 1

print(f'{goldPlayers}{"+" if goldenTeam else ""}')
