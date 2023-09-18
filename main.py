# import board
from kb import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.modules.power import Power
from kmk.modules.mouse_keys import MouseKeys
from kmk.modules.capsword import CapsWord
from kmk.extensions.media_keys import MediaKeys
from kmk.hid import HIDModes
from kmk.handlers.sequences import send_string
import supervisor
from kmk.extensions.peg_oled_Display import Oled,OledDisplayMode,OledReactionType,OledData
from kmk.modules.split import Split, SplitSide, SplitType
from kmk.extensions.RGB import RGB

keyboard = KMKKeyboard()
keyboard.modules.append(Power())
keyboard.modules.append(MouseKeys())
keyboard.modules.append(CapsWord())
keyboard.extensions.append(MediaKeys())
keyboard.modules.append(Layers())
keyboard.modules.append(ModTap())

# codeblock
"""
Enable HoldTap
This codeblock enables HoldTap to be used on the device.
"""
from kmk.modules.holdtap import HoldTap
holdtap = HoldTap()
# optional: set a custom tap timeout in ms
holdtap.tap_time = 200
prefer_hold=True
tap_interrupted=False
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
oled_ext = Oled( OledData(image={0:OledReactionType.LAYER,1:["QWERTY.bmp","STRDY.bmp","GAME.bmp","SHORTCUT.bmp","NAVIGATION.bmp","MOUSE.bmp","MEDIA.bmp","NUMBERS.bmp","SYMBOLS.bmp","FUNCTIONS.bmp","GAME_2.bmp"]}),toDisplay=OledDisplayMode.IMG,flip=False)
# oled
keyboard.extensions.append(oled_ext)



