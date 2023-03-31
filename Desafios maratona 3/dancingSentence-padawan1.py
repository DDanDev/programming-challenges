while True:
    try: inp = input()
    except: break
    upper = True;out = ""
    for char in inp:
        out += char.upper() if upper else char.lower()
        if char != " ": upper = not(upper)
    print(out)
# while True:
#     try: inp = input()
#     except: break
#     upper = True;out = ""
#     for char in inp:
#         if upper: out += char.upper()
#         else: out += char.lower()
#         if char != " ": upper = not(upper)
#     print(out)
