import curses

# 初始化 curses
stdscr = curses.initscr()
curses.noecho()
stdscr.keypad(True)

# 记录按键事件
keys = []

try:
    while True:
        key = stdscr.getch()
        keys.append(key)
        if key == ord('q'):  # 按下 'q' 键退出
            break
finally:
    # 恢复终端设置
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()

# 打印记录的按键
print(keys)

