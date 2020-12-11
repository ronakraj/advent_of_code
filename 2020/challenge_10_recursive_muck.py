# Day 10 - Adapter Array
# Part 2
import copy

# Read data from file into array
# Hard coded, can abstract filename as input
with open("input_10.txt", "r") as fd:
    data_orig = fd.read().splitlines()

adapters = []
for data in data_orig:
    adapters.append(int(data))

adapters.sort()

def satisfies_rule(one, two):
    if two - one >= 1 and two - one <= 3:
        return True
    else:
        return False

all_arrangements = {}
for j in range(0, len(adapters)):
    adapters_subset = adapters[j:]
    all_arrangements[adapters_subset[0]] = []
    for i in range(1, len(adapters_subset)):
        if satisfies_rule(adapters_subset[0], adapters_subset[i]):
            all_arrangements[adapters_subset[0]].append(adapters_subset[i:])
        else:
            break

first_arrangement = all_arrangements[1][0]
final_arrangements = [first_arrangement]

for i in range(1, len(first_arrangement)):
    if len(all_arrangements[i]) > 1:
        new_arrangement = [index]
        new_arrangement.append(remaining)

        for value in new_arrangement:
            if len(all_arrangements[value]) > 1:


    final_arrangements.append(new_arrangement)
