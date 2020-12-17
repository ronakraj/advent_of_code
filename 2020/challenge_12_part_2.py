# Day 12 - Rain Risk
# Part 2
import copy

class MapMover():
    def __init__(self):
        self.attributes = {'x_pos': 0,
                           'y_pos': 0}
        self.wavepoint = {'x_pos': 10,
                          'y_pos': 1}
        self.dir_act = {'N': self.move_north,
                        'S': self.move_south,
                        'E': self.move_east,
                        'W': self.move_west,
                        'L': self.move_left,
                        'R': self.move_right,
                        'F': self.move_forward}

    def move_north(self, value):
        self.wavepoint['y_pos'] += value

    def move_south(self, value):
        self.wavepoint['y_pos'] -= value

    def move_east(self, value):
        self.wavepoint['x_pos'] += value

    def move_west(self, value):
        self.wavepoint['x_pos'] -= value

    def move_forward(self, value):
        self.attributes['x_pos'] += value * self.wavepoint['x_pos']
        self.attributes['y_pos'] += value * self.wavepoint['y_pos']

    def move_left(self, value):
        for i in range(int(value / 90)):
            x_pos = copy.deepcopy(self.wavepoint['x_pos'])
            y_pos = copy.deepcopy(self.wavepoint['y_pos'])
            self.wavepoint['x_pos'] = -1 * y_pos
            self.wavepoint['y_pos'] = x_pos

    def move_right(self, value):
        for i in range(int(value / 90)):
            x_pos = copy.deepcopy(self.wavepoint['x_pos'])
            y_pos = copy.deepcopy(self.wavepoint['y_pos'])
            self.wavepoint['x_pos'] = y_pos
            self.wavepoint['y_pos'] = -1 * x_pos

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
    print(f"Ship: {map_mover.attributes}\tWavepoint: {map_mover.wavepoint}")

print(f"Manhatten distance: {map_mover.manhatten_dist()}")
