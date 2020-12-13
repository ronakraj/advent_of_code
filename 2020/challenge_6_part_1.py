# Challenge 6 
# Part 1

with open('input_6.txt') as fd:
    data_str = fd.read().splitlines()

stores = {}
counts = 0
group_members = 0
for item in data_str:
    if item == '':
        for key in stores:
            if stores[key] == group_members:
                counts += 1
        for key in stores:
            stores[key] = 0
        group_members = 0 
    else:
        group_members += 1
        for question in item:
            if question in stores: 
                stores[question] += 1
            else:
                stores[question] = 1

print(f"Total: {counts}")