from math import sqrt
from math import exp

def f(x):
    return sqrt(1 + (2.5*exp(2.5*x))**2)

def Trapezios(a, b, h, n):
    total = f(a) + f(b)
    
    for i in range(1, n):
        total += 2 * f(a + i*h)
        
    total *= h/2
    
    return total

a = 0
b = 1
h = 0.125
n = int((b-a)/h)

T = Trapezios(a,b,h,n)

h /= 2
n = int((b-a)/h)
T_l = Trapezios(a,b,h,n)    

h /= 2
n = int((b-a)/h)
T_ll = Trapezios(a,b,h,n) 

QC = (T_l - T) / (T_ll - T_l)
erro = (T_ll - T_l) / 3

print("\nMétodo dos Trapézios:\n")
print("T:",T)
print("T':",T_l)
print("T'':",T_ll)
print("QC:",QC)
print("Erro:",erro)

print("\n---------------------\n")

def Simpson(a, b, h, n):
    total = f(a) + f(b)
    
    for i in range(1, n, 2):
        total += 4 * f(a + h*i)
        
    for i in range(2, n-1, 2):
        total += 2 * f(a + h*i)
        
    total *= h/3
    
    return total

a = 0
b = 1
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

print("\nMétodo de Simpson:\n")
print("T:",S)
print("T':",S_l)
print("T'':",S_ll)
print("QC:",QC)
print("Erro:",erro)
