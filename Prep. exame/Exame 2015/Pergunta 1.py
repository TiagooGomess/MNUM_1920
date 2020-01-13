
def dT_dt(T, t):
    return -0.25 * (T - 37)

def Euler(T, t, h, itr):
    T1 = T
    t1 = t
    for i in range(itr):
        T = T1
        t = t1
        T1 = T + h * dT_dt(T, t)
        t1 = t + h
        print("\nItr:",itr)
        print("T:",T1)
        print("t:",t1)
        print("-------------")
        
T = 3
t = 5
h = 0.4
itr = 2

Euler(T,h,h,itr)