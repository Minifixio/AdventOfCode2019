file = open('input.txt', 'r').read().split('\n')

t1 = file[0].split(',')
t2 = file[1].split(',')

vertical = []
horizontal = []
segment = []
junctions = []

def intersect(p1, p2, mode):
    global junctions
    if mode == 'U':    
        for k in horizontal:
            if(p1[0] >= k[0][0] and p1[0] <= k[1][0] and p1[1] <= k[0][1] and p2[1] >= k[0][1]):
                junctions.append([p1[0], k[0][1]]) 
    if mode == 'D':
        for k in horizontal:
            if(p1[0] >= k[0][0] and p1[0] <= k[1][0] and p1[1] <= k[0][1] and p2[1] >= k[0][1]):
                junctions.append([p1[0], k[0][1]]) 
    if mode == 'R':
        for k in vertical:
            if(p1[1] >= k[0][1] and p1[1] <= k[1][1] and p1[0] <= k[0][0] and p2[0] >= k[0][0]):
                junctions.append([p1[0], k[0][1]]) 
    if mode == 'L':
        for k in vertical:
            if(p1[1] >= k[0][1] and p1[1] <= k[1][1] and p1[0] <= k[0][0] and p2[0] >= k[0][0]):
                junctions.append([p1[0], k[0][1]]) 

def track1(x=0, y=0):
    for i in t1:
        segment = []
        if i[0] == 'R':
            horizontal.append(([x,y], [(x + int(i[1:])), y]))
            x = x + int(i[1:])
        if i[0] == 'L':
            horizontal.append(([(x - int(i[1:])), y],[x,y]))
            x = x - int(i[1:])
        if i[0] == 'U':
            vertical.append(([x,y], [x, (y + int(i[1:]))]))
            y = y + int(i[1:])
        if i[0] == 'D':
            vertical.append(([x, (y - int(i[1:]))], [x,y]))
            y = y - int(i[1:])   

def track2(x=0, y=0):
    for j in t2:
        if j[0] == 'R':
            intersect(([x, y]), ([(x + int(j[1:])), y]), 'R')
            x = x + int(j[1:])
        if j[0] == 'L':
            intersect(([(x - int(j[1:])), y]), ([x, y]), 'L')
            x = x - int(j[1:])
        if j[0] == 'U':
            intersect(([x, y]), ([x, (y + int(j[1:]))]), 'U')
            y = y + int(j[1:])
        if j[0] == 'D':
            intersect(([x, (y - int(j[1:]))]), ([x, y]), 'D')
            y = y - int(j[1:])

def distance():
    result = abs(junctions[0][0]) + abs(junctions[0][1])
    for k in junctions:
        d = abs(k[0]) + abs(k[1])
        if d < result:
            result = d
    print('Min distance : ' + str(result))    

track1()
track2()
distance()
