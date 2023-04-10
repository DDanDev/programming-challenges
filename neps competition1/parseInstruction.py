#v3 numbers are the most common character so deal with them first.
sequence = input()
instructions = [["","",""]]
currInst = 0
for char in sequence:
    try: instructions[currInst][2] += str(int(char))
    except:
        if char == "+": instructions[currInst][1] = "tighten"
        elif char == "-": instructions[currInst][1] = "loosen"
        else:
            if instructions[currInst][2] != "":
                currInst += 1
                instructions.append(["","",""])
            instructions[currInst][0] += char

for instruction in instructions:
    print(" ".join(instruction))


#v2 no need for boolean, no need for the second try either
# sequence = input()
# instructions = [["","",""]]
# currInst = 0
# for char in sequence:
#     if char == "+": instructions[currInst][1] = "tighten"
#     elif char == "-": instructions[currInst][1] = "loosen"
#     else:
#         try: instructions[currInst][2] += str(int(char))
#         except:
#             if instructions[currInst][2] != "":
#                 currInst += 1
#                 instructions.append(["","",""])
#             instructions[currInst][0] += char

# for instruction in instructions:
#     print(" ".join(instruction))
    

#v1
# sequence = input()
# instructions = []
# currInst = -1
# loadingNumbers = False
# for char in sequence:
#     if char == "+": instructions[currInst][1] = "tighten"
#     elif char == "-": instructions[currInst][1] = "loosen"
#     else:
#         try:
#             instructions[currInst][2] += str(int(char))
#             loadingNumbers = True
#         except:
#             try:
#                 if loadingNumbers: raise
#                 instructions[currInst][0] += char
#             except:
#                 currInst += 1
#                 loadingNumbers = False
#                 instructions.append(["","",""])
#                 instructions[currInst][0] += char

# for instruction in instructions:
#     print(" ".join(instruction))