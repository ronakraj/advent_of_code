# Day 3 - Toboggan Trajectory
# Part 1

# Read data from file into array
# Hard coded, can abstract filename as input
with open("input_3.txt", "r") as fd:
    data_str = fd.read().splitlines()

map_orig = []
for row in data_str:
    new_row = []
    for item in row:
        new_row.append(item)
    map_orig.append(new_row)

# Create map repetition three times due to arboreal genetics and biome stability
map_repeated = []
for item in map_orig:
    map_repeated.append(item * 10000)

pos_x = 3
pos_y = 1
tree_count = 0

while(pos_y < len(map_repeated) and pos_x < len(map_repeated[0])):
    if map_repeated[pos_y][pos_x] == '#':
        tree_count += 1

    pos_x += 3
    pos_y += 1

print(f"Trees found: {tree_count}")
print(f"Position Y: {pos_y} Max Y: {len(map_repeated)}")