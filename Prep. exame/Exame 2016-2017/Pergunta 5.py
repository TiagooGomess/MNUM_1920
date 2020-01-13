def dz(y,t,z):
    return 0.5 + t**2 + t*z

h = 0.25
t = 0
y = 0
z = 1

print("\nMétodo de Euler:\n")

for i in range(3):
    print("Iteração:",i)
    print("t:",t)
    print("y:",y)
    deltaZ = dz(y,t,z)
    t += h
    y += h*z
    z += h * deltaZ
    print("---------")
    
h = 0.25
t = 0
y = 0
z = 1

print("\n\nMétodo Kunge-Katta de 4ª ordem:\n")

for i in range(3):
    print("Iteração:",i)
    print("t:",t)
    print("y:",y)
    z1 = h*z
    dz1 = h*dz(y,t,z)
    
    z2 = h*(z+dz1/2)
    dz2 = h*dz(y,t+h/2,z+dz1/2)
    
    z3 = h*(z+dz2/2)
    dz3 = h*dz(y,t+h/2,z+dz2/2)
    
    z4 = h*(z+dz3)
    dz4 = h*dz(y,t+h,z+dz3)
    
    y += z1/6 + z2/3 + z3/3 + z4/6
    z += dz1/6 + dz2/3 + dz3/3 + dz4/6
    t += h
    print("---------")