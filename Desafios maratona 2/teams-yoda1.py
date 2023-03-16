# 3 (works, better?) iterates 2x over nOfPlayers, 1x over nOfTeams, 1x over finished team.
# 1 less lambda sort
def main():
    nOfPlayers, nOfTeams = [int(x) for x in input().split()]

    players = []
    for i in range(nOfPlayers):
        players.append(input().split())

    players.sort(key=(lambda x: int(x[1])), reverse=True)

    for teamN in range(nOfTeams):
        print(f"Time {teamN+1}")
        team = []
        i = 0
        while True:
            try:
                team.append(players[(nOfTeams * i) + teamN][0])
                i += 1
            except:
                break
        team.sort()
        for player in team:
            print(player)
        print()


main()

# 2 (works, better) iterates 2x over nOfPlayers, 1x over nOfTeams, 1x over finished team.
# nOfPlayers, nOfTeams = [int(x) for x in input().split()]

# players = []
# for i in range(nOfPlayers):
#     players.append(input().split())

# players.sort(key=(lambda player: int(player[1])), reverse=True)

# teams = []

# choosingTeam = 0
# for i in range(nOfPlayers):
#     try:
#         teams[choosingTeam]
#     except:
#         teams.append([])
#     teams[choosingTeam].append(players.pop(0))
#     choosingTeam = (choosingTeam + 1) if choosingTeam < (nOfTeams - 1) else 0


# for teamN in range(nOfTeams):
#     teams[teamN].sort(key=(lambda player: player[0]))
#     print(f"Time {teamN+1}")
#     for player in teams[teamN]:
#         print(player[0])
#     print()

# 1 (accepted)
# nOfPlayers, nOfTeams = [int(x) for x in input().split()]

# players = []
# for i in range(nOfPlayers):
#     players.append(input().split())

# players.sort(key=(lambda player: int(player[1])), reverse=True)

# teams = []
# for i in range(nOfTeams):
#     teams.append([])

# choosingTeam = 0
# for i in range(nOfPlayers):
#     teams[choosingTeam].append(players.pop(0))
#     choosingTeam = (choosingTeam + 1) if choosingTeam < (nOfTeams -1) else 0


# for teamN in range(nOfTeams):
#     teams[teamN].sort(key=(lambda player: player[0]))
#     print(f"Time {teamN+1}")
#     for player in teams[teamN]:
#         print(player[0])
#     print()

# felipe 4
# alvaro 8
# thiago 1
# rodrigo 3
# robson 2
# fabio 9
# ricardo 11
# rodolfo 0
# andre 14
# arthur 12
# ronaldo 55
# rogerio 30
# lucas 7
# rafael 17
