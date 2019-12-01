import math

file = open('input.txt', 'r')
words = file.readlines()

result = 0

for i in range(0, len(words)):
    result = result + (math.trunc(int(words[i].replace('\n', '')) / 3)) - 2

print result