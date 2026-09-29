hand = 0

def on_gesture_shake():
    global hand
    hand = randint(0, 3)
    if hand == 1:
        basic.show_leds("""
            # # # # .
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        music.play_sound_effect(music.create_sound_effect(WaveShape.SINE,
                500,
                500,
                255,
                0,
                50,
                SoundExpressionEffect.VIBRATO,
                InterpolationCurve.LINEAR),
            SoundExpressionPlayMode.UNTIL_DONE)
    elif hand == 2:
        basic.show_leds("""
            . . . . .
            . # # # .
            # # # # .
            # # # # .
            # # # . .
            """)
        music.play_sound_effect(music.create_sound_effect(WaveShape.SQUARE,
                200,
                1,
                255,
                0,
                100,
                SoundExpressionEffect.NONE,
                InterpolationCurve.CURVE),
            SoundExpressionPlayMode.UNTIL_DONE)
    else:
        basic.show_icon(IconNames.SCISSORS)
        music.play_sound_effect(music.create_sound_effect(WaveShape.SINE,
                500,
                500,
                255,
                0,
                50,
                SoundExpressionEffect.VIBRATO,
                InterpolationCurve.LINEAR),
            SoundExpressionPlayMode.UNTIL_DONE)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
