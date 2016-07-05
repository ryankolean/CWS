# Ryan Kolean
# marsRover.py

# Main class of the rover for handling set-up movement and position
class Rover():

    def __init__(self, position, direction):
        self.position = position
        self.position.set_grid_size(10,10)
        self.direction = direction

    def move(self, commands):
        for cmd in commands:
            if cmd == 'f':
                self.direction.forward(self.position)
            elif cmd == 'b':
                self.direction.backward(self.position)
            elif cmd == 'l':
                self.direction = self.direction.turn_left()
            elif cmd == 'r':
                self.direction = self.direction.turn_right()

    def get_position(self):
        return self.position

# Class for handling the 
class Position():

    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

    def set_grid_size(self, grid_size):
        self.grid_size = grid_size

    def is_finite_grid(self):
        return self.grid_size != (-1, -1)

    def __repr__(self):
        return "<Position x=%s, y=%s>" % (self.pos_x, self.pos_y)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return other.pos_x == self.pos_x and other.pos_y == self.pos_y
        else: 
            return False

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return other.pos_x != self.pos_x or other.pos_y != self.pos_y
        else:
            return True

    def down(self):
        if self.is_finite_grid() and self.pos_x-1 < self.grid_size[0] * -1:
            self.pos_x = self.grid_size[0]
        else:
            self.pos_x -= 1

    def up(self):
        if self.is_finite_grid() and self.pos_x+1 > self.grid_size[0]:
            self.pos_x = 0-self.grid_size[0]
        else:
            self.pos_x += 1

    def left(self):
        # negating grid size by multiplying with -1
        if self.is_finite_grid() and self.pos_y-1 < self.grid_size[1] * -1:
            self.pos_y = self.grid_size[1]
        else:
            self.pos_y -= 1

    def right(self):
        if self.is_finite_grid() and self.pos_y+1 > self.grid_size[1]:
            self.pos_y = 0-self.grid_size[1]
        else:
            self.pos_y += 1

class NorthDirection():

    def forward(self, position):
        return position.up()

    def backward(self, position):
        return position.down()

    def turn_left(self):
        return Direction.W

    def turn_right(self):
        return Direction.E

class WestDirection():

    def forward(self, position):
        return position.left()

    def backward(self, position):
        return position.right()

    def turn_right(self):
        return Direction.N

    def turn_left(self):
        return Direction.S

class EastDirection():

    def forward(self, position):
        return position.right()

    def backward(self, position):
        return position.left()

    def turn_right(self):
        return Direction.S

    def turn_left(self):
        return Direction.N

class SouthDirection():

    def forward(self, position):
        return position.down()

    def backward(self, position):
        return position.up()

    def turn_right(self):
        return Direction.W

    def turn_left(self):
        return Direction.E

class Direction():
    S = SouthDirection()
    N = NorthDirection()
    W = WestDirection()
    E = EastDirection()
