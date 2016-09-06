from collections import namedtuple

PositionParent = namedtuple('PositionParent', ['x', 'y'])


class Position(PositionParent):
    def get_neighbors(self):
        set_of_neighbors = set()
        for i in range(self.x - 1, self.x + 2):
            for j in range(self.y - 1, self.y + 2):
                if i != self.x or j != self.y:
                    set_of_neighbors.add(Position(i, j))
        return set_of_neighbors
