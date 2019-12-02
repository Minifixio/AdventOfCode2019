import math

file = open('input.txt', 'r')
l = file.readlines()

result1 = 0
result2 = 0

def fuel(n):
    return math.trunc(n / 3) - 2

for i in l:
    i = int(i.replace('\n', ''))
    result1 = result1 + fuel(i)

    if(fuel(i) > 0):
       while(fuel(i) > 0):
           result2 = result2 + fuel(i)
           i = fuel(i)
    else:
        result2 = result2 + fuel(i)

print ('Result part 1: ' + str(result1))
print ('Result part 2: ' + str(result2))