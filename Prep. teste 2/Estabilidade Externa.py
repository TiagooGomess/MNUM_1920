
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

