from math import exp

def dC_dt(t, T, C):
    return -exp(-0.5/(T+273))*C

def dT_dt(t, T, C):
    return 30*exp(-0.5/(T+273))*C - 0.5*(T-20)

def Euler(t, T, C, h, n):
    t1 = t
    T1 = T
    C1 = C
    for i in range(n):
        t = t1
        T = T1
        C = C1
        t1 = t + h
        T1 = T + h * dT_dt(t,T,C)
        C1 = C + h * dC_dt(t,T,C)
        
#        print("Itr:",i)
#        print("t:",t)
#        print("T:",T)
#        print("C:",C)
#        print("--------")
    return T
        
        
t = 0
T = 25
C = 2.5
h = 0.25
n = 3
#Euler(t,T,C,h,n)

def RK4(t, T, C, h, n):
    t1 = t
    T1 = T
    C1 = C
    for i in range(n):
        t = t1
        T = T1
        C = C1
        
        deltaC1 = h * dC_dt(t, T, C)
        deltaT1 = h * dT_dt(t, T, C)
        
        deltaC2 = h * dC_dt(t + t/2, T + deltaT1/2, C + deltaC1/2)
        deltaT2 = h * dT_dt(t + t/2, T + deltaT1/2, C + deltaC1/2)
        
        deltaC3 = h * dC_dt(t + t/2, T + deltaT2/2, C + deltaC2/2)
        deltaT3 = h * dT_dt(t + t/2, T + deltaT2/2, C + deltaC2/2)
        
        deltaC4 = h * dC_dt(t + t/2, T + deltaT3, C + deltaC3)
        deltaT4 = h * dT_dt(t + t/2, T + deltaT3, C + deltaC3)
        
        t1 = t + h
        C1 = C + 1/6*deltaC1 + 1/3*deltaC2 + 1/3*deltaC3 + 1/6*deltaC4
        T1 = T + 1/6*deltaT1 + 1/3*deltaT2 + 1/3*deltaT3 + 1/6*deltaT4
        
        print("Itr:",i)
        print("t:",t)
        print("T:",T)
        print("C:",C)
        print("--------")
        
t = 0
T = 25
C = 2.5
h = 0.25
n = 3

#print("\n------- RK4 ---------\n")
#RK4(t,T,C,h,n)


t = 0
T = 25
C = 2.5
h = 0.25
n = 3

S = Euler(t,T,C,h,n)

h /= 2
n = 5
S_l = Euler(t,T,C,h,n)

h /= 2
n = 9
S_ll = Euler(t,T,C,h,n)

QC = (S_l - S) / (S_ll - S_l)
erro = S_ll - S_l

#print("S:",S)
print("S':",S_l)
print("S'':",S_ll)
print("QC:",QC)
print("Erro:",erro)


