# TODO Comment one of these on each side
split_side = SplitSide.LEFT
#split_side = SplitSide.RIGHT
split = Split(data_pin=keyboard.rx, data_pin2=keyboard.tx, uart_flip=False)
keyboard.modules.append(split)
# encodercount
# 2
# encodercount
# keymap
keyboard.keymap = keyboard.keymap = [
#0 QWERTY
    [
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
        KC.NO, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.NO,
        KC.NO, KC.MT(KC.A, KC.LGUI, prefer_hold=False, tap_interrupted=True), KC.MT(KC.S, KC.LALT, prefer_hold=False, tap_interrupted=True), KC.MT(KC.D, KC.LCTL, prefer_hold=False, tap_interrupted=True), KC.MT(KC.F, KC.LSFT, prefer_hold=False, tap_interrupted=True), KC.G, KC.H, KC.MT(KC.J, KC.LSFT, prefer_hold=False, tap_interrupted=True), KC.MT(KC.K, KC.LCTL, prefer_hold=False, tap_interrupted=True), KC.MT(KC.L, KC.LALT, prefer_hold=False, tap_interrupted=True), KC.MT(KC.SCLN, KC.LGUI, prefer_hold=False, tap_interrupted=True), KC.NO,
        KC.NO, KC.LT(3, KC.Z), KC.MT(KC.X, KC.RALT, prefer_hold=False, tap_interrupted=True), KC.C, KC.V, KC.B, KC.MUTE, KC.MPLY, KC.N, KC.M, KC.COMM, KC.MT(KC.DOT, KC.RALT, prefer_hold=False, tap_interrupted=True), KC.LT(3, KC.SLSH), KC.NO,
        KC.TG(2), KC.LT(9, KC.ESC), KC.LT(7, KC.SPC), KC.LT(8, KC.TAB), KC.LT(5, KC.ENT), KC.LT(4, KC.BSPC), KC.LT(6, KC.DEL), KC.TO(1),
        KC.VOLD,
        KC.VOLU,
        KC.MPRV,
        KC.MNXT
    ],
    #1 STRDY
    [
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
        KC.NO, KC.V, KC.M, KC.L, KC.C, KC.P, KC.X, KC.F, KC.O, KC.U, KC.J, KC.NO,
        KC.NO, KC.MT(KC.S, KC.LGUI, prefer_hold=False, tap_interrupted=True), KC.MT(KC.T, KC.LALT, prefer_hold=False, tap_interrupted=True), KC.MT(KC.R, KC.LCTL, prefer_hold=False, tap_interrupted=True), KC.MT(KC.D, KC.LSFT, prefer_hold=False, tap_interrupted=True), KC.Y, KC.DOT, KC.MT(KC.N, KC.LSFT, prefer_hold=False, tap_interrupted=True), KC.MT(KC.A, KC.LCTL, prefer_hold=False, tap_interrupted=True), KC.MT(KC.E, KC.LALT, prefer_hold=False, tap_interrupted=True), KC.MT(KC.I, KC.LGUI, prefer_hold=False, tap_interrupted=True), KC.NO,
        KC.NO, KC.LT(3, KC.Z), KC.MT(KC.K, KC.RALT, prefer_hold=False, tap_interrupted=True), KC.Q, KC.G, KC.W, KC.TRNS, KC.TRNS, KC.B, KC.H, KC.QUOT, KC.MT(KC.SCLN, KC.RALT, prefer_hold=False, tap_interrupted=True), KC.LT(3, KC.COMM), KC.NO,
        KC.TG(2), KC.LT(9, KC.ESC), KC.LT(7, KC.SPC), KC.LT(8, KC.TAB), KC.LT(5, KC.ENT), KC.LT(4, KC.BSPC), KC.LT(6, KC.DEL), KC.TO(0),
        KC.TRNS,
        KC.TRNS,
        KC.TRNS,
        KC.TRNS
    ],
    #2 GAME
    [
        KC.GRV, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.BSPC,
        KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.BSLS,
        KC.ESC, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.ENT,
        KC.LSFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.TRNS, KC.TRNS, KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH, KC.RSFT,
        KC.TG(2), KC.LCTL, KC.SPC, KC.MO(10), KC.ENT, KC.BSPC, KC.DEL, KC.TG(2),
        KC.TRNS,
        KC.TRNS,
        KC.TRNS,
        KC.TRNS
    ],
    #3 SHORTCUT
    [
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
        KC.NO, KC.LCTL(KC.Z), KC.LCTL(KC.X), KC.LCTL(KC.C), KC.LCTL(KC.V), KC.LCTL(KC.Y), KC.LCTL(KC.Y), KC.LCTL(KC.V), KC.LCTL(KC.C), KC.LCTL(KC.X), KC.LCTL(KC.Z), KC.NO,
        KC.NO, KC.LGUI, KC.LALT, KC.LCTL, KC.LSFT, KC.NO, KC.NO, KC.LSFT, KC.LCTL, KC.LALT, KC.LGUI, KC.NO,
        KC.NO, KC.LCTL(KC.Z), KC.LCTL(KC.X), KC.LCTL(KC.C), KC.LCTL(KC.V), KC.LCTL(KC.Y), KC.TRNS, KC.TRNS, KC.LCTL(KC.Y), KC.LCTL(KC.V), KC.LCTL(KC.C), KC.LCTL(KC.X), KC.LCTL(KC.Z), KC.NO,
        KC.NO, KC.MB_MMB, KC.MB_LMB, KC.MB_RMB, KC.MB_RMB, KC.MB_LMB, KC.MB_MMB, KC.NO,
        KC.TRNS,
        KC.TRNS,
        KC.TRNS,
        KC.TRNS
    ],
    #4 NAVIGATION
    [
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
        KC.NO, KC.HOME, KC.UP, KC.END, KC.PGUP, KC.INS, KC.NO, KC.TD(KC.NO, KC.DF(0)), KC.TD(KC.NO, KC.DF(1)), KC.TD(KC.NO, KC.DF(2)), KC.TD(KC.NO, KC.RESET), KC.NO,
        KC.NO, KC.LEFT, KC.DOWN, KC.RGHT, KC.PGDN, KC.TD(KC.CW, KC.CAPS), KC.NO, KC.LSFT, KC.LCTL, KC.LALT, KC.LGUI, KC.NO,
        KC.NO, KC.LCTL(KC.Z), KC.LCTL(KC.X), KC.LCTL(KC.C), KC.LCTL(KC.V), KC.LCTL(KC.Y), KC.TRNS, KC.TRNS, KC.NO, KC.TD(KC.NO, KC.DF(4)), KC.TD(KC.NO, KC.DF(7)), KC.RALT, KC.NO, KC.NO,
        KC.NO, KC.ESC, KC.SPC, KC.TAB, KC.NO, KC.NO, KC.NO, KC.NO,
        KC.TRNS,
        KC.TRNS,
        KC.TRNS,
        KC.TRNS
    ],
    #5 MOUSE
    [
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
        KC.NO, KC.NO, KC.MS_UP, KC.NO, KC.MW_UP, KC.NO, KC.NO, KC.TD(KC.NO, KC.DF(0)), KC.TD(KC.NO, KC.DF(1)), KC.TD(KC.NO, KC.DF(2)), KC.TD(KC.NO, KC.RESET), KC.NO,
        KC.NO, KC.MS_LT, KC.MS_DN, KC.MS_RT, KC.MW_DN, KC.NO, KC.NO, KC.LSFT, KC.LCTL, KC.LALT, KC.LGUI, KC.NO,
        KC.NO, KC.LCTL(KC.Z), KC.LCTL(KC.X), KC.LCTL(KC.C), KC.LCTL(KC.V), KC.LCTL(KC.Y), KC.TRNS, KC.TRNS, KC.NO, KC.TD(KC.NO, KC.DF(5)), KC.TD(KC.NO, KC.DF(8)), KC.RALT, KC.NO, KC.NO,
        KC.NO, KC.MB_MMB, KC.MB_LMB, KC.MB_RMB, KC.NO, KC.NO, KC.NO, KC.NO,
        KC.TRNS,
        KC.TRNS,
        KC.TRNS,
        KC.TRNS
    ],
    #6 MEDIA
    [
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
        KC.NO, KC.NO, KC.NO, KC.VOLU, KC.NO, KC.NO, KC.NO, KC.TD(KC.NO, KC.DF(0)), KC.TD(KC.NO, KC.DF(1)), KC.TD(KC.NO, KC.DF(2)), KC.TD(KC.NO, KC.RESET), KC.NO,
        KC.NO, KC.NO, KC.MPRV, KC.VOLD, KC.MNXT, KC.NO, KC.NO, KC.LSFT, KC.LCTL, KC.LALT, KC.LGUI, KC.NO,
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.TRNS, KC.TRNS, KC.NO, KC.TD(KC.NO, KC.DF(6)), KC.TD(KC.NO, KC.DF(9)), KC.RALT, KC.NO, KC.NO,
        KC.NO, KC.MUTE, KC.MPLY, KC.MSTP, KC.NO, KC.NO, KC.NO, KC.NO,
        KC.TRNS,
        KC.TRNS,
        KC.TRNS,
        KC.TRNS
    ],
    #7 NUMBERS
    [
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
        KC.NO, KC.TD(KC.NO, KC.RESET), KC.TD(KC.NO, KC.DF(2)), KC.TD(KC.NO, KC.DF(1)), KC.TD(KC.NO, KC.DF(0)), KC.NO, KC.LBRC, KC.N7, KC.N8, KC.N9, KC.RBRC, KC.NO,
        KC.NO, KC.LGUI, KC.LALT, KC.LCTL, KC.LSFT, KC.NO, KC.EQL, KC.N4, KC.N5, KC.N6, KC.GRV, KC.NO,
        KC.NO, KC.NO, KC.RALT, KC.TD(KC.NO, KC.DF(4)), KC.TD(KC.NO, KC.DF(7)), KC.NO, KC.TRNS, KC.TRNS, KC.BSLS, KC.N1, KC.N2, KC.N3, KC.SLSH, KC.NO,
        KC.NO, KC.NO, KC.NO, KC.NO, KC.MINS, KC.N0, KC.DOT, KC.NO,
        KC.TRNS,
        KC.TRNS,
        KC.TRNS,
        KC.TRNS
    ],
    #8 SYMBOLS
    [
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
        KC.NO, KC.TD(KC.NO, KC.RESET), KC.TD(KC.NO, KC.DF(2)), KC.TD(KC.NO, KC.DF(1)), KC.TD(KC.NO, KC.DF(0)), KC.NO, KC.LCBR, KC.AMPR, KC.ASTR, KC.LPRN, KC.RCBR, KC.NO,
        KC.NO, KC.LGUI, KC.LALT, KC.LCTL, KC.LSFT, KC.NO, KC.PLUS, KC.DLR, KC.PERC, KC.CIRC, KC.TILD, KC.NO,
        KC.NO, KC.NO, KC.RALT, KC.TD(KC.NO, KC.DF(5)), KC.TD(KC.NO, KC.DF(8)), KC.NO, KC.TRNS, KC.TRNS, KC.PIPE, KC.EXLM, KC.AT, KC.HASH, KC.QUES, KC.NO,
        KC.NO, KC.NO, KC.NO, KC.NO, KC.UNDS, KC.LPRN, KC.RPRN, KC.NO,
        KC.TRNS,
        KC.TRNS,
        KC.TRNS,
        KC.TRNS
    ],
    #9 FUNCTIONS
    [
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
        KC.NO, KC.TD(KC.NO, KC.RESET), KC.TD(KC.NO, KC.DF(2)), KC.TD(KC.NO, KC.DF(1)), KC.TD(KC.NO, KC.DF(0)), KC.NO, KC.PSCR, KC.F7, KC.F8, KC.F9, KC.F12, KC.NO,
        KC.NO, KC.LGUI, KC.LALT, KC.LCTL, KC.LSFT, KC.NO, KC.SLCK, KC.F4, KC.F5, KC.F6, KC.F11, KC.NO,
        KC.NO, KC.NO, KC.RALT, KC.TD(KC.NO, KC.DF(6)), KC.TD(KC.NO, KC.DF(9)), KC.NO, KC.TRNS, KC.TRNS, KC.PAUS, KC.F1, KC.F2, KC.F3, KC.F10, KC.NO,
        KC.NO, KC.NO, KC.NO, KC.NO, KC.ENT, KC.BSPC, KC.APP, KC.NO,
        KC.TRNS,
        KC.TRNS,
        KC.TRNS,
        KC.TRNS
    ],
    #10 GAME_2
    [
        KC.BSPC, KC.N0,  KC.N9, KC.N8, KC.N7, KC.N6, KC.N5, KC.N4, KC.N3, KC.N2, KC.N1, KC.GRV,
        KC.BSLS, KC.P,  KC.O, KC.I, KC.U, KC.Y, KC.T, KC.R, KC.E, KC.W, KC.Q, KC.TAB,
        KC.ENT, KC.SCLN,  KC.L, KC.K, KC.J, KC.H, KC.G, KC.F, KC.D, KC.S, KC.A, KC.ESC,
        KC.RSFT, KC.SLSH, KC.DOT, KC.COMM, KC.M, KC.N, KC.TRNS, KC.TRNS, KC.B, KC.V, KC.C, KC.X, KC.Z, KC.LSFT,
        KC.TG(2), KC.LCTL, KC.SPC, KC.MO(10), KC.ENT, KC.BSPC, KC.DEL, KC.TG(2),
        KC.TRNS,
        KC.TRNS,
        KC.TRNS,
        KC.TRNS
    ]
]

# rgb
rgb = RGB(pixel_pin=keyboard.rgb_pixel_pin, num_pixels=35, hue_default=0, sat_default=0, val_default=0)
keyboard.extensions.append(rgb)

class RgbLayers(Layers):
    last_top_layer = 0
    hues = (135, 135, 135, 224, 64, 0, 165, 96, 100, 192, 32)
    underglow = [0, 1, 2, 3, 4, 5]
    def after_hid_send(self, keyboard):
        if keyboard.active_layers[0] != self.last_top_layer:
            self.last_top_layer = keyboard.active_layers[0]
            rgb.disable_auto_write=True
            for i in self.underglow:
                rgb.set_hsv(self.hues[self.last_top_layer], 255, 255, i)
            rgb.show()

keyboard.modules.append(RgbLayers())

# keymap
if __name__ == '__main__': 
    keyboard.go(hid_type=HIDModes.USB)