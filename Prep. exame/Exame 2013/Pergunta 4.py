from math import exp

def f(x):
    return exp(1.5*x)

def Simpson(a,b,h,n):
    total = f(a) + f(b)
    
    for i in range(1,n,2):
        total += 4 * f(a + i*h)
        
    for i in range(2,n-1,2):
        total += 2 * f(a + i*h)
        
    total *= h/3
    
    return total

a = 1
b = 1.5
h = 0.125
n = int((b-a)/h)
S = Simpson(a,b,h,n)

h /= 2
n = int((b-a)/h)
S_l = Simpson(a,b,h,n)

h /= 2
n = int((b-a)/h)
S_ll = Simpson(a,b,h,n)

QC = (S_l - S) / (S_ll - S_l)
erro = (S_ll - S_l) / 15

print("S:",S)
print("S':",S_l)
print("S'':",S_ll)
print("QC:",QC)
print("Erro:",erro)