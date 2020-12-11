# Day 2 - Password Philosophy
# Part 2

# Read data from file into array
# Hard coded, can abstract filename as input
with open("input_2.txt", "r") as fd:
    data_str = fd.read().splitlines()

valid = False
valid_passwords = 0
for line in data_str:
    valid = False
    init_split = line.split('-')
    first_index = int(init_split[0]) - 1

    second_split = init_split[1].split(' ')
    second_index = int(second_split[0]) - 1

    char_verf = second_split[1].strip(':')
    password = second_split[2]

    if password[first_index] == char_verf or password[second_index] == char_verf:
        if password[first_index] == password[second_index]:
            valid = False
            pass
        else:
            valid_passwords += 1
            valid = True
    else:
        valid = False

    print(f"{first_index}\t{second_index}\t{char_verf}\t{password}\t{valid}")

print(f"Total valid passwords: {valid_passwords}")