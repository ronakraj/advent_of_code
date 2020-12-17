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

arrangements = {}
arrangements[0] = 1
for adapter in adapters:
    arrangements[adapter] = 0
    
    if (adapter-1) in arrangements:
        arrangements[adapter] += arrangements[adapter-1]
    
    if (adapter-2) in arrangements:
        arrangements[adapter] += arrangements[adapter-2]

    if (adapter-3) in arrangements:
        arrangements[adapter] += arrangements[adapter-3]


print(arrangements[max(adapters)])
"""

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



all_adapters = []
for key in all_arrangements:
    all_adapters.append(key)

index_arr = [0] * (max(all_adapters)+1)
index_arr[0] = 1
print(all_arrangements)
for key in all_arrangements:
    print(f"{key} -> {len(all_arrangements[key])}")
    for arr in all_arrangements[key]:
        index_arr[arr[0]] += 1

print(index_arr)
total = 0
for i in range(max(all_adapters)+1):
    if index_arr[i] > 1:
        total += index_arr[i-1]
        total += index_arr[i-2]
        total += index_arr[i-3]

print(f"Total combinations: {total}")

arrangements_uniq = []
for value in all_arrangements[1]:
    new_arrangement = [1]
    for i in range(len(value)):
        new_arrangement.append(value[i])
    arrangements_uniq.append(new_arrangement)

def is_uniq(arr_to_check, arr_list):
    for arr in arr_list:
        if arr == arr_to_check:
            return False
    return True

def find_all(first_arr, uniq_list):
    for arr in first_arr:
        for i in range(1, len(arr)):
            secondary_arr = all_arrangements[arr[i]]

            for sarr in secondary_arr:
                new_arr = arr[0:i+1]
                for j in range(len(sarr)):
                    new_arr.append(sarr[j])

                if is_uniq(new_arr, uniq_list):
                    uniq_list.append(new_arr)
    return uniq_list

test_arr = copy.deepcopy(arrangements_uniq)
arrangements_uniq = find_all(test_arr, arrangements_uniq)
curr_len = len(arrangements_uniq)
new_len = 0
while new_len != curr_len:
    curr_len = len(arrangements_uniq)
    test_arr = copy.deepcopy(arrangements_uniq)
    arrangements_uniq = find_all(test_arr, arrangements_uniq)
    new_len = len(arrangements_uniq)
    print(f"New len: {new_len} and Current len: {curr_len}")

for arr in arrangements_uniq:
    print(arr)
print(f"Number of unique arrangements: {len(arrangements_uniq)}")
"""