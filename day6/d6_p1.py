input_file = open('input.txt', 'r').read().split('\n')
total = 0   

def orbit(plot):
    plot = str(plot)
    for i in input_file:
        if plot[:3] == i[4:]:
            if plot[:3] == 'COM':
                return 1  
            else:
                return orbit(i) + 1
    return 0

for j in input_file:
    total += orbit(j)
    total += 1
    
print(total)


