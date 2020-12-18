# Day 13 - Shuttle Search
# Part 1

# Read data from file into array
# Hard coded, can abstract filename as input
with open("sample_13.txt", "r") as fd:
    data = fd.read().splitlines()

schedule = data[1]
busses = {}
for idx, bus in enumerate(schedule.split(',')):
    if bus != 'x':
        busses[int(bus)] = -idx % int(bus)

print(busses)

iterator = 0
increment = 1
for bus in busses.keys():
    while iterator % bus != busses[bus]:
        iterator += increment
    increment *= bus

print(f"Iterator: {iterator}")