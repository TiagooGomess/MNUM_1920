
def dy_dt(t,y):
    return y / (t - 1)

def Euler(t,y,h):
    for i in range(3):
        print("Itr:",i)
        print("t:",t)
        print("y:",y)
        print("------------")
        y += h * dy_dt(t,y) 
        t += h
        
h = 0.25
t = 2
y = 2

print("\n----- EULER -----\n")
Euler(t,y,h)

def RK4(t,y,h):
    for i in range(3):
        print("Itr:",i)
        print("t:",t)
        print("y:",y)
        print("------------")
        d1 = h * dy_dt(t,y)
        d2 = h * dy_dt(t+h/2,y+d1/2)
        d3 = h * dy_dt(t+h/2,y+d2/2)
        d4 = h * dy_dt(t+h,y+d3)
        y += d1/6 + d2/3 + d3/3 + d4/6
        t += h


h = 0.25
t = 2
y = 2

print("\n----- RK4 -----\n")
RK4(t,y,h)