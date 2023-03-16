# sides = list(map(lambda n: float(n), input().split())).sort().reverse()
sides = list(map(lambda n: float(n), input().split()))
sides.sort()

if (sides[2] >= (sides[1] + sides[0])):
    print("NAO FORMA TRIANGULO")
else:
    if ((sides[2]**2) == ((sides[1]**2) + (sides[0]**2))):
        print("TRIANGULO RETANGULO")
    if ((sides[2]**2) > ((sides[1]**2) + (sides[0]**2))):
        print("TRIANGULO OBTUSANGULO")
    if ((sides[2]**2) < ((sides[1]**2) + (sides[0]**2))):
        print("TRIANGULO ACUTANGULO")
    if (sides[2] == sides[1] == sides[0]):
        print("TRIANGULO EQUILATERO")
    elif (sides[2] == sides[1] or sides[1] == sides[0]):
        print("TRIANGULO ISOSCELES")




# # Return double of n
# def addition(n):
#     return n + n
 
# # We double all numbers using map()
# numbers = (1, 2, 3, 4)
# result = map(addition, numbers)
# print(result)