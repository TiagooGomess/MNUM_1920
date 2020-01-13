from math import log

def g(x):
    return 2*log(2*x)

x = 0.9

for i in range(50):
    print(x)
    x = g(x)