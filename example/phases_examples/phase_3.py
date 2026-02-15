# The goals for this phase include:
# - Implement player movement (I suggest W/A/S/D or arrow keys).
# - Prevent the player from moving off the board or into obstacles.
# - Track total moves (for high-score).
# - Display the updated board after each move.

# To make this work, you may have to type this into the terminal --> pip install curses
import curses

game_data = {
    # Icons
    # To find more icons go to https://emojipedia.org/
    "turtle": "\U0001F422",
    "eagle": "\U0001F985",
    "obstacle": "\U0001FAA8 ",
    "leaf": "\U0001F343",
    "empty": "  ",

    # Board dimensions
    'width': 5,
    'height': 5,

    # Icon positions
    'positions': {
        'player': (0, 0),
        'eagle': (4, 4),
        'obstacle': [(1, 2), (3, 1)],
        'leaf': [(2, 1)],
    }

    'score': 0
}

def draw_board(stdscr):
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_WHITE, -1)

    width = game_data['width']
    height = game_data['height']
    positions = game_data['positions']

    stdscr.clear()
    for y in range(height):
        row = ""
        for x in range(width):
            if (x, y) == positions['player']:
                row += game_data['turtle']
            elif (x, y) == positions['eagle']:
                row += game_data['eagle']
            elif (x, y) in positions['obstacle']:
                row += game_data['obstacle']
            elif (x, y) in positions['leaf']:
                row += game_data['leaf']
            else:
                row += game_data['empty']
        stdscr.addstr(y, 0, row, curses.color_pair(1))

    stdscr.refresh()
    stdscr.getkey()

curses.wrapper(draw_board)
