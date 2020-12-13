# Challenge 4 - Passport Processing
# Part 1
import numpy as np
import sys

with open('input_4_2.txt') as fd:
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
            return 0
    return 1

def valid_fields(storage):
    try:
        byr = int(storage['byr']) 
        iyr = int(storage['iyr'])
        eyr = int(storage['eyr'])
        pid = int(storage['pid'])
    except ValueError:
        return 0
    
    if not (byr >= 1920 and byr <= 2002):
        return 0

    if not (iyr >= 2010 and iyr <= 2020):
        return 0

    if not (eyr >= 2020 and eyr <= 2030):
        return 0

    if 'cm' in storage['hgt']:
        hgt = int(storage['hgt'].split('cm')[0])
        if not (hgt >= 150 and hgt <= 193):
            return 0
    elif 'in' in storage['hgt']:
        hgt = int(storage['hgt'].split('in')[0])
        if not (hgt >= 59 and hgt <= 76):
            return 0
    else:
        return 0

    if storage['hcl'][0] != '#':
        return 0
    
    hex_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    hcl = storage['hcl'][1:]
    for elem in hcl:
        if elem not in hex_list:
            return 0
    
    eye_list = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if storage['ecl'] not in eye_list:
        return 0

    if len(storage['pid']) != 9:
        return 0

    pid_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for elem in storage['pid']:
        if elem not in pid_list:
            return 0

    return 1

valid_passports = 0
current_dict = fields
for item in data_str:
    if item == '':
        if check_valid(current_dict):
            valid_passports += valid_fields(current_dict)
        for key in current_dict: 
            current_dict[key] = ''
    else:
        current_dict = analyse(item, current_dict)

print(f"Valid passports: {valid_passports}")