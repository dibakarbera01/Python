def add(a,b):  # a an b parameters
    x = a+b
    return x

c = add(3,5) # arguments
print(c)



def add(a,b, plus =0):  # a an b parameters
    x = a+b+plus
    return x

c = add(3,5,1) # arguments
print(c)

c1=add(b=5, a=2)
print(c1)