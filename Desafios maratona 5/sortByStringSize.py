for _ in range(int(input())): print(" ".join(sorted(input().split(),key=lambda x: len(x),reverse=True)))
# for _ in range(int(input())):
#     strings = [[len(x),x] for x in input().split()]
#     ordered = [strings.pop(0)]
    
#     for _ in range(len(strings)):
#         toInsert = strings.pop(0)
#         i = -1
#         inserted = False
#         for item in ordered:
#             i += 1
#             if toInsert[0] > item[0]: ordered.insert(i,toInsert); inserted = True; break
#         if not inserted: ordered.append(toInsert)
    
#     print(" ".join([x[1] for x in ordered]))