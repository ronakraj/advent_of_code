# Day 7 - Handy Haversacks
# Part 1
import sys
import copy

# Read data from file into array
# Hard coded, can abstract filename as input
with open("sample_7.txt", "r") as fd:
    data_orig = fd.read().splitlines()

bags = {}
for line in data_orig:
    subject = line.split('bags')[0].strip()
    contain = line.split('contain')[1].strip().strip('.').split(',')

    bags[subject] = {}
    if not "no other bags" in contain:
        for bag in contain:
            bag_qty = bag.strip().split(' ')[0].strip()
            bag_desc = bag.split(bag_qty)[1].strip('bags').strip()
            bags[subject][bag_desc] = int(bag_qty)

desired_bag = "shiny gold"
global_count = 0
def calculate_bags(name, bags):
    global global_count, total_bags
    for bag in bags[name]:
        print(f"Bag: {name} has {bags[name][bag]}x{bag}")
        global_count += bags[name][bag] + bags[name][bag] * calculate_bags(bag, bags)
    return 0


print(calculate_bags(desired_bag, bags))
print(global_count)