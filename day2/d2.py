file = open('input.txt', 'r')
i = map(int, file.read().split(','))

def test(mode):
    global i
    for x in range(0, len(i), 4):
        if(i[x] == 1):
            i[i[(x+3)]] = i[i[(x+1)]] + i[i[(x+2)]]
        if(i[x] == 2):
            i[i[(x+3)]] = i[i[(x+1)]] * i[i[(x+2)]]
        if(i[x] == 99):
            if (mode == 1): print('Result : ' + str(i[0]))
            if(i[0] == 19690720):
                print('End : ' + str(i[0]) + ' and result : ' + str(100*i[1] + i[2]))
            i = map(int, open('input.txt', 'r').read().split(','))
            break

# Part 1
def part1():
    i[1] = 12
    i[2] = 2
    test(1)

# Part 2
def part2():
    for n in range(0, 100):
        for m in range(0, 100):
            i[1] = n
            i[2] = m
            test(2)