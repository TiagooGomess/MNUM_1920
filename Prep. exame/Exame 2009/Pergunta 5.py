from math import sin

def dx_dt(t,x):
    return sin(x) + sin(2*t)

def RK4(t,x,h,n):
    for i in range(n):
        d1 = h * dx_dt(t,x)
        d2 = h * dx_dt(t+h/2,x+d1/2)
        d3 = h * dx_dt(t+h/2,x+d2/2)
        d4 = h * dx_dt(t+h,x+d3)
        x += d1/6 + d2/3 + d3/3 + d4/6
        t += h
        print("Itr:",i+1)
        print("t:",t)
        print("x:",x)
        print("----------")
        
RK4(1,1,0.125,4)

QC = (1.768150-1.767816) / (1.768184-1.768150)

print("\nQC:",QC)