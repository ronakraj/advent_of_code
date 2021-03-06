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

# First check bags that can directly take color
color = "shiny gold"
total_bags = 0
color_check = color

def total_bags_in_color(color):
    total = 0
    for bag in rules[color]:
        total += rules[color][bag]
    return total

def bag_in_color(color, total=1, last_multiple=1):
    global total_bags
    if rules[color] != {}:
        total = last_multiple * total_bags_in_color(color)
        for bag in rules[color]:
            print(f"Checking inside {color} and found {bag}")
            print(f"{last_multiple} * {rules[color][bag]}\ttotal: {total}")
            bag_in_color(bag, total, last_multiple * rules[color][bag]) 
        print(f"DONE: {total}")
        total_bags += total

bag_in_color(color_check)
print(total_bags)