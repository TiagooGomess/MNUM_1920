from math import log

def g(x):
    return 2 * log(2*x)

x = 1.1
print("X:",x)

for i in range(1):
    x = g(x)
    print("X:",x)
    
print("Resíduo ????????")
    
