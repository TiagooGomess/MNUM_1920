
def w(x,y):
    return -1.7*x*y + 12*y + 7*x**2 -8*x

def dw_dx(x,y):
    return -1.7*y + 14*x -8

def dw_dy(x,y):
    return -1.7*x + 12

def gradiente(x,y,h,n):
    for i in range(n):
        xn = x - h * dw_dx(x,y)
        yn = y - h * dw_dy(x,y)
        
        if (w(xn,yn) > w(x,y)):
            h /= 2
        else:
            x = xn
            y = yn
            h *= 2
            
        print("Result:",w(xn,yn))
        
gradiente(2.4,4.3,0.1,1)