#3. Write a function that takes two objects as parameters and returns
#True if they are the same object, and False if not.

class Horse:
    def __init__(self):
        self.name = 'Unicorn'

uni = Horse()
same_uni = uni
print(uni is same_uni)

another_uni = Horse()
print(uni is another_uni)



def compare(obj1, obj2):
    return obj1 is obj2

print(compare("a","b"))




def test_this(obj3, obj4):
    return obj3 is obj4

print(test_this("cat","cat"))


def test_again(obj5, obj6):
    return obj5 == obj6

print(test_again("horse","potato"))
