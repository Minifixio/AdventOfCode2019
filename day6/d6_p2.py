orbits = [ [o[:3], o[4:]] for o in open('input.txt', 'r').read().split('\n') ]

def get_orbit(el):
    for o in orbits:
        if el[0] == o[1]:
            return o

def draw_path(scope):
    space_path = [ o for o in orbits if o[1] == scope ][0]
    orbits_list = []
    while space_path[0] != 'COM':
        orbits_list.append(space_path)
        orbiting = get_orbit(space_path)
        space_path = orbiting
    return orbits_list

def main():
    my_orbits = draw_path('YOU')
    santa_orbits = draw_path('SAN')

    for i, v in enumerate(my_orbits):
        found = False
        for j, w in enumerate(santa_orbits):
            if v == w:
                found = True
                return i + j - 2 # Removing the two original orbits
        if found: break

print(main())