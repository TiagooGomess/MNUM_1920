Método de Gauss-Jacobi:
x0 = [0.25,0.25,0.25,0.25]

A = [[4.5,-1,-1,1],[-1,4.5,1,-1],[-1,2,4.5,-1],[2,-1,-1,4.5]]
b = [1,-1,-1,0]

x1 = [x0[0]+1, x0[1]+1, x0[2]+1, x0[3]+1]

for i in range(1, 3):
    x1[0] = x0[0]
    x1[1] = x0[1]
    x1[2] = x0[2]
    x1[3] = x0[3]
    x0[0] = (1/A[0][0]) * (b[0] - A[0][1] * x1[1] - A[0][2] * x1[2] - A[0][3] * x1[3])
    x0[1] = (1/A[1][1]) * (b[1] - A[1][0] * x1[0] - A[1][2] * x1[2] - A[1][3] * x1[3])
    x0[2] = (1/A[2][2]) * (b[2] - A[2][0] * x1[0] - A[2][1] * x1[1] - A[2][3] * x1[3])
    x0[3] = (1/A[3][3]) * (b[3] - A[3][0] * x1[0] - A[3][1] * x1[1] - A[3][2] * x1[2])
    
    print("{}ª iteração:".format(i))
    print("\nX0: {}\nX1: {}\nX2: {}\nX3: {}\n".format(x0[0], x0[1], x0[2], x0[3]))
    print("------------------------------------------------")



Método de Gauss-Seidel:
x0 = [2.12687,2.39858,3.99517,-3.73040]

A = [[6,0.5,3,0.25],[1.2,3,0.25,0.2],[-1,0.25,4,2],[2,4,1,8]]
b = [25,10,7,-12]

x1 = [x0[0]+1, x0[1]+1, x0[2]+1, x0[3]+1]

for i in range(1,2):
    x1[0] = x0[0]
    x1[1] = x0[1]
    x1[2] = x0[2]
    x1[3] = x0[3]
    x0[0] = (1/A[0][0]) * (b[0] - A[0][1] * x1[1] - A[0][2] * x1[2] - A[0][3] * x1[3])
    x0[1] = (1/A[1][1]) * (b[1] - A[1][0] * x0[0] - A[1][2] * x1[2] - A[1][3] * x1[3])
    x0[2] = (1/A[2][2]) * (b[2] - A[2][0] * x0[0] - A[2][1] * x0[1] - A[2][3] * x1[3])
    x0[3] = (1/A[3][3]) * (b[3] - A[3][0] * x0[0] - A[3][1] * x0[1] - A[3][2] * x0[2])
    
    print("{}ª iteração:".format(i))
    print("\nX0: {}\nX1: {}\nX2: {}\nX3: {}\n".format(x0[0], x0[1], x0[2], x0[3]))
    print("------------------------------------------------")



Regra dos Trapézios (Quadratura):
import math

def f(x):
    return x*math.sin(x)/5

def RegraDosTrapezios(n, a, b, h):
    total = f(a) + f(b)
    for i in range(1, n):
        total += 2 * f(a + i * h)
    total *= h/2
    return total

n = 500
a = 0
b = 20 * math.pi + 0.5
h = (b - a) / n

print(RegraDosTrapezios(n, a, b, h))



Regra de Simpson (Quadratura):
import math

def f(x):
    return math.sin(x)/(x**2)

def MetodoDeSimpson(n, a, b, h):
    total = f(a) + f(b)
    for i in range(1, n, 2):
        total += 4 * f(a + i * h)
    for i in range(2, n-1, 2):
        total += 2 * f(a + i * h)
    total *= h/3
    return total

n = 4
a = math.pi / 2
b = math.pi
h = (b - a) / n

print(MetodoDeSimpson(n, a, b, h))



Estabilidade externa:
def linhaOp(matrix, i, k, x):
    for p in range(len(matrix[0])):
        matrix[x][p] += (matrix[i][p] * k)

