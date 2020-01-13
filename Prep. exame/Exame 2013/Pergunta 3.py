def Z(x,y):
    return 3*x**2 - x*y + 11*y + y**2 -8*x

def dZ_dx(x,y):
    return 6*x - y -8

def dZ_dy(x,y):
    return -x + 11 + 2*y


def gradiente(x,y,h,itr):
    print("xn:",x)
    print("yn:",y)
    print("dZ_dx(xn,yn):",dZ_dx(x,y))
    print("dZ_dy(xn,yn):",dZ_dy(x,y))
    print("Z(xn,yn):",Z(x,y))
    for i in range(itr):
        xn = x - h * dZ_dx(x,y)
        yn = y - h * dZ_dy(x,y)
        
        if (Z(xn,yn) > Z(x,y)):
            h /= 2
        else:
            x = xn
            y = yn
            h *= 2
        
        print("--------")
        print("xn:",xn)
        print("yn:",yn)
        print("dZ_dx(xn,yn):",dZ_dx(xn,yn))
        print("dZ_dy(xn,yn):",dZ_dy(xn,yn))
        print("Z(xn,yn):",Z(xn,yn))
        

x = 2
y = 2
h = 0.5
itr = 1
gradiente(x,y,h,itr)    