
def linhaOp(matrix, i, k, x):
    for p in range(len(matrix[0])):
        matrix[x][p] += (matrix[i][p] * k)

def normalizar(matrix, line, k):
    for i in range(len(matrix[0])):
        matrix[line][i] *= k  
        
def MetodoGauss(matrix):
    for i in range(len(matrix)):
        for p in range(i + 1, len(matrix)):
            linhaOp(matrix, i ,-matrix[p][i]/matrix[i][i], p)
        normalizar(matrix, i, 1/matrix[i][i])
        
matriz = [[0.1, 0.5, 3, 0.250,0],[1.2,0.2,0.25,0.2,1],[-1,0.25,0.3,2,2],[2,0.00001,1,0.4,3]]

MetodoGauss(matriz)

print("\nMÉTODO DE GAUSS:\n")
        
for i in range(len(matriz)):
    print(matriz[i])

# adaptar se a matriz for 3 x 3
w = matriz[3][4]
z = matriz[2][4] - (w * matriz[2][3])
y = matriz[1][4] - (w * matriz[1][3] + z * matriz[1][2])
x = matriz[0][4] - (w * matriz[0][3] + z * matriz[0][2] + y * matriz[0][1])

solutions = [x,y,z,w]

print("\n--------------------------------------------------------------------------")
print("Solutions:\n")
print(solutions)
