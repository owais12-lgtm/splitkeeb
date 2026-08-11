import board
import busio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.oled import Oled, OledData

keyboard = KMKKeyboard()

keyboard.row_pins = (
    board.GP0,
    board.GP1,
    board.GP2,
    board.GP3,
    board.GP4,
    board.GP5,
)

keyboard.col_pins = (
    board.GP6,
    board.GP7,
    board.GP8,
    board.GP9,
    board.GP10,
    board.GP11,
    board.GP12,
    board.GP13,
    board.GP14,
    board.GP15,
    board.GP16,
    board.GP17,
    board.GP18,
    board.GP19,
    board.GP20,
    board.GP21,
)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.modules.append(Layers())
keyboard.extensions.append(MediaKeys())

encoder_handler = EncoderHandler()
encoder_handler.pins = ((board.GP22, board.GP28, None),)
keyboard.modules.append(encoder_handler)

oled = Oled(
    OledData(
        corner_one={0: OledData.oled_text_entry(text="Layer: BASE", x=0, y=0)},
        corner_two={0: OledData.oled_text_entry(text="KMK Ready", x=0, y=16)},
    ),
    toDisplay=OledData.LAYER,
    i2c=lambda: busio.I2C(board.GP27, board.GP26),
)
keyboard.modules.append(oled)

___ = KC.TRNS

BASE = (
    KC.ESC,  KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,   KC.F6,   KC.F7,   KC.F8,   KC.F9,   KC.F10,  KC.F11,  KC.F12,  KC.PSCR, KC.MUTE, KC.MPLY,
    KC.GRV,  KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,   KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.MINS, KC.EQL,  KC.BSPC, ___,     KC.DEL,
    KC.TAB,  KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,    KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    KC.LBRC, KC.RBRC, KC.BSLS, ___,     KC.PGUP,
    KC.CAPS, KC.A,    KC.S,    KC.D,    KC.F,    KC.G,    KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, KC.QUOT, ___,     KC.ENT,  ___,     KC.PGDN,
    KC.LSFT, ___,     KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,    KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH, ___,     KC.RSFT, KC.UP,   ___,
    KC.LCTL, KC.LGUI, KC.LALT, ___,     ___,     ___,     KC.SPC,  ___,     ___,     ___,     KC.RALT, KC.MO(1),KC.RCTL, KC.LEFT, KC.DOWN, KC.RGHT,
)

FN = (
    ___,     KC.BRID, KC.BRIU, KC.MCTL, ___,     ___,     ___,     KC.MPRV, KC.MPLY, KC.MNXT, KC.MUTE, KC.VOLD, KC.VOLU,
)

keyboard.keymap = [BASE, FN]

encoder_handler.map = (
    ((KC.VOLU, KC.VOLD),),
    ((KC.BRIU, KC.BRID),),
)

if __name__ == "__main__":
    keyboard.go()
