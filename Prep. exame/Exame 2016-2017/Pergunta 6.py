from math import sqrt
from math import exp

def f(x):
    return sqrt(1 + (1.5*exp(1.5*x))**2)

def Trapezios(a,b,h,n):
    total = f(a) + f(b)
    
    for i in range(1,n):
        total += 2 * f(a + h*i)
    
    total *= h/2
    
    return total

a = 0
b = 2
h = 0.5
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

print("\nRegra dos Trapézios:\n\nT: {}\nT': {}\nT'': {}\nQC: {}\nErro: {}\n".format(T,T_l,T_ll,QC,erro))



def Simpson(a,b,h,n):
    total = f(a) + f(b)
    
    for i in range(1, n,2):
        total += 4 * f(a + i*h)
        
    for i in range(2,n-1,2):
        total += 2 * f(a + i*h)
        
    total *= h/3
    
    return total

a = 0
b = 2
h = 0.5
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

print("\n----------------------------\n")
print("\nMétodo de Simpson:\n\nS: {}\nS': {}\nS'': {}\nQC: {}\nErro: {}\n".format(S,S_l,S_ll,QC,erro))

