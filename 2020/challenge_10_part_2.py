# Day 10 - Adapter Array
# Part 2
import copy

# Read data from file into array
# Hard coded, can abstract filename as input
with open("sample_10.txt", "r") as fd:
    data_orig = fd.read().splitlines()

adapters = []
for data in data_orig:
    adapters.append(int(data))

adapters.sort()
all_arrangements = []

def find_arrangement(adapters_set, arrangements=[]):
    if len(adapters_set) == 1:
        arrangements.append(adapters_set[0])

    elif len(adapters_set) > 1:
        interest = adapters_set[0]
        for i in range(1, len(adapters_set)):
            jolts_diff = adapters_set[i] - interest

            if jolts_diff >= 1 and jolts_diff <= 3:
                print(f"Combination possible with {interest} -> {adapters_set[i]}")
                #print(f"Next to test {arrangements} -> {adapters_set[i+1:]}")
                arrangements.append(adapters_set[0])
                arrangements.append(adapters_set[i])
                #print(arrangements)
                find_arrangement(adapters_set[i+1:], arrangements)
            else:
                break
    return arrangements

def find_uniq_arrangements(arrangements):
    cur_block = [arrangements[0]]
    all_blocks = []

    for i in range(1, len(arrangements)):
        if arrangements[i] - arrangements[i - 1] > 0:
            cur_block.append(arrangements[i])
        else:
            j = 0
            while cur_block[j] < arrangements[i]:
                j += 1

            new_block = copy.deepcopy(cur_block[:j])
            all_blocks.append(cur_block)
            cur_block = copy.deepcopy(new_block)
            cur_block.append(arrangements[i])
            new_block = []

    all_blocks.append(cur_block)
    return all_blocks

arrangements = find_arrangement(adapters)
uniq_arrs = find_uniq_arrangements(arrangements)

for line in uniq_arrs:
    print(line)