import math

def f(x):
    return math.exp(1.5*x)

def MetodoDeSimpson(n, a, b, h):
    total = f(a) + f(b)
    
    for i in range(1, n, 2):
        total += 4 * f(a + i * h)
        
    for i in range(2, n-1, 2):
        total += 2 * f(a + i * h)
        
    total *= h/3
    
    return total

n = 4
a = 2
b = 2
h = (b - a) / n


print(MetodoDeSimpson(n, a, b, h))