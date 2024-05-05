import curses

# Initialize curses
stdscr = curses.initscr()
curses.noecho()
stdscr.keypad(True)

# Record key incidents
keys = []

try:
    while True:
        key = stdscr.getch()
        keys.append(key)
        if key == ord('q'):  # Press 'q' to quit
            break
finally:
    # Revert to initialized settings
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()

# print recorded keys
print(keys)

