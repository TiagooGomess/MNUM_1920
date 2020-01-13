def y_l(x,y):
    return x**2 + y**2


def RK2(xn, yn, h):
    xn_1 = xn
    yn_1 = yn
    for i in range(2):
        xn = xn_1
        yn = yn_1
        xn_1 = xn + h
        yn_1 = yn + h * y_l(xn + (h/2), yn + (h/2) * y_l(xn, yn))
        print("\nXn: {}\nYn: {}".format(xn_1, yn_1))
        print("----------------------------")

RK2(0, 0, 0.4)