import msvcrt

# record keys
keys = []

try:
    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch()
            keys.append(key)
            if ord(key) == 27:  # press Esc to quit the loop
                break
finally:
    # print recorded keys
    print(keys)
