# Day 12 - Rain Risk
# Part 1

class MapMover():
    def __init__(self):
        self.attributes = {'x_pos': 0,
                           'y_pos': 0,
                           'dir': 'E'}
        self.directions = ['N', 'E', 'S', 'W']
        self.dir_act = {'N': self.move_north,
                        'S': self.move_south,
                        'E': self.move_east,
                        'W': self.move_west,
                        'L': self.move_left,
                        'R': self.move_right,
                        'F': self.move_forward}

    def move_north(self, value):
        self.attributes['y_pos'] += value

    def move_south(self, value):
        self.attributes['y_pos'] -= value

    def move_east(self, value):
        self.attributes['x_pos'] += value

    def move_west(self, value):
        self.attributes['x_pos'] -= value

    def move_forward(self, value):
        self.dir_act[self.attributes['dir']](value)

    def move_left(self, value):
        current_index = self.directions.index(self.attributes['dir'])
        for i in range(int(value / 90)):
            current_index = ((current_index - 1) % len(self.directions))
        self.attributes['dir'] = self.directions[current_index]

    def move_right(self, value):
        current_index = self.directions.index(self.attributes['dir'])
        for i in range(int(value / 90)):
            current_index = ((current_index + 1) % len(self.directions))
        self.attributes['dir'] = self.directions[current_index]

    def manhatten_dist(self):
        return (abs(self.attributes['x_pos']) + abs(self.attributes['y_pos']))

# Read data from file into array
# Hard coded, can abstract filename as input
with open("input_12.txt", "r") as fd:
    data = fd.read().splitlines()

map_mover = MapMover()
for move in data:
    action = move[0]
    value = int(move[1:])
    map_mover.dir_act[action](value)

print(f"Manhatten distance: {map_mover.manhatten_dist()}")
