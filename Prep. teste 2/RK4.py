import math

def dx_dt(t,x):
    return math.sin(2*x) + math.sin(2*t)

def RK4(x, t, h, itr):
    x1 = x
    t1 = t
    for i in range(itr):
        xn = x1
        tn = t1
        
        print("\nItr:",i)
        print("x:",xn)
        print("t:",tn)
        print("-----------")
        
        d1 = h * dx_dt(tn, xn)
        d2 = h * dx_dt(tn + h/2, xn + d1/2)
        d3 = h * dx_dt(tn + h/2, xn + d2/2)
        d4 = h * dx_dt(tn + h, xn + d3)
        
        x1 = xn + d1/6 + d2/3 + d3/3 + d4/6
        t1 = tn + h
     
x = 1
t = 1
h = 0.125
itr = 5
  
RK4(x, t, h, itr)