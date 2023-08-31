import board

from kb import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.extensions.stringy_keymaps import StringyKeymaps
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.modtap import ModTap

Iris = KMKKeyboard()

Iris.modules.append(Layers())
Iris.extensions.append(StringyKeymaps())
Iris.extensions.append(MediaKeys())
Iris.modules.append(ModTap())

# Layers
QWERTY = KC.DF(0)
COLEMAK = KC.DF(1)
GAME = KC.DF(5)
LOWER = KC.MO(2)
RAISE = KC.MO(3)
ADJUST = KC.MO(4)

# Keys
xx = "NO"
__ = "TRNS"
LGUI = KC.MT(KC.ENT, KC.LGUI)  # Enter when tapped, left GUI when held
LSFT = KC.MT(KC.Z, KC.LSFT)  # a when tapped, left shift when held
RSFT = KC.MT(KC.SLSH, KC.RSFT)
LLSFT = KC.MT(KC.AT, KC.LSFT)
LRSFT = KC.MT(KC.PIPE, KC.RSFT)

# fmt: off
Iris.keymap = [
    # layer 0, Qwerty
    [
            xx,      xx,     xx,     xx,    xx,    xx,    xx,     xx,      xx,      xx,      xx,      xx,
          'TAB',    'Q',    'W',    'E',   'R',   'T',   'Y',    'U',     'I',     'O',     'P',   'ESC',
         'BSPC',    'A',    'S',    'D',   'F',   'G',   'H',    'J',     'K',     'L',  'SCLN',  'QUOT',
             xx,   LSFT,    'X',    'C',   'V',   'B',   'N',    'M',  'COMM',   'DOT',    RSFT,      xx,
                        'LCTRL',  LOWER,  LGUI,    xx, 'SPC',  RAISE,  'LALT',
    ],
    # layer 1, Colemak
    [
             xx,    xx,     xx,     xx,    xx,    xx,    xx,     xx,      xx,      xx,      xx,      xx,
          'TAB',   'Q',    'W',    'F',   'P',   'B',   'J',    'L',     'U',     'Y',  'SCLN',   'ESC',
         'BSPC',   'A',    'R',    'S',   'T',   'G',   'M',    'N',     'E',     'I',     'O',  'QUOT',
             xx,  LSFT,    'X',    'C',   'D',   'V',   'K',    'H',  'COMM',   'DOT',    RSFT,      xx,
                       'LCTRL',  LOWER,  LGUI,   xx,  'SPC',  RAISE,  'LALT',
    ],
        # layer 2, LOWER
    [
            xx,     xx,    xx,     xx,    xx,      xx,      xx,     xx,      xx,      xx,      xx,      xx,
         'TAB',   'N0',  'N7',   'N8',  'N9',  'PLUS',  'HASH',  'DLR',  'PERC',  'CIRC',   'AMPR', 'ASTR',
        'BSNC', 'EXLM',  'N4',   'N5',  'N6',  'MINS',  'LPRN', 'RPRN',  'LBRC',  'RBRC',   'BSLS',  'GRV',
           xx,   LLSFT,  'N1',   'N2',  'N3',   'EQL',  'LCBR', 'RCBR',  'LABK',  'RABK',   LRSFT,     xx,
                           __,     __,     __,     xx,      __,    ADJUST,      __,
    ],


        # layer 3, RAISE
    [
          xx,     xx,     xx,       xx,    xx,    xx,      xx,      xx,      xx,       xx,      xx,    xx,
       'INS',     xx,   'F1',     'F2',  'F3',  'F4',  'VOLD',  'BRID',  'BRIU',   'VOLU',  'PSCR',    xx,
       'DEL',     xx,   'F5',     'F6',  'F7',  'F8',  'LEFT',  'DOWN',    'UP',  'RIGHT',  'MUTE',    xx,
          xx, 'LSFT',   'F9',    'F10', 'F11', 'F12',  'HOME',  'PGDN',  'PGUP',    'END',  'RSFT',    xx,
                          __,   ADJUST,    __,    xx,      __,      __,      __,
    ],
        # layer 4, ADJUST
    [
       xx,      xx,   xx,       xx,       xx,    xx,  xx,  xx,  xx,      xx,  xx,    xx,
       xx,  QWERTY,   xx,       xx,  'RESET',    xx,  xx,  xx,  xx,      xx,  xx,    xx,
       xx,      xx,   xx,  'DEBUG',       xx,    GAME,  xx,  xx,  xx,   'RLD',  xx,    xx,
       xx,      xx,   xx,  COLEMAK,       xx,    xx,  xx,  xx,  xx,      xx,  xx,    xx,
                      __,       __,       __,    xx,  __,  __,  __,
    ],
    [
        # layer 5, GAME
            xx,      xx,     xx,     xx,    xx,    xx,    xx,     xx,      xx,      xx,      xx,      xx,
          'ESC',    'Q',    'W',    'E',   'R',   'T',   'Y',    'U',     'I',     'O',     'P',   'ESC',
         'ENT',    'A',    'S',    'D',   'F',   'G',   'H',    'J',     'K',     'L',  'SCLN',   ADJUST,
             xx,    'Z',    'X',    'C',   'V',   'B',   'N',    'M',  'COMM',   'DOT',    RSFT,      xx,
                        'LCTRL',  'LSFT',  'SPC',  xx, 'BSPC',  'LGUI',  'LALT',
    ],

    
]


if __name__ == "__main__":
    Iris.go()
