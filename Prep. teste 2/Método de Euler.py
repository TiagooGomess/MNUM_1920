# Para duas variaveis

#import math
#
#def C_l(T, C):
#    return -math.exp(-0.5/(T + 273)) * C
#
#def T_l(T, C):
#    return 20 * math.exp(-0.5/(T + 273)) * C - 0.5 * (T - 20)
#
#def Euler(xn, yn, h, itr):
#    xn1 = xn
#    yn1 = yn
#    for i in range(itr):
#        xn = xn1
#        yn = yn1
#        xn1 = xn + h * T_l(xn, yn)
#        yn1 = yn + h * C_l(xn, yn)
#        print("\nT: {}".format(xn1))
#        print("C: {}\n".format(yn1))
#        print("-----------------------------------")
#        
#Euler(20, 2, 0.2, 2)



# Para uma variavel

def dT_dt(T):
    return -0.25 * (T - 42)

def Euler(xn, yn, h, itr):
    xn1 = xn
    yn1 = yn
    for i in range(itr):
        xn = xn1
        yn = yn1
        xn1 = xn + h
        yn1 = yn + h * dT_dt(yn)
        print("\nt: {}".format(xn1))
        print("T: {}\n".format(yn1))
        print("-----------------------------------")

Euler(5, 10, 0.4, 2)
