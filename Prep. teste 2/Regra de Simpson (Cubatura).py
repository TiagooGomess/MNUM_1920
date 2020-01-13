
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

