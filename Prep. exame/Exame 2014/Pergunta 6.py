from math import sin,sqrt

def f(x):
    return x + (x-2)**2/(sin(x)+4)

def aurea_minimo(x1,x2):
    B = (sqrt(5)-1)/2
    A = B**2
    x3 = -0.045080
    x4 = 0.545085
    
    for i in range(2):
        if (f(x3) < f(x4)):
            x2 = x4
            x4 = x3
            x3 = x1 + A * (x2 - x1)
        else:
            x1 = x3
            x3 = x4
            x4 = x1 + B * (x2 - x1)
            
        print("Itr:",i+1)
        print("X1:",x1)
        print("X2:",x2)
        print("X3:",x3)
        print("X4:",x4)
        print("f(x1):",f(x1))
        print("f(x2):",f(x2))
        print("f(x3):",f(x3))
        print("f(x4):",f(x4))
        print("--------------------------")
    
    amplitude = x4 - x1
    print("\nAMPLITUDE:",amplitude)
    print()
    
    
x1 = -1
x2 = 1.5

aurea_minimo(x1,x2)