def normalizar(matrix, line, k):
    for i in range(len(matrix[0])):
        matrix[line][i] *= k  
        
def MetodoGauss(matrix, residuos):
    for i in range(len(matrix)):
        div = matrix[i][i]
        residuos[i] /= div
        for p in range(i + 1, len(matrix)):
            mul = matrix[p][i]
            linhaOp(matrix, i ,-matrix[p][i]/matrix[i][i], p)
            residuos[p] -= residuos[i] * mul
        normalizar(matrix, i, 1/matrix[i][i])

# Estabilidade externa

matrix = [[18,-1,1],[3,-5,4],[6,8,29]]

solutions = [0.552949, -0.15347, -0.10655]

coefficient_error = 0.1

residuos = [0,0,0]

for i in range(len(matrix)):
    residuos[i] = coefficient_error * (1 - solutions[0] - solutions[1] - solutions[2])
    
MetodoGauss(matrix, residuos)

for i in range(len(matrix) + 1, -1, -1):
    for j in range(i+1, len(matrix)):
        residuos[i] -= matrix[i][j] * residuos[j]

dx = residuos[0]
dy = residuos[1]
dz = residuos[2]


print("\nESTABILIDADE EXTERNA:\n")
print("dx: {}\ndy: {}\ndz: {}".format(dx, dy, dz))



Gauss e estabilidade:
def linhaOp(matrix, i, k, x):
    for p in range(len(matrix[0])):
        matrix[x][p] += (matrix[i][p] * k)

def normalizar(matrix, line, k):
    for i in range(len(matrix[0])):
        matrix[line][i] *= k  
        
def MetodoGauss(matrix, residuos):
    for i in range(len(matrix)):
        div = matrix[i][i]
        residuos[i] /= div
        for p in range(i + 1, len(matrix)):
            mul = matrix[p][i]
            linhaOp(matrix, i ,-matrix[p][i]/matrix[i][i], p)
            residuos[p] -= residuos[i] * mul
        normalizar(matrix, i, 1/matrix[i][i])


# Estabilidade externa

matrix = [[0.7,8,3,12],[-6,0.45,-0.25,15],[8,-3.1,1.05,23]]

void = [0,0,0]
MetodoGauss(matrix,void)

print("\nMÉTODO DE GAUSS:\n")
        
for i in range(len(matrix)):
    print(matrix[i])

z = matrix[2][3]
y = matrix[1][3] - (z * matrix[1][2])
x = matrix[0][3] - (z * matrix[0][2] + y * matrix[0][1])

solutions = [x,y,z]

print("\n---------------------------------------")
print("Solutions:\n")
print(solutions)
print("----------------------------------------")

matrixCopy = [[0.7,8,3,12],[-6,0.45,-0.25,15],[8,-3.1,1.05,23]]

coefficient_error = 0.5

residuos = [0,0,0]

for i in range(len(matrixCopy)):
    residuos[i] = coefficient_error * (1 - solutions[0] - solutions[1] - solutions[2])
    

MetodoGauss(matrixCopy, residuos)

for i in range(len(matrixCopy) + 1, -1, -1):
    for j in range(i+1, len(matrixCopy)):
        residuos[i] -= matrixCopy[i][j] * residuos[j]

dx = residuos[0]
dy = residuos[1]
dz = residuos[2]

print("\nESTABILIDADE EXTERNA:\n")
print("dx: {}\ndy: {}\ndz: {}".format(dx, dy, dz))


Regra de Simpson (com valores da função):
results = [0, 0, 0]

a = 0
b = 1.6
h = (b - a) / 2
dx = 0.20

values = [1.02, 1.21, 1.45, 0.89, 0.62, 1.46, 0.74, 0.36, 0.87]

