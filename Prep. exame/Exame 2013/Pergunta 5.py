from math import cos,sin

def f(x):
    return (x-3.7) + (cos(x+1.2))**3

def df(x):
    return 1 - 3*cos(x+1.2)**2*sin(x+1.2)

x = 3.8

for i in range(1):
    x -= f(x)/df(x)
    print("x:",x)