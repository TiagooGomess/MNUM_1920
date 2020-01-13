
def dz(t, z):
    return 1.5 + t**2 + t*z

def RK4(t, y, z, h):
    for i in range(3):
        print("Iteração:", i)
        print("t:", t)
        print("y:", y)
        print("--------")
        z1 = h*z
        dz1 = h*dz(t,z)
        
        z2 = h*(z + dz1/2)
        dz2 = h*dz(t + h/2, z + dz1/2)
        
        z3 = h*(z + dz2/2)
        dz3 = h*dz(t + h/2, z + dz2/2)
        
        z4 = h*(z + dz3)
        dz4 = h*dz(t + h, z + dz3)
        
        y += z1/6 + z2/3 + z3/3 + z4/6
        z += dz1/6 + dz2/3 + dz3/3 + dz4/6
        t += h
        
h = 0.2
t = 1
y = 0
z = 1

RK4(t, y, z, h)
    