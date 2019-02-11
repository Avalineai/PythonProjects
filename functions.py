def f(x):
    return x**2
x = f(3)
print(x)

def test(string):
    print(string)

test("Not sure 123")



def add_all(a,b,c,d=200,e=2000):
    return a + b + c * d * e

result = add_all(1,2,3)
print(result)



def divide(x):
    return x / 2

def multiply(x):
    return x * 4

y = divide(4)
z = multiply(y)

print(z)




def convert(string):
    try:
        return float(string)
    except ValueError:
        print("not possible")

c = convert("55.0")
print(c)








def squared(x):
    """ Takes int and returns it squared.
    :param x: int.
    :return: x squared.
    """

    return x**2

def print_string(string):
    """ Prints the string passed in.
    :param string: str.
    """
    print(string)

print_string("this is a test")

def add_all(a,b,c,d=200,e=2000):
    """ returns the result of two optional params
    multiplied by the addition of 3 required params
    :param a: int.
    :param b: int.
    :param c: int.
    :param d: int.
    :param e: int.
    :return: int.
    """
    return a + b + c * d * e
print(result)


def convert(string):
    """Converts passed in str to int.
    :param string: str.
    :return: string converted to int.
    """
    try:
        return float(string)
    except ValueError:
        print("could not")
