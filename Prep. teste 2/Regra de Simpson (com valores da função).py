
results = [0, 0, 0]

a = 0
b = 2
h = (b - a) / 2
dx = 0.25

values = [1.04,0.37,0.38,1.49,1.08,0.13,0.64,0.84,0.12]

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