# (d^2)y/dt^2 -> z
def dz(t, z): 
    return 1 + t**2 + t*z

def Euler(t, y, z, h, itr):
    t1 = t
    y1 = y
    z1 = z
    for i in range(itr):
        tn = t1
        yn = y1
        zn = z1
        print("----------")
        print("Itr:",i)
        print("t:",tn)
        print("y:",yn)
        print("y':",zn)
        t1 = tn + h
        y1 = yn + h * zn
        z1 = zn + h * dz(tn, zn)


def RK4(t, y, z, h, itr):
    t1 = t
    y1 = y
    z_1 = z
    for i in range(itr):
        tn = t1
        yn = y1
        zn = z_1
        print("----------")
        print("Itr:",i)
        print("t:",tn)
        print("y:",yn)
        print("y':",zn)
        z1 = h * zn
        d1 = h * dz(tn, zn)
        
        z2 = h * (zn + d1/2)
        d2 = h * dz(tn + h/2, zn + d1/2)
        
        z3 = h * (zn + d2/2)
        d3 = h * dz(tn + h/2, zn + d2/2)
        
        z4 = h * (zn + d3)
        d4 = h * dz(tn + h, zn + d3)
        
        z_1 = zn + d1/6 + d2/3 + d3/3 + d4/6
        y1 = yn + z1/6 + z2/3 + z3/3 + z4/6
        t1 = tn + h

t = 0
y = 1
z = 2
h = 0.5
itr = 3

print("\n-------EULER--------")
Euler(t, y, z, h, itr)

print("\n-------RK4--------")
RK4(t, y, z, h, itr)
