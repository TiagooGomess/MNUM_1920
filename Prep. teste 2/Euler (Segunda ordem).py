
def dz(t, z):
    return 2 + t**2 + t*z

h = 0.25
t = 1
y = 1
z = 0

print("\nEULER:\n")

for i in range(3):
    print("Iteração:", i)
    print("t:", t)
    print("y:", y)
    deltaZ = dz(t, z)
    t += h
    y += h * z
    z += h * deltaZ
    print("--------------")
    