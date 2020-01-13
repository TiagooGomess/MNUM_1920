def f1(x,y):
    return x**2 - y - 1.2

def f2(x,y):
    return -x + y**2 - 1

def df1_x(x,y):
    return 2*x

def df1_y(x,y):
    return -1

def df2_x(x,y):
    return -1

def df2_y(x,y):
    return 2*y

xn = 1
yn = 1

for i in range(2):
    xn_1 = xn - (f1(xn,yn)*df2_y(xn,yn)-f2(xn,yn)*df1_y(xn,yn)) / (df1_x(xn,yn)*df2_y(xn,yn)-df2_x(xn,yn)*df1_y(xn,yn))
    yn_1 = yn - (f2(xn,yn)*df1_x(xn,yn)-f1(xn,yn)*df2_x(xn,yn)) / (df1_x(xn,yn)*df2_y(xn,yn)-df2_x(xn,yn)*df1_y(xn,yn))
    print("xn: {}\nyn: {}\n\n".format(xn_1,yn_1))
    xn = xn_1
    yn = yn_1