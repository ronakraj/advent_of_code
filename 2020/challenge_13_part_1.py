# Day 13 - Shuttle Search
# Part 1

# Read data from file into array
# Hard coded, can abstract filename as input
with open("input_13.txt", "r") as fd:
    data = fd.read().splitlines()

earliest_timestamp = int(data[0])
schedule = data[1]
buses = []

for id in schedule.split(','):
    if id != 'x':
        buses.append(int(id))

buses.sort()
modulos = {}
for bus in buses:
    modulos[(bus * int(earliest_timestamp / bus)) + bus - earliest_timestamp] = bus

min_time = min(modulos.keys())
min_bus = modulos[min_time]

print(f"Earliest bus: {min_bus}\nTime wait: {min_time}\nID * Time: {min_bus*min_time}")