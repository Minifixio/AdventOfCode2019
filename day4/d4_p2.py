input = [240920, 789858]
result = []

for i in range (240920, 789858):
    i = [int(x) for x in str(i)] 
    previous = 0
    double = False
    order = True
    for j in i:
        if previous == j and i.count(j) < 3:
            double = True
        if previous > j:
            order = False
            break
        previous = j
    if double and order:
        result.append(i)

print(len(result))