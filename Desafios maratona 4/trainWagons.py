while True:
    size = int(input())
    if size == 0: break
    while True:
        reordered = [int(x) for x in input().split()]
        if reordered == [0]: 
            print()
            break
        incoming = [x+1 for x in list(range(size))]
        station = []
        broke = False
        for wagon in reordered:
            if len(incoming) > 0:
                if wagon == incoming[0]:
                    incoming.pop(0)
                    continue
            if len(station) > 0:
                if wagon == station[-1]:
                    station.pop(-1)
                    continue
            if len(incoming) > 0:
                if wagon > incoming[0]:
                    for i in range(wagon-incoming[0]):
                        station += [incoming.pop(0)]
                    incoming.pop(0)
                    continue
            broke = True
            break
        if broke: print("No")
        else: print("Yes")






# while True:
#     size = int(input())
#     if size == 0: break
#     while True:
#         reordered = [int(x) for x in input().split()]
#         if reordered == [0]: 
#             print()
#             break
#         expected = 1
#         owe = 0
#         broke = False
#         for wagon in reordered:
#             if owe > 0:
#                 if wagon == expected: 
#                     owe -= 1
#                     expected -= 1
#                     if owe == 0: expected = detour
#                     continue
#                 if wagon > expected:
#                     if wagon == detour: detour += 1; continue
#                     if wagon > detour: pass #refactor owe expected and detour into arrays to be able to keep track of multiple "owes"
#                 broke = True
#                 print("No")
#                 break
#             else:
#                 if wagon == expected:
#                     expected += 1
#                     continue
#                 owe = wagon - expected
#                 expected = wagon - 1
#                 detour = wagon + 1
#         if broke: continue
#         print("Yes")