def f(x=2):
    return x**x
x= f()
print(x)


def squared(b):
    return b**2
print(squared(5))



def test_talk(string):
    print(string)

test_talk("testing: where am I?")



def add_mult (c,d,e,y=200,z=2000):
    return c+d+e*y*z
result = add_mult(10,15,25)
print(result)




def divide(p):
    return p / 2

def multiply(p):
    return p * 4

q = divide(9)

r = multiply(q)

print(r)
