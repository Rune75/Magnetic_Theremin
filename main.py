def on_button_pressed_b():
    input.calibrate_compass()
input.on_button_pressed(Button.B, on_button_pressed_b)

scaling = input.magnetic_force(Dimension.STRENGTH)

def on_forever():
    if input.button_is_pressed(Button.A):
        music.ring_tone(input.magnetic_force(Dimension.STRENGTH) - scaling + 262)
    else:
        music.stop_all_sounds()
basic.forever(on_forever)