for j in range(3):
    result = values[0]
    counter = 1
    for i in range(int(h/dx), len(values) - int(h/dx), int(h/dx)):
        if (counter % 2 == 0):
            result += values[i] * 2
        else:
            result += values[i] * 4
        counter += 1
    result += values[len(values) - 1]
    result *= h/3
    print("Step: {}\nResult: {}\n".format(h, result))
    results[j] = result;
    h /= 2

erro = (results[2] - results[1]) / 15
print("\nErro:",erro)



Regra de Simpson (cubatura):
total = 0

xy = [[1.1,1.4,2.6],[2.1,4.9,2.2],[6.3,1.5,1.2]]

hx = 0.9
hy = 0.9

for i in range(len(xy)):
    for j in range(len(xy)):
        if ((i == 0 or i == len(xy) - 1) and (j == 0 or j == len(xy) - 1)):
            total += xy[i][j]
        elif (i == 0 or j == 0 or i == len(xy) - 1 or j == len(xy) - 1):
            total += 4 * xy[i][j]
        else:
            total += 16 * xy[i][j]

total *= (hx * hy) / 9

print("\nTotal:",total)



Regra dos trapézios (cubatura):
total = 0

hx = 1
hy = 1

xy = [[1.1,1.4,7.7],[2.1,3.1,2.2],[7.3,1.5,1.2]]

for i in range(len(xy)):
    for j in range(len(xy)):
        if ((i == 0 or i == len(xy) - 1) and (j == 0 or j == len(xy) - 1)):
            total += xy[i][j]
        elif (i == 0 or j == 0 or i == len(xy) - 1 or j == len(xy) - 1):
            total += 2 * xy[i][j]
        else:
            total += 4 * xy[i][j]

total *= (hx * hy) / 4
print("Total:",total)



Método de Euler (para 2 variáveis):
import math

def C_l(T, C):
    return -math.exp(-0.5/(T + 273)) * C

def T_l(T, C):
    return 20 * math.exp(-0.5/(T + 273)) * C - 0.5 * (T - 20)

def Euler(xn, yn, h, itr):
    xn1 = xn
    yn1 = yn
    for i in range(itr):
        xn = xn1
        yn = yn1
        xn1 = xn + h * T_l(xn, yn)
        yn1 = yn + h * C_l(xn, yn)
        print("\nT: {}".format(xn1))
        print("C: {}\n".format(yn1))
        print("-----------------------------------")
        
Euler(20, 2, 0.2, 2)




Método de Euler (para 1 variável):
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



RK2:
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




RK4:
import math

def dx_dt(t,x):
    return math.sin(2*x) + math.sin(2*t)

def RK4(x, t, h, itr):
    x1 = x
    t1 = t
    for i in range(itr):
        xn = x1
        tn = t1
        
        print("\nItr:",i)
        print("x:",xn)
        print("t:",tn)
        print("-----------")
        
        d1 = h * dx_dt(tn, xn)
        d2 = h * dx_dt(tn + h/2, xn + d1/2)
        d3 = h * dx_dt(tn + h/2, xn + d2/2)
        d4 = h * dx_dt(tn + h, xn + d3)
        
        x1 = xn + d1/6 + d2/3 + d3/3 + d4/6
        t1 = tn + h
     
x = 1
t = 1
h = 0.125
itr = 5
  
RK4(x, t, h, itr)





RK4 (equação diferencial de 2ª ordem):
def dz(t, z):
    return 1.5 + t**2 + t*z

def RK4(t, y, z, h):
    for i in range(3):
        print("Iteração:", i)
        print("t:", t)
        print("y:", y)
        print("--------")
        z1 = h*z
        dz1 = h*dz(t,z)
        
        z2 = h*(z + dz1/2)
        dz2 = h*dz(t + h/2, z + dz1/2)
        
        z3 = h*(z + dz2/2)
        dz3 = h*dz(t + h/2, z + dz2/2)
        
        z4 = h*(z + dz3)
        dz4 = h*dz(t + h, z + dz3)
        
        y += z1/6 + z2/3 + z3/3 + z4/6
        z += dz1/6 + dz2/3 + dz3/3 + dz4/6
        t += h
        
