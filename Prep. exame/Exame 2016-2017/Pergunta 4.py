def f(x):
    return x**7 + 0.5*x - 0.5

xe = 0  # f(xe) = -0.5 
xd = 0.8  # f(xd) = 0.109715
xn = 0.656044  # f(xn) = -0.119674

xn = (xe*f(xd) - xd*f(xe))/(f(xd)-f(xe))
xn_1 = xn

for i in range(3):
    if (f(xe)*f(xn) < 0):
        xd = xn
    else:
        xe = xn
    xn_1 = xn
    xn = (xe*f(xd) - xd*f(xe))/(f(xd)-f(xe))
    print("xe: {}\nxd: {}\nxn: {}\n\n".format(xe,xd,xn))    
    
    