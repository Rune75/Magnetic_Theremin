input.onButtonPressed(Button.B, function () {
    input.calibrateCompass()
})
let scaling = input.magneticForce(Dimension.Strength)
basic.forever(function () {
    if (input.buttonIsPressed(Button.A)) {
        music.ringTone(input.magneticForce(Dimension.Strength) - scaling + 131)
    } else {
        music.stopAllSounds()
    }
})
