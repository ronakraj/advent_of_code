# Day 10 - Adapter Array
# Part 1

# Read data from file into array
# Hard coded, can abstract filename as input
with open("input_10.txt", "r") as fd:
    data_orig = fd.read().splitlines()

adapters = []
for data in data_orig:
    adapters.append(int(data))

adapters.sort()

one_diff = 1
three_diff = 1
for i in range(1, len(adapters)):
    if adapters[i] - adapters[i - 1] == 1:
        one_diff += 1
    elif adapters[i] - adapters[i - 1] == 3:
        three_diff += 1

print(f"One: {one_diff} Three: {three_diff} Multiplied: {one_diff * three_diff}")