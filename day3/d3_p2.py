file = open('input.txt', 'r').read().split('\n')

def isWayX(d):
    way = d[0]
    if (way == 'R' or way == 'L'):
        return True
    else:
        return False

def formatL(l):
    total = 0
    x, y = 0, 0
    for i, v in enumerate(l):
        step = int(v[1:]) if (v[0] == 'R' or v[0] == 'U') else -int(v[1:])
        l[i] = [v, [x, y], step, total]
        total += abs(step)
        if isWayX(v):
            x += step
        else:
            y += step
    return(l)

t1 = formatL(file[0].split(','))
t2 = formatL(file[1].split(','))

def isInRange(pos, lim1, lim2):
    sup = lim1 if lim1 >= lim2 else lim2
    inf = lim1 if lim1 < lim2 else lim2
    if pos >= inf and pos <= sup:
        return True
    else:
        return False

def main():
    best = 0
    for i in t1:
        iPos = i[1]
        for j in t2:
            jPos = j[1]
            if isWayX(i[0]) and not isWayX(j[0]):
                if isInRange(iPos[1], jPos[1], jPos[1] + j[2]) and isInRange(jPos[0], iPos[0], iPos[0] + i[2]):
                    cross = (jPos[0], iPos[1])
                    total = j[3] + i[3] + abs(iPos[0] - cross[0]) + abs(jPos[1] - cross[1])
                    if total < best or best == 0: best = total                   
            if not isWayX(i[0]) and isWayX(j[0]):
                if isInRange(iPos[0], jPos[0], jPos[0] + j[2]) and isInRange(jPos[1], iPos[1], iPos[1] + i[2]):
                    cross = (iPos[0], jPos[1])
                    total = j[3] + i[3] + abs(iPos[1] - cross[1]) + abs(jPos[0] - cross[0])
                    if total < best or best == 0: best = total 
    print (best)

main()

