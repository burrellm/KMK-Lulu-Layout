from kb import KMKKeyboard
from storage import getmount
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.mouse_keys import MouseKeys
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.lock_status import LockStatus
from kmk.hid import HIDModes
from kmk.handlers.sequences import send_string
import supervisor
from kmk.extensions.peg_oled_Display import Oled,OledDisplayMode,OledReactionType,OledData
from kmk.extensions.RGB import RGB
from kmk.modules.split import Split, SplitSide, SplitType
keyboard = KMKKeyboard()
layers_ext = Layers()
locks = LockStatus()
keyboard.modules.append(layers_ext)
keyboard.extensions.append(locks)
keyboard.modules.append(MouseKeys())
keyboard.extensions.append(MediaKeys())
#keyboard.debug_enabled = True

# TODO Comment one of these on each side
#split_side = SplitSide.LEFT
#split_side = SplitSide.RIGHT
split = Split(data_pin=keyboard.rx, data_pin2=keyboard.tx, uart_flip=False)
keyboard.modules.append(split)

side = SplitSide.RIGHT if str(getmount('/').label)[-1] == 'R' else SplitSide.LEFT
# codeblock
"""
Enable HoldTap
This codeblock enables HoldTap to be used on the device.
"""
from kmk.modules.holdtap import HoldTap
from kmk.modules.holdtap import HoldTapRepeat
holdtap = HoldTap()
# optional: set a custom tap timeout in ms
holdtap.tap_time = 200
keyboard.modules.append(holdtap)
# codeblock
# codeblock
"""
Enable TapDance
This codeblock enables TapDance to be used on the device.
"""
from kmk.modules.tapdance import TapDance
tapdance = TapDance()
tapdance.tap_time = 200
keyboard.modules.append(tapdance)
# codeblock
# oled
oled_ext = Oled(
    OledData(
        corner_one={0:OledReactionType.STATIC,1:["layer"]},
        corner_two={0:OledReactionType.LAYER,1:["0","1","2","3","4","5","6"]},
        corner_three={0:OledReactionType.LAYER,1:["Base","Base","Game","Navigation","Mouse","Media","Game"]},
        corner_four={0:OledReactionType.LAYER,1:["qwerty","sturdy","Layer","Numbers","Symbols","Functions","Mirror"]}
        ),
        toDisplay=OledDisplayMode.TXT,flip=False)# oled
keyboard.extensions.append(oled_ext)
# rgb
rgb = RGB(pixel_pin=keyboard.rgb_pixel_pin, num_pixels=35, hue_default=0, sat_default=0, val_default=0)
keyboard.extensions.append(rgb)

class RgbLayers(Layers):
    last_top_layer = 0
    hues = (135, 135, 135, 224, 64, 0, 165, 96, 100, 192, 32)
    underglow = [0, 1, 2, 3, 4, 5]
    wasdglow = [14, 20, 21, 22]
    numpadglow = [14,15,16,21,20,19,26,27,28]
    thumbglow = [34, 33, 32, 31, 66, 67, 68, 69]
    def after_hid_send(self, keyboard):
        if keyboard.active_layers[0] != self.last_top_layer:
            self.last_top_layer = keyboard.active_layers[0]
            rgb.disable_auto_write=True
            for i in self.underglow:
                rgb.set_hsv(self.hues[self.last_top_layer], 255, 255, i)
            if self.last_top_layer in [2, 3, 4, 5, 6] and side == SplitSide.LEFT:
                for i in self.wasdglow:
                    rgb.set_hsv(self.hues[self.last_top_layer + 1], 255, 255, i)
            else:
                if side == SplitSide.LEFT:
                    for i in self.wasdglow:
                        rgb.set_hsv(0, 0, 0, i)
            if self.last_top_layer in [3, 4, 5] and side == SplitSide.RIGHT:
                for i in self.numpadglow:
                    rgb.set_hsv(self.hues[self.last_top_layer + 1], 255, 255, i)
            else:
                if side == SplitSide.RIGHT:
                    for i in self.numpadglow:
                        rgb.set_hsv(0, 0, 0, i)
            if locks.get_caps_lock():
                for i in self.thumbglow:
                    rgb.set_hsv(self.hues[self.last_top_layer + 1], 255, 255, i)
            else:
                for i in self.thumbglow:
                    rgb.set_hsv(0, 0, 0, i)
            rgb.show()

keyboard.modules.append(RgbLayers())
#rgb

