def Z(x,y):
    return 6*x**2 - x*y + 12*y + y**2 - 8*x

def dZ_dx(x,y):
    return -y +12*x -8

def dZ_dy(x,y):
    return 2*y -x +12

def gradiente(x,y,h):
    print("Itr:",0)
    print("x:",x)
    print("y:",y)
    print("Z(x,y):",Z(x,y))
    print("dZ_dx(x,y):",dZ_dx(x,y))
    print("dZ_dy(x,y):",dZ_dy(x,y))
    print("-------------")
    for i in range(1):
        xn = x - h * dZ_dx(x,y)
        yn = y - h * dZ_dy(x,y)
        
        if (Z(xn,yn) > Z(x,y)):
            h /= 2
        else:
            x = xn
            y = yn
            h *= 2
        print("Itr:",i+1)
        print("x:",xn)
        print("y:",yn)
        print("Z(x,y):",Z(xn,yn))
        print("dZ_dx(x,y):",dZ_dx(xn,yn))
        print("dZ_dy(x,y):",dZ_dy(xn,yn))
        print("-------------")
        
gradiente(0,0,0.25)