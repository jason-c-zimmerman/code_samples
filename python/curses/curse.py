import curses
from curses import wrapper
import time
import random

# stdscr = curses.initscr()
# curses.noecho()
# curses.cbreak()
# stdscr.keypad(True)

def main(stdscr):
	stdscr.nodelay(True)
	stdscr.clear()
	stdscr.border()
	curses.curs_set(0)
	curses.start_color()
	curses.use_default_colors()

	scrHeight, scrWidth = stdscr.getmaxyx()
	x = scrWidth / 2
	y = scrHeight / 2

	while True:
		#collisionCheck();
		
		c = stdscr.getch()
		curses.flushinp()
		stdscr.clear()
		
		stdscr.addstr(y,x, chr(178))

		if c == curses.KEY_DOWN:
			y += 1
		elif c == curses.KEY_UP:
			y -= 1
		elif c == curses.KEY_LEFT:
			x -= 1
		elif c == curses.KEY_RIGHT:
			x += 1
		# stdscr.addstr('#' * count)
		# count += direction
		# if count == width:
		# 	direction = -1
		# elif count == 0:
		# 	direction = 1

		# time.sleep(0.1)
		
	# print("running some program")
	# while (1): True

wrapper(main)



# begin_x = 20; begin_y = 7
# height = 5; width = 40
# win = curses.newwin(height, width, begin_y, begin_x)
# tb = curses.textpad.Textbox(win)
# text = tb.edit()

# stdscr.addstr(0,0, "Current Mode NCurses Typing Mode", curses.A_REVERSE)
# # stdscr.refresh()


# curses.nocbreak()
# stdscr.keypad(0)
# curses.echo()

# curses.endwin()