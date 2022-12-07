import array
import random
from util import *
from yaku import *


class Hand:
    """手牌类"""

    def __init__(self, wind=0):
        """初始化手牌。创建手牌数组及设定自风"""
        self.tiles = []
        self.wind = wind

    def draw(self, new_tile):
        """摸牌。将牌插入手牌中"""
        self.tiles.append(new_tile)

    def sort(self):
        """理牌。将手牌以顺序排列"""
        self.tiles.sort()

    def discard(self, index) -> int:
        """出牌。按手牌数组索引移除并返回对应牌
        若非摸切（打出第 13 张），则理牌
        """
        t = self.tiles.pop(index)
        if index != 13:
            self.sort()
        print(f"{MAHJONG_WIND_CHAR[self.wind]}: {show(t)}{show_ascii(t)}")
        return t

    def discard_by_face(self, face) -> bool:
        """按牌面出牌。输入牌面编号以打出手牌中第一张对应牌。
        若成功找到并打出，则返回 True；否则返回 False
        """
        for i in range(14):
            if self.tiles[i] // 4 == face:
                self.discard(i)
                return True
        return False

    def win(self) -> Han:
        """判定和牌。和牌则返回 True，否则返回 False"""
        tiles_faces = array.array('B')
        for t in self.tiles:
            tiles_faces.append(t // 4)
        return Han(tiles_faces)

    def print(self, add_str: str = ''):
        """打印手牌字符串"""
        output = ""
        for t in self.tiles:
            output += show(t)
        print(output)
        output = ""
        for t in self.tiles:
            output += show_ascii(t)
        print(output, add_str)


class HandAuto(Hand):
    def is_win(self):
        """判定是否自动和牌。和牌则返回 True，否则返回 False"""
        tiles_faces = array.array('B')
        for t in self.tiles:
            tiles_faces.append(t // 4)
        han = Han(tiles_faces)
        han.check_win()
        return han.is_win

    def tenpai(self):
        """找到打出后能听牌的牌"""
        ...


class Wall:
    """牌山类"""

    def __init__(self):
        """初始化牌山。新建牌山数组并打乱"""
        self.wall = array.array('B', range(36))
        random.shuffle(self.wall)

    def get(self) -> int:
        """摸牌。弹出当前牌山的第一张作为返回值"""
        return self.wall.pop(0)

    def is_empty(self) -> bool:
        """判断牌山是否摸完。摸完返回 True，否则返回 False"""
        return not self.wall

    def wall_remain(self) -> int:
        return len(self.wall)

    def print_wall(self):
        """打印牌山数组"""
        print(self.wall.tolist())


class MahjongError(Exception):
    def __init__(self, expression='', message=''):
        self.expression = expression
        self.message = message
