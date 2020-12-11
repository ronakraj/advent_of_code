# Day 10 - Adapter Array
# Part 2
import copy

# Read data from file into array
# Hard coded, can abstract filename as input
with open("input_11.txt", "r") as fd:
    data_orig = fd.read().splitlines()

max_row_len = len(data_orig) - 1
max_col_len = len(data_orig[0]) - 1 # Assuming same length
print(f"MAX: {max_row_len}\t{max_col_len}")
print(f"Total seats: {(max_row_len+1) * (max_col_len+1)}")
def split(word):
    return [char for char in word]

data_list = []
for item in data_orig:
    data_list.append(split(item))

def get_adjacent(row, col, data):
    check_list = []
    if row == 0 and col == 0:
        check_list.append(data[row+1][col])
        check_list.append(data[row][col+1])
        check_list.append(data[row+1][col+1])

    elif row == max_row_len and col == max_col_len:
        check_list.append(data[row-1][col])
        check_list.append(data[row][col-1])
        check_list.append(data[row-1][col-1])

    elif row == max_row_len and col == 0:
        check_list.append(data[row-1][col])
        check_list.append(data[row][col+1])
        check_list.append(data[row-1][col+1])

    elif row == 0 and col == max_col_len:
        check_list.append(data[row][col-1])
        check_list.append(data[row+1][col])
        check_list.append(data[row+1][col-1])

    elif row == 0:
        check_list.append(data[row+1][col-1])
        check_list.append(data[row+1][col])
        check_list.append(data[row+1][col+1])
        check_list.append(data[row][col-1])
        check_list.append(data[row][col+1])

    elif row == max_row_len:
        check_list.append(data[row-1][col-1])
        check_list.append(data[row-1][col])
        check_list.append(data[row-1][col+1])
        check_list.append(data[row][col-1])
        check_list.append(data[row][col+1])

    elif col == 0:
        check_list.append(data[row-1][col+1])
        check_list.append(data[row][col+1])
        check_list.append(data[row+1][col+1])
        check_list.append(data[row-1][col])
        check_list.append(data[row+1][col])

    elif col == max_col_len:
        check_list.append(data[row-1][col-1])
        check_list.append(data[row][col-1])
        check_list.append(data[row+1][col-1])
        check_list.append(data[row-1][col])
        check_list.append(data[row+1][col])

    else:
        check_list.append(data[row-1][col-1])
        check_list.append(data[row-1][col])
        check_list.append(data[row-1][col+1])
        check_list.append(data[row][col-1])
        check_list.append(data[row][col+1])
        check_list.append(data[row+1][col-1])
        check_list.append(data[row+1][col])
        check_list.append(data[row+1][col+1])

    return check_list

def none_occupied(row, col, data):
    safe_list = ['L', '.']
    check_list = get_adjacent(row, col, data)
    for item in check_list:
        if item not in safe_list:
            return False
    return True

def occupied(row, col, qty, symbol, data):
    check_list = get_adjacent(row, col, data)
    if check_list.count(symbol) >= qty:
        return True
    else:
        return False

def update_table(data_in):
    data_out = copy.deepcopy(data_in)
    for row in range(len(data_in)):
        for col in range(len(data_in[row])):
            if data_in[row][col] == 'L':
                if none_occupied(row, col, data_in):
                    data_out[row][col] = '#'
            elif data_in[row][col] == '#':
                if occupied(row, col, 4, '#', data_in):
                    data_out[row][col] = 'L'
    return data_out

def pretty_print(data):
    for item in data:
        print(item)

def check_same(data_1, data_2):
    for i in range(len(data_1)):
        if data_1[i] != data_2[i]:
            return False
    return True

data_in = copy.deepcopy(data_list)
data_out = []
j = 1
while True:
    data_out = update_table(data_in)
    if check_same(data_in, data_out):
        print("STABILIZED")
        break
    data_in = copy.deepcopy(data_out)

occupied = 0
vacant = 0
floor = 0
for row in data_in:
    for item in row:
        if item == '#':
            occupied += 1
        elif item == 'L':
            vacant += 1
        elif item == '.':
            floor += 1

print(f"Total occupied seats (#): {occupied}\nTotal vacant seats (L): {vacant}\nTotal floor seats (.): {floor}\nTotal: {occupied+vacant+floor}")
