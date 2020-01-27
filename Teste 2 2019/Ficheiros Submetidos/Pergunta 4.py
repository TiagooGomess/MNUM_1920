
def dv_du(u,v):
    return u*(u/2+1)*v**3+(u+5/2)*v**2

def RK4(u,v, h, n):
    u1 = u
    v1 = v
    for i in range(n):
        un = u1
        vn = v1
#        print("-------")
#        print("Itr:",i)
#        print("u:",un)
#        print("v:",vn)
        d1 = h * dv_du(un, vn)
        d2 = h * dv_du(un + h/2, vn + d1/2)
        d3 = h * dv_du(un + h/2, vn + d2/2)
        d4 = h * dv_du(un + h, vn + d3)
        v1 = vn + d1/6 + d2/3 + d3/3 + d4/6
        u1 = un + h
    return vn
        
u = 1
v = 0.15
h = 0.08
n = int((u-v)/h) + 1 # para o u chegar a 1.8

S = RK4(u,v,h,n)

h /= 2
n = int((u-v)/h) # para o u chegar a 1.8
S_l = RK4(u,v,h,n)

h /= 2
n = int((u-v)/h) - 1 # para o u chegar a 1.8
S_ll = RK4(u,v,h,n)

QC = (S_l - S) / (S_ll - S_l)

erro = (S_ll - S_l) / 15

print("\nS:",S)
print("S':",S_l)
print("S'':",S_ll)
print("\nQC:",QC)
print("\nErro:",erro)