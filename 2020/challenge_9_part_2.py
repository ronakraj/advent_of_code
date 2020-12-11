# Day 9 - Encoding Error
# Part 2
import copy
import numpy as np

# Read data from file into array
# Hard coded, can abstract filename as input
with open("input_9.txt", "r") as fd:
    data_orig = fd.read().splitlines()

numbers = []
for item in data_orig:
    numbers.append(int(item))

low_index = 0
upper_index = 1

def check_valid(number_array, number):
    number_array.sort()
    lower = 0
    upper = len(number_array) - 1
    valid = False

    while upper > lower and lower <= upper:
        sum_numbers = number_array[upper] + number_array[lower]
        if sum_numbers == number:
            valid = True
            break
        elif sum_numbers > number:
            upper -= 1
        elif sum_numbers < number:
            lower += 1

    return valid

desired_sum = 542529149
#desired_sum = 127
current_sum = np.sum(numbers[low_index:upper_index])
while (current_sum != desired_sum and upper_index > low_index and low_index < upper_index):
    if current_sum < desired_sum:
        upper_index += 1
    elif current_sum > desired_sum:
        low_index += 1
    current_sum = np.sum(numbers[low_index:upper_index])

if current_sum == desired_sum:
    print("Found it!")
    print(f"Low index: {low_index}\tUpper index: {upper_index}")
    print(f"Min: {np.min(numbers[low_index:upper_index])}\tMax: {np.max(numbers[low_index:upper_index])}")
    print(f"Sum: {np.min(numbers[low_index:upper_index]) + np.max(numbers[low_index:upper_index])}")
else:
    print("Not found")