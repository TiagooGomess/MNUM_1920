import math

def f(x):
    return 1 + math.sqrt(1 + (1.5*math.exp(1.5*x))**2)

def RegraDosTrapezios(n, a, b, h):
    total = f(a) + f(b)
    
    for i in range(1, int(n)):
        total += 2 * f(a + i * h)

    total *= h/2
    
    return total

n = 4
a = 0
b = 1
h = (b - a) / n




print(RegraDosTrapezios(n, a, b, h))
    

    