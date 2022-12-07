import array
from copy import copy

zeros = array.array('b', [0 for _ in range(9)])


class Yaku:
    def __init__(self, name: str, han: int):
        self.name = name
        self.han = han


class Yakuman:
    def __init__(self, name: str):
        self.name = name


class Han:
    def __init__(self, tile_faces: array.array):
        self.is_win = False
        self.han = []
        self.yakuman = []
        self.score = 0
        self.tile_faces = tile_faces

    def append_yaku(self, name, han):
        self.han.append(Yaku(name, han))

    def append_yakuman(self, name):
        self.yakuman.append(Yakuman(name))

    def remove_yaku(self, name):
        for yaku in self.han:
            if yaku.name == name:
                self.han.remove(yaku)
                break

    def check_win(self, riichi: int = 0, tsumo: bool = 0):
        """判定是否和牌"""
        # 建立长度为 9 的空数组 tiles_map，统计各牌张数
        tiles_map = copy(zeros)
        for t in self.tile_faces:
            tiles_map[t] += 1
            # 若出现大于 4 张的牌，则为检查听牌时出现虚听
            if tiles_map[t] > 4:
                return False
        if riichi == 2:
            self.append_yaku("两立直", 2)
        elif riichi == 1:
            self.append_yaku("立直", 1)
        if tsumo:
            self.append_yaku("自摸", 1)
        self.append_yaku("清一色", 6)
        if tiles_map[0] == 0 and tiles_map[8] == 0:
            self.append_yaku("断幺九", 1)
        if tiles_map[0] > 3 and tiles_map[8] > 3 and 0 not in tiles_map:
            self.append_yakuman("九莲宝灯")
        self.win_7(tiles_map)
        self.win_normal(tiles_map, tsumo)

    def win_7(self, m: array):
        """判定是否和七对型"""
        # counts = [0, 0, 0, 0, 0]
        # for i in range(34):
        #     counts[m[i]] += 1
        # return counts == [27, 0, 7, 0, 0]
        for t in m:
            if t != 0 and t != 0:
                return
        self.append_yaku("七对子", 2)
        self.is_win = True

    def win_normal(self, m: array, tsumo: bool):
        """判定是否和一般型"""
        # 轮流判断各牌是否可以作为雀头 (数量 > 2)
        # 若得到雀头，则移除并进入内层判断
        for pair in range(9):
            if m[pair] >= 2:
                m2 = copy(m)
                m2[pair] -= 2

                # 刻子
                tri = array.array('B')
                # 顺子
                seq = array.array('B')

                for curr_tile in range(9):
                    if m2[curr_tile] >= 3:
                        tri.append(curr_tile)
                        m2[curr_tile] -= 3
                    elif m2[curr_tile] == 2 and curr_tile < 7:
                        seq.append(curr_tile)
                        seq.append(curr_tile)
                        m2[curr_tile] -= 2
                        m2[curr_tile + 1] -= 2
                        m2[curr_tile + 2] -= 2
                    if m2[curr_tile] == 1 and curr_tile < 7:
                        seq.append(curr_tile)
                        m2[curr_tile] -= 1
                        m2[curr_tile + 1] -= 1
                        m2[curr_tile + 2] -= 1
                    if m2[curr_tile] != 0:
                        break
                if m2 == zeros:
                    self.is_win = True
                    if len(tri) == 4:
                        if tsumo:
                            self.append_yakuman("四暗刻")
                        else:
                            self.append_yaku("对对和", 2)
                            self.append_yaku("三暗刻", 2)
                    elif len(tri) == 3:
                        self.append_yaku("三暗刻", 2)
                    if len(seq) == 4:
                        if seq[0] == seq[1] and seq[2] == seq[3]:
                            self.append_yaku("两杯口", 3)
                            self.remove_yaku("七对子")
                        elif seq[0] == seq[1] or seq[1] == seq[2] or seq[2] == seq[3]:
                            self.append_yaku("一杯口", 1)
                    if len(seq) == 3 and (seq[0] == seq[1] or seq[1] == seq[2]):
                        self.append_yaku("一杯口", 1)
                    if len(seq) == 2 and seq[0] == seq[1]:
                        self.append_yaku("一杯口", 1)
                    if {0, 3, 6} <= set(seq):
                        self.append_yaku("一气通贯", 2)
                    if set(tri) <= {0, 8} and set(seq) <= {0, 6}:
                        self.append_yaku("纯全带幺九", 3)
                    if set(tri) <= {1, 2, 3, 5, 7} and set(seq) <= {1}:
                        self.append_yakuman("绿一色")
                    return

    def stat(self):
        scores = {
            4: 8000,
            6: 12000,
            7: 12000,
            8: 16000,
            9: 16000,
            10: 16000,
            11: 24000,
            12: 24000,
            13: 32000
        }

        if self.yakuman:
            for entry in self.yakuman:
                print(entry.name)
            self.score = len(self.yakuman) * 32000
        else:
            han = 0
            for entry in self.han:
                print(f'{entry.name} {entry.han}番')
                han += entry.han
            if han >= 13:
                self.score = 13
            else:
                self.score = scores[han]


def discard_check_win(tile_faces, discard = 0):
    """判定能否听牌，不考虑役种"""
    # 建立长度为 9 的空数组 tiles_map，统计各牌张数
    tiles_map = copy(zeros)
    for t in tile_faces:
        tiles_map[t] += 1
        # 若出现大于 4 张的牌，则为检查听牌时出现虚听
        if tiles_map[t] > 4:
            return False
    win_7(tiles_map)
    win_normal(tiles_map)