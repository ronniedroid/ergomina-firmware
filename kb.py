import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation


class KMKKeyboard(_KMKKeyboard):
    col_pins = (board.GP0, board.GP1, board.GP2, board.GP3, board.GP4)
    row_pins = (
        board.GP5,
        board.GP6,
        board.GP7,
        board.GP8,
        board.GP9,
        board.GP16,
        board.GP17,
        board.GP18,
        board.GP19,
        board.GP20,
        board.GP21,
        board.GP22,
    )

    diode_orientation = DiodeOrientation.COL2ROW

    # flake8: noqa
    # fmt: off
    coord_mapping = [
         0,  1,  2,  3,  4,  5,  35, 34, 33, 32, 31, 30,
         6,  7,  8,  9, 10, 11,  41, 40, 39, 38, 37, 36,
        12, 13, 14, 15, 16, 17,  47, 47, 45, 44, 43, 42,
        18, 19, 20, 21, 22, 23,  53, 52, 51, 50, 49, 48,
                26, 27, 28, 29,  59, 58, 57,
     ]
