import copy

with open('input_7.txt') as fd:
    data_str = fd.read().splitlines()

bag_colors = {}
rules = {}
for rule in data_str:
    bag = rule.split('bags')[0].strip()
    bag_colors[bag] = 1
    remaining = rule.split('contain')[1].strip()
    rules[bag] = {}

    if remaining != "no other bags.":
        for item in remaining.split(','):
            remaining_part = item.strip().strip('.')
            remaining_qty = int(remaining_part.split(' ')[0])
            remaining_type = remaining_part.strip(str(remaining_qty)).strip('bags').strip('bag').strip().strip('.')
            rules[bag][remaining_type] = remaining_qty


def bag_that_contains(color, can_contain):
    for bag in rules.keys():
        for bags in rules[bag]:
            if bags == color:
                can_contain[bag] = 1
    return can_contain

# First check bags that can directly take color
color = "shiny gold"
can_contain = {}
can_contain = bag_that_contains(color, can_contain)

# Next check bags that can indirectly take color
bag_checking = copy.deepcopy(can_contain)
while True:
    bags_to_check = []
    for bag in bag_checking.keys():
        bags_to_check.append(bag)

    can_contain_output = {}
    for bag in bags_to_check:
        can_contain_output = bag_that_contains(bag, can_contain_output)

    if can_contain_output == {}:
        break
    else:
        for key in can_contain_output.keys():
            can_contain[key] = can_contain_output[key]
        bag_checking = copy.deepcopy(can_contain_output)

print(can_contain)
print(len(can_contain))