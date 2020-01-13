from math import sqrt

def f(x):
    return 2**sqrt(x) - 10*x + 1

a = 0 # limite inferior
b = 1 #limite superior

e = 0.0000000001 #precisão

it = 0 # número de iterações

xn = (a * f(b) - b * f(a)) / (f(b) - f(a))
xn_1 = xn + 99999999

while (abs(xn_1 - xn) > e):
    if (f(a) * f(xn) < 0):
        b = xn
    else:
        a = xn
    xn_1 = xn
    xn = (a*f(b) - b*f(a)) / (f(b) - f(a))
    
    it += 1
    
print("a: {}\nb: {}\nit: {}\n".format(a, b, it))