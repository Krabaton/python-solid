class Floor:
    def __init__(self):
        self.name = 'floor'

    def build(self):
        print(f'Build {self.name}')


class Ceiling:
    def __init__(self):
        self.name = 'ceiling'

    def build(self):
        print(f'Build {self.name}')


class Wall:
    def __init__(self):
        self.name = 'wall'

    def build(self):
        print(f'Build {self.name}')


class Building:
    def __init__(self):
        self.floor = None
        self.ceiling = None
        self.wall = None

    def inject_ceiling(self, ceiling):
        self.ceiling = ceiling

    def inject_floor(self, floor):
        self.floor = floor

    def inject_wall(self, wall):
        self.wall = wall


def build():
    house = Building()
    house.inject_wall(Wall())
    house.inject_ceiling(Ceiling())
    house.inject_floor(Floor())
    return house


house = build()
house.floor.build()
house.wall.build()
house.ceiling.build()
