somevar = "something"
def someFunction(args):
    # global somevar
    print(somevar) #error: inside the fn, "somevar" is a local variable which doesn't have a value yet
    # somevar = "else"
someFunction("")
print(somevar) #error: 