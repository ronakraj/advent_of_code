# Day 9 - Encoding Error
# Part 1
import sys
import copy

# Read data from file into array
# Hard coded, can abstract filename as input
with open("input_9.txt", "r") as fd:
    data_orig = fd.read().splitlines()

numbers = []
for item in data_orig:
    numbers.append(int(item))

step = 25
low_index = 0
upper_index = low_index + step

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

for i in range(step, len(numbers) - 1):
    if not check_valid(numbers[low_index:upper_index], numbers[i]):
        print(f"Found number: {numbers[i]}")
        break

    upper_index += 1
    low_index += 1
