def linhaOp(matrix, i, k, x):
    for p in range(len(matrix[0])):
        matrix[x][p] += matrix[i][p]*k
        
def normalizar(matrix, line, k):
    for i in range(len(matrix[0])):
        matrix[line][i] *= k
        
def MetodoGauss(matrix,residuos):
    for i in range(len(matrix)):
        div = matrix[i][i]
        residuos[i] /= div
        for p in range(i + 1, len(matrix)):
            mul = matrix[p][i]
            linhaOp(matrix, i, -matrix[p][i]/matrix[i][i],p)
            residuos[p] -= residuos[i]*mul
        normalizar(matrix,i,1/matrix[i][i])
        
matrix = [[1,1/2,1/3,-1],[1/2,1/3,1/4,1],[1/3,1/4,1/5,1]]

void = [0,0,0]
MetodoGauss(matrix,void)

print("\nMétodo de Gauss:\n")

for i in range(len(matrix)):
    print(matrix[i])
    
z = matrix[2][3]
y = matrix[1][3] - matrix[1][2]*z
x = matrix[0][3] - matrix[0][2]*z - matrix[0][1]*y

solutions = [x,y,z]

print("\nSolutions:",solutions)

matrixCopy = [[1,1/2,1/3,-1],[1/2,1/3,1/4,1],[1/3,1/4,1/5,1]]

coefficient_error = 0.05

residuos = [0,0,0]

for i in range(len(matrixCopy)):
    residuos[i] = coefficient_error * (1 - solutions[0] - solutions[1] - solutions[2])

MetodoGauss(matrixCopy,residuos)

for i in range(len(matrixCopy)+1,-1,-1):
    for j in range(i+1,len(matrixCopy)):
        residuos[i] -= matrixCopy[i][j] * residuos[j]
        
dx = residuos[0]
dy = residuos[1]
dz = residuos[2]

print("\n\nEstabilidade externa:\n")
print("dx: {}\ndy: {}\ndz: {}".format(dx,dy,dz))

 