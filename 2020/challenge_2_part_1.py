# Day 2 - Password Philosophy
# Part 1

# Read data from file into array
# Hard coded, can abstract filename as input
with open("input_2.txt", "r") as fd:
    data_str = fd.read().splitlines()

valid = False
valid_passwords = 0
for line in data_str:
    valid = False
    init_split = line.split('-')
    lower_limit = int(init_split[0])

    second_split = init_split[1].split(' ')
    upper_limit = int(second_split[0])

    char_verf = second_split[1].strip(':')

    password = second_split[2]

    found_char = 0
    for char in password:
        if char == char_verf:
            found_char += 1

    if found_char >= lower_limit and found_char <= upper_limit:
        valid_passwords += 1
        valid = True
    else:
        valid = False

    print(f"{lower_limit}\t{upper_limit}\t{char_verf}\t{password}\t{found_char}\t{valid}")

print(f"Total valid passwords: {valid_passwords}")