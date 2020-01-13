
def f1(x,y):
    return x**2 - y - 2

def f2(x,y):
    return -x + y**2 - 2

def df1_dx(x,y):
    return 2*x

def df1_dy(x,y):
    return -1

def df2_dx(x,y):
    return -1

def df2_dy(x,y):
    return 2*y

x = 1.5
y = 0.8

for i in range(2):
    x1 = x - (f1(x,y)*df2_dy(x,y)-f2(x,y)*df1_dy(x,y)) / (df1_dx(x,y)*df2_dy(x,y)-df2_dx(x,y)*df1_dy(x,y))
    y1 = y - (f2(x,y)*df1_dx(x,y)-f1(x,y)*df2_dx(x,y)) / (df1_dx(x,y)*df2_dy(x,y)-df2_dx(x,y)*df1_dy(x,y))
    x = x1
    y = y1
    print("x:",x)
    print("y:",y)
    print("---------")
    