from math import cos,sin,sqrt

def f(x):
    return 5*cos(x) - sin(x)

def aurea_minimo(x1,x2):
    B = (sqrt(5)-1)/2
    A = B**2
    x3 = x1 + A*(x2-x1)
    x4 = x1 + B*(x2-x1)
    
    print("x1:",x1)
    print("x2:",x2)
    print("x3:",x3)
    print("x4:",x4)
    print("f(x1):",f(x1))
    print("f(x2):",f(x2))
    print("f(x3):",f(x3))
    print("f(x4):",f(x4))
    print("\n-----------\n")
    
    for i in range(2):
        
        if (f(x3) < f(x4)):
            x2 = x4
            x4 = x3
            x3 = x1 + A*(x2-x1)
        else:
            x1 = x3
            x3 = x4
            x4 = x1 + B*(x2-x1)
        
        print("x1:",x1)
        print("x2:",x2)
        print("x3:",x3)
        print("x4:",x4)
        print("f(x1):",f(x1))
        print("f(x2):",f(x2))
        print("f(x3):",f(x3))
        print("f(x4):",f(x4))
        print("\n-----------\n")
    
    amplitude = x4 - x1
    print("\nAmplitude:",amplitude)
        
aurea_minimo(2,4)

