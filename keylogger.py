import curses

# initialize curses
stdscr = curses.initscr()
curses.noecho()
stdscr.keypad(True)

# record keylogger events
keys = []

try:
    while True:
        key = stdscr.getch()
        keys.append(key)
        if key == ord('q'):  # push 'q' to quit
            break
finally:
    # revert back to initialized settings
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()

# print recorded keys
print(keys)

