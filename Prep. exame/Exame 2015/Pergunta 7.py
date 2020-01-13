from math import sin

def f(x):
    return x**3 - 10*sin(x) + 2.8

a = 1.5
b = 4.2

for i in range(3):
    m = (a + b)/2
    
    if (f(a)*f(m) < 0):
        b = m
    else:
        a = m
        
    print("\nItr:",i+1)
    print("a:",a)
    print("b:",b)
    print("\n--------")