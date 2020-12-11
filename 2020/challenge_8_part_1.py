# Day 3 - Handheld Halting
# Part 1
import sys
import copy

# Read data from file into array
# Hard coded, can abstract filename as input
with open("input_8.txt", "r") as fd:
    data_orig = fd.read().splitlines()

def check_loop(data_str):
    start_acc = 0
    step_index = 0
    steps_performed = []
    failed = False

    while step_index < len(data_str):
        if step_index in steps_performed:
            print("Repeated loop found")
            failed = True
            break

        steps_performed.append(step_index)
        step = data_str[step_index]
        instruction = step.split(' ')[0].strip()
        value = step.split(' ')[1].strip()
        value_sign = value[0]
        value_qty = int(value[1:])

        if instruction == 'acc':
            if value_sign == '+':
                start_acc += value_qty
            elif value_sign == '-':
                start_acc -= value_qty
            else:
                print("INVALID OPERATOR")
                sys.exit(1)
            step_index += 1

        elif instruction == 'nop':
            step_index += 1

        elif instruction == 'jmp':
            if value_sign == '+':
                step_index += value_qty
            elif value_sign == '-':
                step_index -= value_qty
            else:
                print("INVALID STEP")
                sys.exit(1)
        else:
            print("INVALID INSTRUCTION")
            sys.exit(1)

    return failed, start_acc

data_copy = copy.deepcopy(data_orig)
index = 0
for line in data_orig:
    failed = False
    start_acc = 0
    if "jmp" in line:
        data_copy[index] = line.replace("jmp", "nop")
        failed, start_acc = check_loop(data_copy)

        if failed == False:
            print("SUCCESS!")
            print("")
            print(f"Acc: {start_acc}")
            break
        else:
            data_copy[index] = line

    elif "nop" in line:
        data_copy[index] = line.replace("nop", "jmp")
        failed, start_acc = check_loop(data_copy)

        if failed == False:
            print("SUCCESS!")
            print(f"Acc: {start_acc}")
            break
        else:
            data_copy[index] = line

    index += 1