import keyboard

# record keylogger events
keys = []

def on_key_event(event):
    keys.append(event.name)

# listen moniter the key events
keyboard.on_press(on_key_event)

try:
    while True:
        pass
except KeyboardInterrupt:
    # press Ctrl+C to quit the loop
    pass
finally:
    # stop the listener
    keyboard.unhook_all()

# print recorded keys
print(keys)
