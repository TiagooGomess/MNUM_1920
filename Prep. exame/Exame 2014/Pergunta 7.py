from math import sqrt,cos,sin

a = 2
b = 60

def g(x):
    return -x + b*cos(sqrt(x)) + a

def dg(x):
    return - (1 + (30*sin(sqrt(x)))/sqrt(x))

x = 1.8
print("Itr:",0)
print("X:",x)
print("g(x):",g(x))
print("------------")

for i in range(2):
    x -= g(x)/dg(x)
    print("Itr:",i+1)
    print("x:",x)
    print("g(x):",g(x))
    print("------------")