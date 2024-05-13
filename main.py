import board

from kb import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.extensions.stringy_keymaps import StringyKeymaps
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.holdtap import HoldTap

Ergomina = KMKKeyboard()

Ergomina.modules.append(Layers())
Ergomina.extensions.append(StringyKeymaps())
Ergomina.extensions.append(MediaKeys())
Ergomina.modules.append(HoldTap())

Ergomina.debug_enabled = True

# Layers
QWERTY = KC.DF(0)
COLEMAK = KC.DF(1)
LOWER = KC.MO(2)
RAISE = KC.MO(3)

# Keys
xx = "NO"
__ = "TRNS"
LGUI = KC.HT(KC.ENT, KC.LM(4, KC.LGUI), prefer_hold=True, tap_interrupted=False, tap_time=250)  # Enter when tapped, left GUI when held
LSFT = KC.HT(KC.Z, KC.LSFT)  # a when tapped, left shift when held
RSFT = KC.HT(KC.SLSH, KC.RSFT)
LLSFT = KC.HT(KC.AT, KC.LSFT)
LRSFT = KC.HT(KC.PIPE, KC.RSFT)
# Gnome macros
MWSR = KC.PGDN  # Move to right workspace 
MWSL = KC.PGUP  # Move to left workspace 
MWSF = KC.HOME # Move to the first workspace 
MWSE = KC.END # Move to the last workspace 
KWIN = KC.W  # Kill window
SAPP = KC.TAB # Switch apps
SWIN = KC.GRV # Switch windows
HWIN = KC.H # Hide window
TERM = KC.T # Open terminal
OVIEW = KC.X # Open overview
MWIN = KC.UP # Toggle maximization
RWIN = KC.DOWN # Restore window size
CWIN = KC.C # Move window to center (tiling assistant)
TWL = KC.LEFT # Tile window to the left
TWR = KC.RIGHT # Tile window to the right
TWTL = KC.P7 # Tile window top left
TWTR = KC.P9 # Tile window top left
TWBL = KC.P1 # Tile window top left
TWBR = KC.P3 # Tile window top left
APPS = KC.A # Show all apps
NOTIF = KC.V # Show the notification list
QMENU = KC.S # Show the quick settings menu
RUN = KC.R # Show the run command prompt
SLANG = KC.SPC # Switch input language

# fmt: off
Ergomina.keymap = [
    # layer 0, Qwerty
    [
          'TAB',    'Q',    'W',    'E',   'R',   'T',   'Y',    'U',     'I',     'O',     'P',   'ESC',
         'BSPC',    'A',    'S',    'D',   'F',   'G',   'H',    'J',     'K',     'L',  'SCLN',  'QUOT',
             xx,   LSFT,    'X',    'C',   'V',   'B',   'N',    'M',  'COMM',   'DOT',    RSFT,      xx,
                        'LCTRL',  LOWER,  LGUI,    xx, 'SPC',  RAISE,  'LALT',
    ],
    # layer 1, Colemak
    [
          'TAB',   'Q',    'W',    'F',   'P',   'B',   'J',    'L',     'U',     'Y',  'SCLN',   'ESC',
         'BSPC',   'A',    'R',    'S',   'T',   'G',   'M',    'N',     'E',     'I',     'O',  'QUOT',
             xx,  LSFT,    'X',    'C',   'D',   'V',   'K',    'H',  'COMM',   'DOT',    RSFT,      xx,
                       'LCTRL',  LOWER,  LGUI,   xx,  'SPC',  RAISE,  'LALT',
    ],
        # layer 2, LOWER
    [
         'TAB',   'N0',  'N7',   'N8',  'N9',  'PLUS',  'HASH',  'DLR',  'PERC',  'CIRC',   'AMPR', 'ASTR',
        'BSNC', 'EXLM',  'N4',   'N5',  'N6',  'MINS',  'LPRN', 'RPRN',  'LBRC',  'RBRC',   'BSLS',  'GRV',
           xx,   LLSFT,  'N1',   'N2',  'N3',   'EQL',  'LCBR', 'RCBR',  'LABK',  'RABK',   LRSFT,     xx,
                           __,     __,     'LGUI',     xx,      __,    __,      __,
    ],


        # layer 3, RAISE
    [
       'INS',  QWERTY,   'F1',     'F2',  'F3',  'F4',  'VOLD',  'BRID',  'BRIU',   'VOLU',  'PSCR',    xx,
       'DEL', COLEMAK,   'F5',     'F6',  'F7',  'F8',  'LEFT',  'DOWN',    'UP',  'RIGHT',  'MUTE',    xx,
          xx,  'LSFT',   'F9',    'F10', 'F11', 'F12',  'HOME',  'PGDN',  'PGUP',    'END',  'RSFT',    xx,
                          __,   __,    'LGUI',    xx,      __,      __,      __,
    ],
        # layer 4, Gnome
    [
     SAPP,    KWIN,     SWIN,       xx,    RUN,  TERM,   TWTL,  TWBL,  TWBR,   TWTR, 'PSCR',     xx,
     HWIN,    APPS,    QMENU,       xx,     xx,    xx,    TWL,  RWIN,  MWIN,    TWR,   CWIN,     xx,
       xx,  'LSFT',    OVIEW,       xx,  NOTIF,    xx,   MWSF,  MWSL,  MWSR,   MWSE,     xx,     xx,
                          __,       __,     __,    xx,  SLANG,    __,    __,
    ],
]


if __name__ == "__main__":
    Ergomina.go()
