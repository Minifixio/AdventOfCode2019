file = open('input.txt', 'r')
i = map(int, file.read().split(','))

for x in range(0, len(i), 4):
    if(i[x] == 1):
        i[i[(x+3)]] = i[i[(x+1)]] + i[i[(x+2)]]
    if(i[x] == 2):
        i[i[(x+3)]] = i[i[(x+1)]] * i[i[(x+2)]]
    if(i[x] == 99):
        print('End : ' + str(i[0]))
        break
