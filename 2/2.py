import copy
def get_input():
    inp = []
    with open("input.txt") as f:
        for i in f.readlines():
            inp.append(i.strip())
            
    return inp

def is_it_safe(num_row):
    
    pos = int(num_row[0]) - int(num_row[1]) < 0

    for i, num in enumerate(num_row):
        if i == len(num_row) - 1:
            print(num_row)
            return -1
        else:
            if abs(int(num) - int(num_row[i+1])) not in range(1, 4):
                return i
            elif int(num) < int(num_row[i+1]) and not pos:
                return i
            elif int(num) > int(num_row[i+1]) and pos:
                return i


def main():
# Solution goes here
    print("test")

    count_1 = 0
    count_2 = 0
    for row in get_input():
        num_row = row.split()
        safe = is_it_safe(num_row)
        if safe == -1:
            count_1 += 1
            count_2 += 1
        else:
            for i in range(len(num_row)):
                new_num_row = copy.deepcopy(num_row)
                new_num_row.pop(i)
                if is_it_safe(new_num_row) == -1:
                    count_2 += 1
                    break
    
    print(count_1)
    print(count_2)
    return

if __name__ == "__main__":
    main()