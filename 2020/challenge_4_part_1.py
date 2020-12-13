# Challenge 4 - Passport Processing
# Part 1
import numpy as np
import sys

with open('input_4.txt') as fd:
    data_str = fd.read().splitlines()

fields = {'byr': '',
          'iyr': '',
          'eyr': '',
          'hgt': '',
          'hcl': '',
          'ecl': '',
          'pid': '',
          'cid': ''}

def analyse(item, storage):
    for field in item.split(' '):
        storage[field.split(':')[0]] = field.split(':')[1]

    return storage

def check_valid(storage):
    for key in storage:
        if storage[key] == '' and key != 'cid':
            print(f"Not valid: {storage}")
            return 0
    return 1

valid_passports = 0
current_dict = fields
for item in data_str:
    if item == '':
        valid_passports += check_valid(current_dict)
        for key in current_dict: 
            current_dict[key] = ''
    else:
        current_dict = analyse(item, current_dict)

print(f"Valid passports: {valid_passports}")