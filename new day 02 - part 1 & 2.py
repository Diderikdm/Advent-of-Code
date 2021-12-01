from itertools import combinations

def run(i):
    steps, func = opcodes[data[i]]
    func(*[data[x] for x in range(i, i + steps)])
    return i + steps
    

with open("2019 day2.txt", 'r') as file:
    data = [int(x) for x in file.read().split(',')]
    opcodes = {
        1 : [4, lambda w, x, y, z: ops.__setitem__(z, ops[x] + ops[y])],
        2 : [4, lambda w, x, y, z: ops.__setitem__(z, ops[x] * ops[y])]
        }
    combs = [(x,y) for x,y in combinations([z for z in range(100)] * 2, 2)]
    ops = {e : x for e,x in enumerate(data)}
    while ops[0] != 19690720:
        i = 0
        ops = {e : x for e,x in enumerate(data)}
        comb = combs.pop(0)
        ops[1], ops[2] = comb
        while ops[i] != 99:
            i = run(i)
        if comb == (12, 2):
            print(ops[0])
    print(''.join([str(x).rjust(2, '0') for x in comb]))
