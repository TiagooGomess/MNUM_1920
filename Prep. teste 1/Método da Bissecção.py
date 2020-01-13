from math import sqrt

def f(x):
    return 2**sqrt(x) - 10*x + 1

a = 0 # limite inferior
b = 1 #limite superior

e = 0.0000000001 #precisão

it = 0 # número de iterações

while(abs(a - b) > e):
    x = (a + b) / 2
    if f(x) * f(a) < 0:
        b = x
    else:
        a = x
    it += 1;

print("a: {}\nb: {}\nit: {}\n".format(a, b, it))