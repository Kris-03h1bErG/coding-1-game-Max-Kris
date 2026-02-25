# Write your game here
import curses
import time
import random 

game_data = {
    # Store board dimensions, player/enemy positions, score, energy, collectibles, and icons
    'width': 15,
    'height': 15,
    'player': {"x": 7, "y": 15, "score": 0,}

    #ASCII icons

        # Blocks
    'pipe': "U+1F7E9",
    "sky": "U+1F7E6",
    "empty": "  ",

        # Random Players
    "icons": {'japan': "U+1F5FE", 'hotel': "U+1F3E8", "bball": "U+1F3C0", "caution_sign": "U+1F6A7", "pencil": "U+270F", "palette": "U+1F3A8", "top_hat": "U+1F3A9"}
    
}

def random_player(icon_list)


def draw_board(stdscr):
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_WHITE, -1)

    stdscr.clear()
    for y in range(game_data['height']):
        row = ""
        for x in range(game_data['width']):
            # Random player
            if x == game_data['player']['x'] and y == game_data['player']['y']:
                row += game_data['turtle']
            # Eagle
            elif x == game_data['eagle_pos']['x'] and y == game_data['eagle_pos']['y']:
                row += game_data['eagle_icon']
            else:
                row += game_data['sky']
        stdscr.addstr(y, 0, row, curses.color_pair(1))

    stdscr.refresh()
    stdscr.getkey()  # pause so player can see board

curses.wrapper(draw_board)