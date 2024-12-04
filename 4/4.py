
def get_input():
    inp = []
    with open("input.txt") as f:
        for i in f.readlines():
            inp.append(i.strip())
            
    return inp

dirs = [(1, 0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1)]
key = ['X', 'M', 'A', 'S']
field = get_input()
max_x = len(field[0])
max_y = len(field)

perms = [{(1,1): 'M', (-1, 1): 'M', (-1,-1): 'S', (1, -1): 'S'},
         {(1,1): 'M', (-1, 1): 'S', (-1,-1): 'S', (1, -1): 'M'},
         {(1,1): 'S', (-1, 1): 'S', (-1,-1): 'M', (1, -1): 'M'},
         {(1,1): 'S', (-1, 1): 'M', (-1,-1): 'M', (1, -1): 'S'}]

def recursive_xmas(pos, k, next_dir, f):
    x, y = pos
    next_x, next_y = next_dir
    if 0 <= x + next_x < max_x and 0 <= y + next_y < max_y:
        if f[y + next_y][x + next_x] == k[0]:
            if len(k) == 1:
                return True
            return recursive_xmas((x + next_x, y + next_y), k[1:], next_dir, f)
    
    return False
            
def check_pos(pos, val):
    x, y = pos
    if 0 <= x < max_x and 0 <= y < max_y:
        return field[y][x] == val

def main(f, k):
# Solution goes here

    count_1 = 0
    count_2 = 0
    for y in range(max_y):
        for x in range(max_x):
            # part 1
            if f[y][x] == k[0]:
                for next_dir in dirs:
                    if recursive_xmas((x,y), k[1:], next_dir, f):
                        # print(f"({x},{y}): {next_dir}")
                        count_1 += 1

    for y in range(max_y):
        for x in range(max_x):

            # part 2
            # 32982 too high
            if f[y][x] == 'A':
                for perm in perms:
                    sub_count = 0
                    for k,v in perm.items():
                        n_x, n_y = k
                        if check_pos((x + n_x, y + n_y), v):
                            sub_count += 1
                    if sub_count == 4:
                        count_2 += 1
                        # print(f"({x},{y}): {perm}")
                        break
                        

    print(count_1)
    print(count_2)

if __name__ == "__main__":
    main(field, key)