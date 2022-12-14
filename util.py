import array


MAHJONG_CHAR = "πππππππππ"
MAHJONG_RANK_CHAR = "123456789"
MAHJONG_WIND_CHAR = "δΈθ₯Ώ"


def show(tile_id):
    """θΏεε―ΉεΊηι’ε·ηε―ΉεΊ Unicode ε­η¬¦"""
    return MAHJONG_CHAR[tile_id // 4]


def show_ascii(tile_id):
    """θΏεε―ΉεΊηι’ε·ηζε­θ‘¨η€Ί"""
    return MAHJONG_RANK_CHAR[tile_id // 4]


def get_face(tile_name) -> int:
    """ε°ζε­θ‘¨η€Ίηηθ½¬ζ’δΈΊηι’ε·"""
    rank = int(tile_name) - 1
    return rank


def str_to_tiles_array(string):
    arr = array.array('B')
    for char in string:
        if char not in "123456789":
            continue
        arr.append(int(char)-1)
    return arr
