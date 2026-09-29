let hand = 0
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    
    hand = randint(0, 3)
    if (hand == 1) {
        basic.showLeds(`
            # # # # .
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
        music.playSoundEffect(music.createSoundEffect(WaveShape.Sine, 500, 500, 255, 0, 50, SoundExpressionEffect.Vibrato, InterpolationCurve.Linear), SoundExpressionPlayMode.UntilDone)
    } else if (hand == 2) {
        basic.showLeds(`
            . . . . .
            . # # # .
            # # # # .
            # # # # .
            # # # . .
            `)
        music.playSoundEffect(music.createSoundEffect(WaveShape.Square, 200, 1, 255, 0, 100, SoundExpressionEffect.None, InterpolationCurve.Curve), SoundExpressionPlayMode.UntilDone)
    } else {
        basic.showIcon(IconNames.Scissors)
        music.playSoundEffect(music.createSoundEffect(WaveShape.Sine, 500, 500, 255, 0, 50, SoundExpressionEffect.Vibrato, InterpolationCurve.Linear), SoundExpressionPlayMode.UntilDone)
    }
    
})
