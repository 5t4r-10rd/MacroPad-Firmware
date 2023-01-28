print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.handlers.sequences import send_string, simple_key_sequence
from kmk.modules.encoder import EncoderHandler
from kmk.modules.tapdance import TapDance
from kmk.extensions.media_keys import MediaKeys

# KEYTBOARD SETUP
keyboard = KMKKeyboard()
encoder_handler = EncoderHandler()
tapdance = TapDance()
tapdance.tap_time = 250
keyboard.modules = [tapdance, encoder_handler]

# SWITCH MATRIX
keyboard.col_pins = (board.GP22, board.GP13, board.GP17)
keyboard.row_pins = (board.GP24, board.GP18)
keyboard.diode_orientation = DiodeOrientation.COLUMNS

# ENCODERS
encoder_handler.pins = ((board.GP2, board.GP0, None, True, 2),)

#### EXTENSIONS ####
keyboard.debug_enabled = False
keyboard.extensions.append(MediaKeys())


#### MACROS ####

# Browser
BROWSER = KC.X
INSPECT = simple_key_sequence([KC.LCTRL(KC.LSHIFT(KC.I))])
HARD_RELOAD = simple_key_sequence([KC.LCTRL(KC.LSHIFT(KC.R))])

# Media
PLAY_PAUSE = KC.MEDIA_PLAY_PAUSE
NEXT_TRACK = KC.MEDIA_NEXT_TRACK
PREV_TRACK = KC.MEDIA_PREV_TRACK
VOL_UP = KC.AUDIO_VOL_UP
VOL_DOWN = KC.AUDIO_VOL_DOWN

_______ = KC.TRNS
xxxxxxx = KC.NO


# KEYMAPS
keyboard.keymap = [
    [
        PLAY_PAUSE, PREV_TRACK, NEXT_TRACK,
        KC.D, KC.E, KC.F
    ],
]

encoder_handler.map = [ ((VOL_DOWN, VOL_UP, KC.AUDIO_MUTE),) ]



if __name__ == '__main__':
    keyboard.go()