def main(system_id = 1, i = 0, code = 0, val = list(map(int, open('input.txt', 'r').read().split(',')))):
    while code != 99:
        nxt = val[(i+1)]
        code = val[i]
        opcode = abs(code) % 10 

        if opcode == 3:
            val[nxt] = system_id
            i = i + 2
            continue

        elif opcode == 4:
            print('Output: ' + str(val[nxt]))
            i = i + 2
            continue

        elif code == 99:
            break

        else:
            if ((code // 100)%10) == 0: p1 = val[nxt]
            else: p1 = nxt
            if ((code // 1000)%10) == 0: p2 = val[val[(i+2)]] 
            else: p2 = val[(i+2)] 
            
            if opcode == 1:
                val[val[(i+3)]] = (p1 + p2) 
                i = i + 4
            elif opcode == 2:
                val[val[(i+3)]] = (p1 * p2) 
                i = i + 4
            elif opcode == 5:
                if p1 != 0:
                    i = p2
                else: i = i + 3
            elif opcode == 6:
                if p1 == 0:
                    i = p2
                else: i = i + 3
            elif opcode == 7:
                if p1 < p2: val[val[(i+3)]] = 1
                else: val[val[(i+3)]] = 0
                i = i + 4
            if opcode == 8:
                if p1 == p2: val[val[(i+3)]] = 1
                else: val[val[(i+3)]] = 0
                i = i + 4

main(5)