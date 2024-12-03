import re

def get_input():
    inp = []
    with open("input.txt") as f:
        for i in f.readlines():
            inp.append(i.strip())
            
    return inp


def multiply(mul_str):
    l = mul_str.split("(")[1].split(",")[0]
    r = mul_str.split(",")[1].split(")")[0]
    return int(l) * int(r)

def main():
# Solution goes here

    sum = 0
    memory = ''
    for i in get_input():
        memory += i.strip()

    muls = re.findall("mul\([0-9]+,[0-9]+\)", memory)
    for j in muls:
        sum += multiply(j)

    print(sum)

    sum_2 = 0

    dos = re.finditer("do\(\)", memory)
    inst_list = []
    for do in dos:
        inst_list.append((do.start(), 'do'))
    donts_list = []
    donts = re.finditer("don't\(\)", memory)
    for dont in donts:
        inst_list.append((dont.start(), 'dont'))

    muls_list = []
    muls = re.finditer("mul\([0-9]+,[0-9]+\)", memory)
    for mul in muls:
        inst_list.append((mul.start(), memory[mul.start():mul.end()]))

    inst_list.sort()
    
    do = True
    for pos, inst in inst_list:
        if inst == 'do':
            do = True
        elif inst == 'dont':
            do = False
        else:
            if do:
                sum_2 += multiply(inst)

    print(sum_2)

    return

if __name__ == "__main__":
    main()