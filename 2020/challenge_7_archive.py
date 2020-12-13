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


"""
def bags_recursion(color, bag, mult):
    if rules[color][bag] == {}:
        return 0

    else:
        return mult * bags_recursion(color, bag, rules[color][bag])
"""

def bags_in_color(color, qty):
    for bag in rules[color].keys():
        print(bag)
        print(rules[bag])

        for next_color in rules[bag].keys():
            print(next_color)
            print(rules[next_color])
    return 0

# First check bags that can directly take color
color = "shiny gold"
color_check = color
total_bags = 0

print(bags_in_color(color_check, 0))

while True:
    for bag in rules[color_check]:
        print(rules[bag].keys())