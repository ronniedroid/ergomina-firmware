import board

from kb import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.extensions.stringy_keymaps import StringyKeymaps
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.capsword import CapsWord

PlanckHW = KMKKeyboard()

PlanckHW.modules.append(Layers())
PlanckHW.modules.append(CapsWord())
PlanckHW.extensions.append(StringyKeymaps())
PlanckHW.extensions.append(MediaKeys())

# Layers
QWERTY = KC.DF(0)
COLEMAK = KC.DF(1)
LOWER = KC.MO(2)
RAISE = KC.MO(3)

# Keys
xx = "NO"
__ = "TRNS"
LALT = KC.MT(KC.ENT, KC.LALT)  # Enter when tapped, left Alt when held
LCTL = KC.MT(KC.SPC, KC.LCTL)  # Space when tapped, left Ctrl when held
cut = KC.LCTL(KC.X)
copy = KC.LCTL(KC.C)
paste = KC.LCTL(KC.V)
MWSR = KC.LGUI(KC.PGDN)  # Move to right workspace (Gnome)
MWSL = KC.LGUI(KC.PGUP)  # Move to left workspace (Gnome)
MWWSR = KC.LGUI(KC.RSFT(KC.PGDN))  # Move window to right workspace (Gnome)
MWWSL = KC.LGUI(KC.RSFT(KC.PGUP))  # Move window to left workspace (Gnome)
MWMR = KC.LGUI(KC.RSFT(KC.RIGHT))  # Move window to right monitor (Gnome)
MWML = KC.LGUI(KC.RSFT(KC.LEFT))  # Move window to left monitor (Gnome)
KLW = KC.LALT(KC.F4)  # Kill window

# fmt: off
PlanckHW.keymap = [
    # layer 0, Qwerty
    [
        'GRAVE',   'N1',   'N2',   'N3',  'N4',  'N5',  'N6',   'N7',    'N8',    'N9',    'N0',  'LBRC',
          'TAB',    'Q',    'W',    'E',   'R',   'T',   'Y',    'U',     'I',     'O',     'P',  'RBRC',
         'BSPC',    'A',    'S',    'D',   'F',   'G',   'H',    'J',     'K',     'L',  'SCLN',  'QUOT',
         'LSFT',    'Z',    'X',    'C',   'V',   'B',   'N',    'M',  'COMM',   'DOT',  'SLSH',  'RSFT',
                        'LGUI',  LOWER,  LALT,  'ESC',  LCTL,  RAISE,  'RALT',
    ],
    # layer 1, Colemak
    [
        'GRAVE',  'N1',   'N2',   'N3',  'N4',  'N5',  'N6',   'N7',    'N8',    'N9',    'N0',  'LBRC',
          'TAB',   'Q',    'W',    'F',   'P',   'B',   'J',    'L',     'U',     'Y',  'SCLN',  'RBRC',
         'BSPC',   'A',    'R',    'S',   'T',   'G',   'M',    'N',     'E',     'I',     'o',  'QUOT',
         'LSFT',   'Z',    'X',    'C',   'D',   'V',   'K',    'H',  'COMM',   'DOT',  'SLSH',  'RSFT',
                        'LGUI',  LOWER,  LALT, 'ESC',  LCTL,  RAISE,  'RALT',
    ],
        # layer 2, LOWER
    [
            xx,   'P1',   'P2',   'P3',   'P4',   'P5',    'P6',   'P7',    'P8',    'P9',     'P0',      xx,
         'TAB', 'EXLM',   'AT', 'HASH',  'DLR', 'GRAVE', 'LABK', 'LCBR',  'RCRR',  'LBRC',   'RBRC',  'BSLS',
        'BSPC', 'PERC', 'CIRC', 'AMPR', 'ASTR',     xx,  'RABK', 'LPRN',  'RPRN',   'EQL',   'PLUS',  'QUOT',
        'LSFT',     xx,    cut,   copy,  paste,     xx,      xx,     __,      __,      __,   'MINS',  'RSFT',
                            __,     __,     __,     __,      __,     xx,      __,
    ],
        # layer 3, RAISE
    [
            xx,    'F1', 'F2',   'F3',   'F4',   'F5',   'F6',   'F7',    'F8',   'F9',   'F10',  'F11',
       'RESET',  QWERTY, 'CW', 'BRIU', 'VOLU', 'MUTE', 'PSCR',  'INS',  'PGDN', 'PGUP',   'DEL',  'F12',
      'RELOAD', COLEMAK,   xx, 'BRID', 'VOLD', 'MPLY', 'HOME', 'LEFT',  'DOWN',   'UP', 'RIGHT',  'END',
       'DEBUG',      xx,   xx,    KLW,     xx,     xx,   MWSR,   MWSL,   MWWSR,  MWWSL,    MWML,   MWMR,
                           __,     __,     __,     __,     __,     xx,      __,
    ],
]



if __name__ == "__main__":
    PlanckHW.go()
