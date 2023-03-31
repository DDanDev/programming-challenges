somevar = "something"
def someFunction(args):
    # global somevar #global tag to declare variable with global scope inside function 
    print(somevar) #error: inside the fn, because of line below, "somevar" is a local variable which doesn't have a value yet
    # somevar = "else"
someFunction("")
print(somevar) #error: 



while True:
    num = int(input())
    if 2 <= num <= 10: # multiple comparison operators work in sequence as if it was an AND for each pair
        print("entre 2 e 10, incluso")