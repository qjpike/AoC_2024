

def get_input():
    inp = []
    with open("input.txt") as f:
        for i in f.readlines():
            inp.append(i.strip())
            
    return inp


def main():
# Solution goes here
    list_1 = []
    list_2 = []

    sum = 0
    
    for i in get_input():
        list_1.append(int(i.strip().split()[0]))
        list_2.append(int(i.strip().split()[1]))

    list_1.sort()
    list_2.sort()

    for i in range(len(list_1)):
        sum += abs(list_1[i] - list_2[i])

    sum_2 = 0
    for i in list_1:
        sum_2 += i * list_2.count(i)
    
    print("Part 1:", sum)
    print("Part 2:", sum_2)
    return

if __name__ == "__main__":
    main()