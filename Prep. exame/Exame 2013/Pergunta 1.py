A = 0.5

def dz(t,z):
    return A + t**2 + t*z

def Euler(z,t,y,h):
    for i in range(3):
        print("Itr:",i)
        print("t:",t)
        print("y:",y)
        deltaZ = dz(t,z)
        t += h
        y += h * z
        z += h * deltaZ
        print("--------")
        
z = 1
t = 0
y = 0
h = 0.25

print("\n-------- Euler --------\n")
Euler(z,t,y,h)


def RK4(z,t,y,h):
    for i in range(3):
        print("Itr:",i)
        print("t:",t)
        print("y:",y)
        z1 = h*z
        dz1 = h*dz(t,z)
        
        z2 = h*(z + dz1/2)
        dz2 = h*dz(t + h/2, z + dz1/2)
        
        z3 = h*(z + dz2/2)
        dz3 = h*dz(t + h/2, z + dz2/2)
        
        z4 = h*(z + dz3)
        dz4 = h*dz(t + h, z + dz3)
        
        z += 1/6*dz1 + 1/3*dz2 + 1/3*dz3 + 1/6*dz4
        y += 1/6*z1 + 1/3*z2 + 1/3*z3 + 1/6*z4
        t += h
        print("--------")
        
z = 1
t = 0
y = 0
h = 0.25

print("\n-------- RK4 --------\n")
RK4(z,t,y,h)