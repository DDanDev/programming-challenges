# def main():
monthly = float(input())

if monthly <= 2000:
    print("Isento")
elif monthly <= 3000:
    print(f"R$ {((monthly-2000)*0.08):.2f}")
elif monthly <= 4500:
    print(f"R$ {(((monthly-3000)*0.18)+80):.2f}")
else:
    print(f"R$ {(((monthly-4500)*0.28)+350):.2f}")


# main()


# def main():
#     monthly = float(input())

#     ranges = [0, 2000, 3000, 4500]
#     taxes = [0, 0.08, 0.18, 0.28]

#     if monthly <= ranges[1]:
#         print("Isento")
#     else:
#         totaltax = 0
#         index = 0
#         for tax in taxes:
#             if monthly == 0:
#                 break
#             try:
#                 base = min(monthly, ranges[index + 1] - ranges[index])
#             except:
#                 base = monthly
#             totaltax += base * tax
#             monthly -= base
#             index += 1
#         print(f"R$ {totaltax:.2f}")


# main()
