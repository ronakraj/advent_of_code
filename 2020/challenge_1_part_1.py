# Day 1 - Report Repair
# Part 1

# Read data from file into array
# Hard coded, can abstract filename as input
with open("input_1.txt", "r") as fd:
    data_str = fd.read().splitlines()

# Convert array of string to int
data_int = [int(item) for item in data_str]

# Sort data in ascending order
data_int.sort()

# Find integers that add to 2020
# Hard coded, can abstract as input
lower_index = 0
upper_index = len(data_int) - 1
total_cur = 0
total_exp = 2020

# First remove any number greater than our expected integer
for data in data_int:
    if data > total_exp:
        data_int.pop(data_int.index(data))

while(lower_index <= upper_index and upper_index >= lower_index):
    total_cur = data_int[lower_index] + data_int[upper_index]

    if total_cur < total_exp:
        lower_index += 1
    elif total_cur > total_exp:
        upper_index -= 1
    else:
        # total_cur == total_exp
        break

if total_cur == total_exp:
    multiply = data_int[lower_index] * data_int[upper_index]
    print(f"SUM: {total_cur}\nValue 1: {data_int[lower_index]}\tValue 2: {data_int[upper_index]}\nMultiply: {multiply}")