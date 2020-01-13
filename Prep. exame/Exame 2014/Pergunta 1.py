def g(x):
    return (4*x**3-x+1)**(1/4)

x = 4

for i in range(1,3):
    x = g(x)
    print("ITR:",i)
    print("x:",x)
    print("\n")