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

def trees_found(map_repeated, start_y, start_x, slope_y, slope_x):
    tree_count = 0
    pos_x = start_x
    pos_y = start_y

    while(pos_y < len(map_repeated) and pos_x < len(map_repeated[0])):
        if map_repeated[pos_y][pos_x] == '#':
            tree_count += 1

        pos_x += slope_x
        pos_y += slope_y

    return tree_count


# Right 1, down 1.
tree_count_1 = trees_found(map_repeated, 1, 1, 1, 1)
# Right 3, down 1. (This is the slope you already checked.)
tree_count_2 = trees_found(map_repeated, 1, 3, 1, 3)
# Right 5, down 1.
tree_count_3 = trees_found(map_repeated, 1, 5, 1, 5)
# Right 7, down 1.
tree_count_4 = trees_found(map_repeated, 1, 7, 1, 7)
# Right 1, down 2.
tree_count_5 = trees_found(map_repeated, 2, 1, 2, 1)


print(f"Trees found 1: {tree_count_1}\t2: {tree_count_2}\t3: {tree_count_3}\t4: {tree_count_4}\t5: {tree_count_5}")
print(f"Multiplied: {tree_count_1 * tree_count_2 * tree_count_3 * tree_count_4 * tree_count_5}")