h = 0.2
t = 1
y = 0
z = 1

RK4(t, y, z, h)

    


Euler e RK4 com 3 variáveis: 
import math

b = 0.5
a = 20

def dC_t(t, C, T):
    return -math.exp((-b) / (T + 273)) * C

def dT_t(t, C, T):
    return a * math.exp((-b) / (T + 273)) * C - b * (T - 20)

def euler(t, C, T):
    tn_1 = t
    Cn_1 = C
    Tn_1 = T
    h = 0.25
    for i in range(3):
        tn = tn_1
        Cn = Cn_1
        Tn = Tn_1
        print("t: ", tn, "C: ", Cn, "T: ", Tn)
        tn_1 += h
        Cn_1 += h * dC_t(tn, Cn, Tn)
        Tn_1 += h * dT_t(tn, Cn, Tn)
t = 0
C = 1
T = 15

print("------------------------ EULER --------------------  \n")
euler(t, C, T)       

def RK4(t, C, T):
    tn_1 = t
    Cn_1 = C
    Tn_1 = T
    h = 0.25
    for i in range(3):
        tn = tn_1
        Cn = Cn_1
        Tn = Tn_1
        print("t: ", tn, "C: ", Cn, "T: ", Tn)
        deltaC1 = h * dC_t(tn, Cn, Tn)
        deltaT1 = h * dT_t(tn, Cn, Tn)

        deltaC2 = h * dC_t(tn + (tn / 2), Cn + deltaC1 / 2, Tn + deltaT1 / 2)
        deltaT2 = h * dT_t(tn + (tn / 2), Cn + deltaC1 / 2, Tn + deltaT1 / 2)

        deltaC3 = h * dC_t(tn + (tn / 2), Cn + deltaC2 / 2, Tn + deltaT2 / 2)
        deltaT3 = h * dT_t(tn + (tn / 2), Cn + deltaC2 / 2, Tn + deltaT2 / 2)

        deltaC4 = h * dC_t(tn + (tn / 2), Cn + deltaC3 , Tn + deltaT3)
        deltaT4 = h * dT_t(tn + (tn / 2), Cn + deltaC3 , Tn + deltaT3)

        tn_1 += h
        Cn_1 += (1/6) * deltaC1 + (1/3) * deltaC2 + (1/3) * deltaC3 + (1/6) * deltaC4
        Tn_1 += (1/6) * deltaT1 + (1/3) * deltaT2 + (1/3) * deltaT3 + (1/6) * deltaT4

print(" ------------------------RUNGE-KUTTA 4 ------------------------")
t = 0
C = 1
T = 15
RK4(t, C, T)




Erro e QC para Euler:

import math

def dC_dt(t, C, T):
    return -math.exp(-0.5/(T+273)) * C

def dT_dt(t, C, T):
    return 20 * math.exp(-0.5/(T+273)) * C - 0.5 * (T - 20)
    
def Euler(t, C, T, h, n):
    tn_1 = t
    Cn_1 = C
    Tn_1 = T
    for i in range(n):
        tn = tn_1
        Cn = Cn_1
        Tn = Tn_1
#        print("\nt:",tn,"C:",Cn,"T:",Tn)
#        print("\n----------------------")
        tn_1 += h
        Cn_1 += h * dC_dt(tn, Cn, Tn)
        Tn_1 += h * dT_dt(tn, Cn, Tn)
    return Cn_1
    
t = 0
C = 1
T = 15
h = 0.25

# n -> número de iterações necessárias para o t chegar a 0.5

S = Euler(t, C, T, h, 3)
S_l = Euler(t, C, T, h/2, 5)
S_ll = Euler(t, C, T, h/4, 9)

QC = (S_l-S)/(S_ll-S_l)

erro = S_ll - S_l

print("\nQC:", QC)
print("S:",S)
print("S_l:", S_l)
print("S_ll:", S_ll)
print("Erro:",erro)