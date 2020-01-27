
def linhaOp(matrix, i, k, x):
    for p in range(len(matrix[0])):
        matrix[x][p] += matrix[i][p] * k
        
def normalizar(matrix, line, k):
    for i in range(len(matrix[0])):
        matrix[line][i] *= k
        
def MetodoGauss(matrix, residuos):
    for i in range(len(matrix)):
        div = matrix[i][i]
        residuos[i] /= div
        for p in range(i + 1, len(matrix)):
            mul = matrix[p][i]
            residuos[p] -= residuos[i] * mul
            linhaOp(matrix, i, -matrix[p][i]/matrix[i][i], p)
        normalizar(matrix, i, 1/matrix[i][i])
        
matrix = [[0.000030,0.213472,0.332147,0.235262],[0.215512,0.375623,0.476625,0.127653],[0.173257,0.663257,0.625675,0.285321]]
matrixCopy = [[0.000030,0.213472,0.332147,0.235262],[0.215512,0.375623,0.476625,0.127653],[0.173257,0.663257,0.625675,0.285321]]

solutionsB = [ 0.674262, 0.053108, -0.991431 ]

solutionsC =  [ -0.674262, 0.053108, -0.991431 ]

residuosB = [0,0,0,0]
residuosC = [0,0,0,0]

coefficient_error = 0.1

for i in range(len(matrix)):
    residuosB[i] = coefficient_error * (1 - solutionsB[0] - solutionsB[1] - solutionsB[2])

for i in range(len(matrixCopy)):
    residuosC[i] = coefficient_error * (1 - solutionsC[0] - solutionsC[1] - solutionsC[2])
    
MetodoGauss(matrix, residuosB)

MetodoGauss(matrixCopy, residuosC)

for i in range(len(matrix) + 1, -1, -1):
    for j in range(i + 1, len(matrix)):
        residuosB[i] -= matrix[i][j] * residuosB[j]
    
for i in range(len(matrixCopy) + 1, -1, -1):
    for j in range(i + 1, len(matrixCopy)):
        residuosC[i] -= matrixCopy[i][j] * residuosC[j]

print("\n------ESTABILIDADE EXTERNA-------")
      
print("\nPara a solução B:")
print("Delta x1:",residuosB[0])
print("Delta x2:",residuosB[1])
print("Delta x2:",residuosB[2])

print("\nPara a solução C:")
print("Delta x1:",residuosC[0])
print("Delta x2:",residuosC[1])
print("Delta x2:",residuosC[2])
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    