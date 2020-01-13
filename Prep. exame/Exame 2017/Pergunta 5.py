
def w(x,y):
    return -1.1*x*y + 12*y + 7*x**2 - 8*x

def dw_dx(x,y):
    return -1.1*y +14*x - 8

def dw_dy(x,y):
    return -1.1*x + 12

def gradiente(x,y,h):
    for i in range(1):
        xn = x - h*dw_dx(x,y)
        yn = y - h*dw_dy(x,y)
        
        if (w(xn,yn) > w(x,y)):
            h /= 2
        else:
            x = xn
            y = yn
            h *= 2
        
        print("Result:",w(xn,yn))
        
gradiente(3,1,0.1)