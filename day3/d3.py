file = open('input.txt', 'r').read().split('\n')

t1 = file[0].split(',')
t2 = file[1].split(',')

vertical = []
horizontal = []
junctions = []

def intersect(p1, p2, mode):
    global junctions
    if mode == 'U' or mode == 'D':    
        for k in horizontal:
            if(p1[0] >= k[0][0] and p1[0] <= k[1][0] and p1[1] <= k[0][1] and p2[1] >= k[0][1]):
                junctions.append([p1[0], k[0][1]]) 
    if mode == 'R' or mode == 'L':
        for k in vertical:
            if(p1[1] >= k[0][1] and p1[1] <= k[1][1] and p1[0] <= k[0][0] and p2[0] >= k[0][0]):
                junctions.append([p1[0], k[0][1]]) 

def track1(x=0, y=0):
    for i in t1:
        point = track(i,x,y)
        if point[2] == 'R': horizontal.append(([x,y], [point[0], point[1]]))
        if point[2] == 'L': horizontal.append(([point[0], point[1]], [x,y]))
        if point[2] == 'U': vertical.append(([x,y], [point[0], point[1]]))
        if point[2] == 'D': vertical.append(([point[0], point[1]], [x,y]))    
        x, y = point[0], point[1]

def track2(x=0, y=0):
    for j in t2:
        point = track(j,x,y)
        if point[2] == 'R': intersect([x,y], ([point[0], point[1]]), 'R')
        if point[2] == 'L': intersect(([point[0], point[1]]), [x,y], 'L')
        if point[2] == 'U': intersect([x,y], ([point[0], point[1]]), 'U')
        if point[2] == 'D': intersect(([point[0], point[1]]), [x,y], 'D')    
        x, y = point[0], point[1]

def track(value, x, y):
    if value[0] == 'R': x = x + int(value[1:])
    if value[0] == 'L': x = x - int(value[1:])
    if value[0] == 'U': y = y + int(value[1:])
    if value[0] == 'D': y = y - int(value[1:])  
    return [x,y,value[0]]

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
