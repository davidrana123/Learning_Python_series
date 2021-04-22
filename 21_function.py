# a = (1,3)
# b = 4
# x = sum(a,b)
# print(x)

def function1():
    print("Hellow i am david singh rana")
function1()

def david(a,b):
    print("i am david ",a+b)

david(2,5)

def function3(a, b):
    average = (a+b)/2
    # print(aerage)
    return average
v  = function3(2, 5)
print(v)

def function5(a, b):
    """this is function of adding num"""
    add = a+b
    return add
# v = function5(2,5)
# print(v)
print(function5.__doc__)
print(function5(3,4))
