from math import sin

def f(t,x):
    return sin(x) + sin(2*t)

def RK4(t,x,h,n):
    for i in range(n):
        d1 = h * f(t,x)
        d2 = h * f(t + h/2, x + d1/2)
        d3 = h * f(t + h/2, x + d2/2)
        d4 = h * f(t + h, x + d3)
        t += h
        x += d1/6 + d2/3 + d3/3 + d4/6
        print("Itr:",i+1)
        print("t:",t)
        print("x:",x)
        print("-----------")
    return x
        
t = 1
x = 0
h = 0.125
n = 4

S = RK4(t,x,h,n)

QC = (0.391503 - 0.391238) / (0.391517 - 0.391503)

print("\nQC:",QC)

