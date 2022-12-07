import array


MAHJONG_CHAR = "🀐🀑🀒🀓🀔🀕🀖🀗🀘"
MAHJONG_RANK_CHAR = "123456789"
MAHJONG_WIND_CHAR = "东西"


def show(tile_id):
    """返回对应牌面号的对应 Unicode 字符"""
    return MAHJONG_CHAR[tile_id // 4]


def show_ascii(tile_id):
    """返回对应牌面号的文字表示"""
    return MAHJONG_RANK_CHAR[tile_id // 4]


def get_face(tile_name) -> int:
    """将文字表示的牌转换为牌面号"""
    rank = int(tile_name) - 1
    return rank


def str_to_tiles_array(string):
    arr = array.array('B')
    for char in string:
        if char not in "123456789":
            continue
        arr.append(int(char)-1)
    return arr
