
# Método de Simpson

results = [0,0,0] # S, S' e S''

values = [0,0.0073522983,0.1806367724, 0.9465361603, 3.0161883586, 	7.3851864223, 15.3335785653, 28.4258681599, 48.5110137371, 77.7224289867, 118.4779827567, 173.4799990541, 245.7152570443, 338.4549910514, 455.2548905581, 599.9551002058, 776.6802197943]
h = 1
dt = 1

for j in range(len(results)):
    total = values[0] + values[-1] # primeiro e último valores
    counter = 1
    for i in range(int(dt/h),len(values)-int(dt/h),int(dt/h)):
        if (counter % 2 == 0):
            total += 2 * values[i]
        else:
            total += 4 * values[i]
    total *= h/3
    results[j] = total
    h /= 2

print("\nTotal:",results[0])

QC = (results[1] - results[0]) / (results[2] - results[1])

erro = (results[2] - results[1]) / 15

print("\nQC:",QC)

print("\nErro:",erro)

