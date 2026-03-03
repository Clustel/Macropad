import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.rgb import RGB

keyboard = KMKKeyboard()

keyboard.col_pins = (board.D10, board.D9, board.D8, board.D7)
keyboard.row_pins = (board.D0, board.D1, board.D2, board.D3)
keyboard.diode_orientation = DiodeOrientation.COL2ROW 

encoder_handler = EncoderHandler()
encoder_handler.pins = ((board.D5, board.D6, None, False),) 
keyboard.modules.append(encoder_handler)

rgb = RGB(
    pixel_pin=board.D4, 
    num_pixels=16,       
    val_limit=150,      
    hue_default=160,     
    sat_default=255,
    val_default=100,
)
keyboard.extensions.append(rgb)

keyboard.keymap = [
    [
        KC.N7, KC.N8, KC.N9, KC.MUTE, 
        KC.N4, KC.N5, KC.N6, KC.A,    
        KC.N1, KC.N2, KC.N3, KC.B,  
        KC.N0, KC.DOT, KC.ENT, KC.C  
    ]
]


encoder_handler.map = [
    ((KC.VOLD, KC.VOLU),) 
]

if __name__ == '__main__':
    keyboard.go()
