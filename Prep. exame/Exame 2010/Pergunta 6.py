def linhaOp(matrix,i,k,x):
    for p in range(len(matrix[0])):
        matrix[x][p] += matrix[i][p]*k
        
def normalizar(matrix,line,k):
    for i in range(len(matrix[0])):
        matrix[line][i] *= k
        
def MetodoGauss(matrix,residuos):
    for i in range(len(matrix)):
        div = matrix[i][i]
        residuos[i] /= div
        for p in range(i + 1, len(matrix)):
            mul = matrix[p][i]
            linhaOp(matrix,i,-matrix[p][i]/matrix[i][i],p)
            residuos[p] -= residuos[i] * mul
        normalizar(matrix,i,1/matrix[i][i])
        
matrixCopy = [[18,-1,1,10],[3,-5,4,2],[6,8,29,-1]]

solutions = [0.552949,-0.15347,-0.10655]

residuos = [0,0,0]
coefficient_error = 0.1

for i in range(len(matrixCopy)):
    residuos[i] = coefficient_error * (1 - solutions[0] - solutions[1] - solutions[2])

MetodoGauss(matrixCopy,residuos)

for i in range(len(matrixCopy) + 1, -1, -1):
    for j in range(i + 1, len(matrixCopy)):
        residuos[i] -= matrixCopy[i][j] * residuos[j]

print(residuos)