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
        
matrix = [[0.1,0.5,3,0.25,0],[1.2,0.2,0.25,0.2,1],[-1,0.25,0.3,2,2],[2,0.00001,1,0.4,3]]
void = [0,0,0,0]

MetodoGauss(matrix,void)
print("\n------ Método de Gauss: --------\n")

for i in range(len(matrix)):
    print(matrix[i])
    
w = matrix[3][4]
z = matrix[2][4] - matrix[2][3]*w
y = matrix[1][4] - matrix[1][3]*w - matrix[1][2]*z
x = matrix[0][4] - matrix[0][3]*w - matrix[0][2]*z - matrix[0][1]*y
solutions = [x,y,z,w]

print("\nSolutions:\n")
print(solutions)

matrixCopy = [[0.1,0.5,3,0.25,0],[1.2,0.2,0.25,0.2,1],[-1,0.25,0.3,2,2],[2,0.00001,1,0.4,3]]
residuos = [0,0,0,0]
coefficient_error = 0.5

for i in range(len(matrixCopy)):
    residuos[i] = coefficient_error * (1 - solutions[0] - solutions[1] - solutions[2] - solutions[3])

MetodoGauss(matrixCopy,residuos)

for i in range(len(matrixCopy) + 1, -1, -1):
    for j in range(i + 1, len(matrixCopy)):
        residuos[i] -= matrixCopy[i][j] * residuos[j]
        
print("\nEstabilidade externa:\n")
print(residuos)
 