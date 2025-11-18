from abc import ABC, abstractmethod
from enum import Enum


class WayType(Enum):
    ShortWay = 1
    LongWay = 2


def go_x_y(x: int, y: int):
    # быстрее но дороже
    result = []
    for i in range(1, x + 1):
        result.append((i, 0))

    for i in range(1, y + 1):
        result.append((x, i))

    return result


def go_y_x(y: int, x: int):
    # дешевле но дольше
    result = []
    for i in range(1, y + 1):
        result.append((0, i))

    for i in range(1, x + 1):
        result.append((i, y))
    return result


class Strategy(ABC):
    @abstractmethod
    def find_way(self):
        pass


class ShortWay(Strategy):

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def find_way(self):
        # быстрее но дороже
        result = []
        for i in range(1, self.x + 1):
            result.append((i, 0))

        for i in range(1, self.y + 1):
            result.append((self.x, i))

        return result


class LongWay(Strategy):
    def __init__(self, y: int, x: int):
        self.y = y
        self.x = x

    def find_way(self):
        # дешевле но дольше
        result = []
        for i in range(1, self.y + 1):
            result.append((0, i))

        for i in range(1, self.x + 1):
            result.append((i, self.y))
        return result


class WayFactory:
    @classmethod
    def create(cls, way_type: WayType, x, y) -> Strategy:
        if way_type == WayType.LongWay:
            return LongWay(y, x)
        elif way_type == WayType.ShortWay:
            return ShortWay(x, y)


class SelectWay:
    def __init__(self, way: Strategy):
        self.way = way

    def find_path(self):
        return self.way.find_way()


way = WayFactory.create(WayType.ShortWay, 3, 4)
select_way = SelectWay(way)
print(select_way.find_path())
