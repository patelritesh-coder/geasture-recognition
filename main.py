def on_gesture_right():
    basic.show_string("Anand Niketan")
grove.on_gesture(GroveGesture.RIGHT, on_gesture_right)

def on_gesture_clockwise():
    basic.show_icon(IconNames.HAPPY)
grove.on_gesture(GroveGesture.CLOCKWISE, on_gesture_clockwise)

def on_gesture_left():
    basic.show_string("Satellite")
grove.on_gesture(GroveGesture.LEFT, on_gesture_left)

def on_forever():
    pass
basic.forever(on_forever)