# encodercount
# 2
# encodercount
# keymap
keyboard.keymap = [
    #0 QWERTY
    [
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
        KC.NO, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.NO,
        KC.NO, KC.HT(KC.A, KC.LGUI, prefer_hold=False, tap_interrupted=True, repeat=HoldTapRepeat.TAP), KC.HT(KC.S, KC.LALT, prefer_hold=False, tap_interrupted=True, repeat=HoldTapRepeat.TAP), KC.HT(KC.D, KC.LCTL, prefer_hold=False, tap_interrupted=True, repeat=HoldTapRepeat.TAP), KC.HT(KC.F, KC.LSFT, prefer_hold=False, tap_interrupted=True, repeat=HoldTapRepeat.TAP), KC.G, KC.H, KC.HT(KC.J, KC.LSFT, prefer_hold=False, tap_interrupted=True, repeat=HoldTapRepeat.TAP), KC.HT(KC.K, KC.LCTL, prefer_hold=False, tap_interrupted=True, repeat=HoldTapRepeat.TAP), KC.HT(KC.L, KC.LALT, prefer_hold=False, tap_interrupted=True, repeat=HoldTapRepeat.TAP), KC.HT(KC.SCLN, KC.LGUI, prefer_hold=False, tap_interrupted=True, repeat=HoldTapRepeat.TAP), KC.NO,
        KC.NO, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.MUTE, KC.MPLY, KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH, KC.NO,
        KC.TG(2), KC.LT(5, KC.ESC, prefer_hold=False, tap_interrupted=True, repeat=HoldTapRepeat.TAP), KC.LT(3, KC.SPC, prefer_hold=False, tap_interrupted=True, repeat=HoldTapRepeat.TAP), KC.LT(4, KC.TAB, prefer_hold=False, tap_interrupted=True, repeat=HoldTapRepeat.TAP), KC.LT(4, KC.ENT, prefer_hold=False, tap_interrupted=True, repeat=HoldTapRepeat.TAP), KC.LT(3, KC.BSPC, prefer_hold=False, tap_interrupted=True, repeat=HoldTapRepeat.TAP), KC.LT(5, KC.DEL, prefer_hold=False, tap_interrupted=True, repeat=HoldTapRepeat.TAP), KC.TO(1),
        KC.VOLD,
        KC.VOLU,
        KC.MPRV,
        KC.MNXT
    ],
    #1 STRDY
    [
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
        KC.NO, KC.V, KC.M, KC.L, KC.C, KC.P, KC.X, KC.F, KC.O, KC.U, KC.J, KC.NO,
        KC.NO, KC.HT(KC.S, KC.LGUI, prefer_hold=False, tap_interrupted=True, repeat=HoldTapRepeat.TAP), KC.HT(KC.T, KC.LALT, prefer_hold=False, tap_interrupted=True, repeat=HoldTapRepeat.TAP), KC.HT(KC.R, KC.LCTL, prefer_hold=False, tap_interrupted=True, repeat=HoldTapRepeat.TAP), KC.HT(KC.D, KC.LSFT, prefer_hold=False, tap_interrupted=True, repeat=HoldTapRepeat.TAP), KC.Y, KC.DOT, KC.HT(KC.N, KC.LSFT, prefer_hold=False, tap_interrupted=True, repeat=HoldTapRepeat.TAP), KC.HT(KC.A, KC.LCTL, prefer_hold=False, tap_interrupted=True, repeat=HoldTapRepeat.TAP), KC.HT(KC.E, KC.LALT, prefer_hold=False, tap_interrupted=True, repeat=HoldTapRepeat.TAP), KC.HT(KC.I, KC.LGUI, prefer_hold=False, tap_interrupted=True, repeat=HoldTapRepeat.TAP), KC.NO,
        KC.NO, KC.Z, KC.K, KC.Q, KC.G, KC.W, KC.MUTE, KC.MPLY, KC.B, KC.H, KC.QUOT, KC.SCLN, KC.COMM, KC.NO,
        KC.TG(2), KC.LT(5, KC.ESC, prefer_hold=False, tap_interrupted=True, repeat=HoldTapRepeat.TAP), KC.LT(3, KC.SPC, prefer_hold=False, tap_interrupted=True, repeat=HoldTapRepeat.TAP), KC.LT(4, KC.TAB, prefer_hold=False, tap_interrupted=True, repeat=HoldTapRepeat.TAP), KC.LT(4, KC.ENT, prefer_hold=False, tap_interrupted=True, repeat=HoldTapRepeat.TAP), KC.LT(3, KC.BSPC, prefer_hold=False, tap_interrupted=True, repeat=HoldTapRepeat.TAP), KC.LT(5, KC.DEL, prefer_hold=False, tap_interrupted=True, repeat=HoldTapRepeat.TAP), KC.TO(0),
        KC.VOLD,
        KC.VOLU,
        KC.MPRV,
        KC.MNXT
    ],
    #2 GAME
    [
        KC.GRV, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.BSPC,
        KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.BSLS,
        KC.ESC, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.ENT,
        KC.LSFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.MUTE, KC.MPLY, KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH, KC.RSFT,
        KC.TG(2), KC.LCTL, KC.SPC, KC.MO(6), KC.ENT, KC.BSPC, KC.DEL, KC.TG(2),
        KC.VOLD,
        KC.VOLU,
        KC.MPRV,
        KC.MNXT
    ],
    #3 Nav Numbers
    [
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
        KC.NO, KC.HOME, KC.UP, KC.END, KC.PGUP, KC.INS, KC.LBRC, KC.N7, KC.N8, KC.N9, KC.RBRC, KC.NO,
        KC.NO, KC.LEFT, KC.DOWN, KC.RGHT, KC.PGDN, KC.CAPS, KC.EQL, KC.N4, KC.N5, KC.N6, KC.GRV, KC.NO,
        KC.NO, KC.LCTL(KC.Z), KC.LCTL(KC.X), KC.LCTL(KC.C), KC.LCTL(KC.V), KC.LCTL(KC.Y), KC.TRNS, KC.TRNS, KC.BSLS, KC.N1, KC.N2, KC.N3, KC.SLSH, KC.NO,
        KC.NO, KC.ESC, KC.SPC, KC.TAB, KC.MINS, KC.N0, KC.DOT, KC.NO,
        KC.VOLD,
        KC.VOLU,
        KC.MPRV,
        KC.MNXT
    ],
    #4 Mouse Symbols
    [
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
        KC.NO, KC.NO, KC.MS_UP, KC.NO, KC.MW_UP, KC.MB_BTN4, KC.LCBR, KC.AMPR, KC.ASTR, KC.LPRN, KC.RCBR, KC.NO,
        KC.NO, KC.MS_LT, KC.MS_DN, KC.MS_RT, KC.MW_DN, KC.MB_BTN5, KC.PLUS, KC.DLR, KC.PERC, KC.CIRC, KC.TILD, KC.NO,
        KC.NO, KC.LCTL(KC.A), KC.LCTL(KC.S), KC.LCTL(KC.N), KC.LCTL(KC.F), KC.LCTL(KC.W), KC.TRNS, KC.TRNS, KC.PIPE, KC.EXLM, KC.AT, KC.HASH, KC.QUES, KC.NO,
        KC.NO, KC.MB_MMB, KC.MB_LMB, KC.MB_RMB, KC.UNDS, KC.LPRN, KC.RPRN, KC.NO,
        KC.VOLD,
        KC.VOLU,
        KC.MPRV,
        KC.MNXT
    ],
    #5 Media Functions
    [
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
        KC.NO, KC.TD(KC.NO, KC.RESET), KC.VOLU, KC.NO, KC.NO, KC.NO, KC.PSCR, KC.F7, KC.F8, KC.F9, KC.F12, KC.NO,
        KC.NO, KC.MPRV, KC.VOLD, KC.MNXT, KC.NO, KC.NO, KC.SLCK, KC.F4, KC.F5, KC.F6, KC.F11, KC.NO,
        KC.NO, KC.RGB_TOG, KC.RGB_MODE_PLAIN, KC.RGB_MODE_BREATHE, KC.RGB_MODE_RAINBOW, KC.RGB_MODE_KNIGHT, KC.TRNS, KC.TRNS, KC.PAUS, KC.F1, KC.F2, KC.F3, KC.F10, KC.NO,
        KC.NO, KC.MUTE, KC.MPLY, KC.MSTP, KC.ENT, KC.BSPC, KC.APP, KC.NO,
        KC.VOLD,
        KC.VOLU,
        KC.MPRV,
        KC.MNXT
    ],
    #6 GAME_2
    [
        KC.BSPC, KC.N0,  KC.N9, KC.N8, KC.N7, KC.N6, KC.N5, KC.N4, KC.N3, KC.N2, KC.N1, KC.GRV,
        KC.BSLS, KC.P,  KC.O, KC.I, KC.U, KC.Y, KC.T, KC.R, KC.E, KC.W, KC.Q, KC.TAB,
        KC.ENT, KC.SCLN,  KC.L, KC.K, KC.J, KC.H, KC.G, KC.F, KC.D, KC.S, KC.A, KC.ESC,
        KC.RSFT, KC.SLSH, KC.DOT, KC.COMM, KC.M, KC.N, KC.TRNS, KC.TRNS, KC.B, KC.V, KC.C, KC.X, KC.Z, KC.LSFT,
        KC.TG(2), KC.LCTL, KC.SPC, KC.MO(6), KC.ENT, KC.BSPC, KC.DEL, KC.TG(2),
        KC.VOLD,
        KC.VOLU,
        KC.MPRV,
        KC.MNXT
    ]
]
# keymap
if __name__ == '__main__': 
    keyboard.go(hid_type=HIDModes.USB)