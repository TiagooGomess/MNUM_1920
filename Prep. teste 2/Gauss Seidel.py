
print("\nMÉTODO DE GAUSS SEIDEL:\n")

x0 = [2.12687,2.39858,3.99517,-3.73040]

A = [[6,0.5,3,0.25],[1.2,3,0.25,0.2],[-1,0.25,4,2],[2,4,1,8]]
b = [25,10,7,-12]

x1 = [0,0,0,0]

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

"""Convergencia do processo iterativo:
    
   - O metodo converge porque em cada linha da matriz A,
   o modulo do elemento da diagonal principal e superior
   ao modulo da soma dos restantes elementos da linha
    
"""   
    