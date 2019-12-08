input = [240920, 789857]
result = []

for i in range(input[0], input[1], 1):
    i = str(i)
    previous = 0
    double = False
    order = True
    for j in i:
        if previous == j:
            double = True
        if previous > j:
            order = False
            break
        previous = j
    if double and order:
        result.append(i)

print(len(result))