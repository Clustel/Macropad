import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.rgb import RGB

keyboard = KMKKeyboard()

# 1. MATRIX SETUP
# Mapped exactly to your COL0-COL3 and ROW0-ROW3 nets
keyboard.col_pins = (board.D10, board.D9, board.D8, board.D7)
keyboard.row_pins = (board.D0, board.D1, board.D2, board.D3)
keyboard.diode_orientation = DiodeOrientation.COL2ROW 

# 2. ENCODER SETUP
# Mapped to EC11A (D5) and EC11B (D6). 
# Button pin is None because SW4 is wired directly into the Row 0 / Col 3 matrix spot.
encoder_handler = EncoderHandler()
encoder_handler.pins = ((board.D5, board.D6, None, False),) 
keyboard.modules.append(encoder_handler)

# 3. RGB SETUP
# Mapped to LEDC (D4) with 16 total pixels as shown in the schematic (D17-D32)
rgb = RGB(
    pixel_pin=board.D4, 
    num_pixels=16,       
    val_limit=150,       # Brightness limit to prevent pulling too much current from USB
    hue_default=160,     # Default color (Cyan-ish)
    sat_default=255,
    val_default=100,
)
keyboard.extensions.append(rgb)

# 4. KEYMAP (4x4 Grid)
# SW4 (Encoder Push) is located at the end of Row 0.
keyboard.keymap = [
    [
        KC.N7, KC.N8, KC.N9, KC.MUTE, # Row 0 (SW1, SW2, SW3, SW4/Encoder)
        KC.N4, KC.N5, KC.N6, KC.A,    # Row 1 (SW5, SW6, SW7, SW8)
        KC.N1, KC.N2, KC.N3, KC.B,    # Row 2 (SW9, SW10, SW11, SW12)
        KC.N0, KC.DOT, KC.ENT, KC.C   # Row 3 (SW13, SW14, SW15, SW16)
    ]
]

# 5. ENCODER MAP
# Defines what turning the knob does. Mapped per-layer.
encoder_handler.map = [
    ((KC.VOLD, KC.VOLU),) # Turn Left = Vol Down, Turn Right = Vol Up
]

if __name__ == '__main__':
    keyboard.go()
