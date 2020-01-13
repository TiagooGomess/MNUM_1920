from math import cos,sin

def f(x):
    return (cos(x+1.1))**3 + x - 2.6

def df_dx(x):
    return 1 - 3*cos(x+1.1)**2*sin(x+1.1)

x = 1.8

for i in range(1):
    x -= f(x)/df_dx(x)
    print("x:",x)