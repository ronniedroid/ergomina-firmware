import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation


class KMKKeyboard(_KMKKeyboard):
    row_pins = (board.GP1, board.GP2, board.GP4, board.GP6, board.GP5)
    col_pins = (
        board.GP9,
        board.GP7,
        board.GP11,
        board.GP13,
        board.GP14,
        board.GP15,
        board.GP16,
        board.GP19,
        board.GP22,
        board.GP21,
        board.GP26,
        board.GP17,
    )

    diode_orientation = DiodeOrientation.COL2ROW

    # flake8: noqa
    # fmt: off
    coord_mapping = [
         0,  1,  2,  3,  4,   5,  6,  7,  8,  9, 10, 11,
        12, 13, 14, 15, 16,  17, 18, 19, 20, 21, 22, 23,
        24, 25, 26, 27, 28,  29, 30, 31, 32, 33, 34, 35,
        36, 37, 38, 39, 40,  41, 42, 43, 44, 45, 46, 47,
                50, 51, 52,  53, 54, 55, 56
     ]
