# Challenge 5 - Binary Decoding
# Part 1
import numpy as np
import sys

with open('input_5.txt') as fd:
    data_str = fd.read().splitlines()

seat_ids = []
all_seat_ids = []
for i in range(128):
    for j in range(8):
        all_seat_ids.append(i * 8 + j)

for ticket in data_str:
    row_lower = 0
    row_upper = 127
    column_lower = 0
    column_upper = 7

    for instruction in ticket:
        if instruction == 'F':
            row_upper = int(np.floor(row_upper - ((row_upper - row_lower) / 2.)))
        elif instruction == 'B':
            row_lower = int(np.ceil(row_lower + ((row_upper - row_lower) / 2.)))
        elif instruction == 'L':
            column_upper = int(np.floor(column_upper - ((column_upper - column_lower) / 2.)))
        elif instruction == 'R':
            column_lower = int(np.ceil(column_lower + ((column_upper - column_lower) / 2.)))
        else:
            print(f"Invalid input detected: {instruction}")
            sys.exit(1)
    
    if row_upper != row_lower or column_upper != column_lower:
        print(f"Error in instruction found.")

    else:
        seat_id = row_upper * 8 + column_upper
        seat_ids.append(seat_id)
        all_seat_ids.pop(all_seat_ids.index(seat_id))

print(f"Highest seat id: {np.max(seat_ids)}")
print(f"Available seat ids: {all_seat_ids}")