# Copy this python3 game.py
# Ripoff flappybird
import curses
import time
import random 

game_data = {
    # Store board dimensions, player/enemy positions, score, energy, collectibles, and icons
    'width': 7,
    'height': 10,
    'player': {"x": 0, "y": 10, "score": 0, "seed" : random.randint(1,100)} , 

    'pipes': [
        {"x": 7, "y": 0},
        {"x": 7, "y": 1},
        {"x": 7, "y": 2},
        {"x": 7, "y": 3},
        {"x": 7, "y": 7},
        {"x": 7, "y": 8},
        {"x": 7, "y": 9},
        {"x": 7, "y": 10}
    ],

    #ASCII icons
        # Blocks
    'pipe': "\U0001F7E9", #weird green 
    'sky' : " ", #"sky": "\U0001F7E6",  #weird blue 
    "empty":  "Lorsum Ipsum idk?", # this is empty for now 

        # Random Players just a large dict of emojis for player 
    "icons": {
            'japan': "\U0001F5FE",
            'hotel': "\U0001F3E8", 
            "bball": "\U0001F3C0", 
            "caution_sign": "\U0001F6A7", 
            #"pencil": "\u270F",  for some reason is slightly shorter than the rest?
            "palette": "\U0001F3A8", 
            "top_hat": "\U0001F3A9",
        }

}

def random_player(icon_list , number):
    random.seed(number)
    # debug stuff
    # print(type)(random.choice(icon_list.keys))
    # print(random.choice(icon_list.keys))
    return random.choice(list(icon_list.values()))

def move_player(key):
    if key == "w" and y > 0: #checks player input and  changes according vlaues 
        new_y -= 1
    else:
        return #change this to make the player fall a certain amount in a certain period of time


def draw_board(stdscr):
    curses.start_color() # inizilaze requiremnets for color
    curses.use_default_colors() # Checks for terminals normal color scheme  
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_CYAN) # sets up basic color scheme
    stdscr.clear() # sets up termninal to look like game 
    for y in range(game_data['height'] + 1): #itterates through hight in dict (10) 
        row = ""
        for x in range(game_data['width'] + 1): #itterates through width in dict (7)
            # Random player
            if x == game_data['player']['x'] and y == game_data['player']['y']: #checks if XY equals players x and y 
                row += random_player(game_data["icons"], game_data["player"]["seed"]) #then  adds player icon to str
                #row += " " #just helps readability 
            # Pipes
            elif any(p['x'] == x and p['y'] == y for p in game_data['pipes']):
                row += game_data['pipe']
            # Blue sky stuff
            else: # need to add more elif's to display more 
                row += game_data['sky'] #adds skys dict value to the string
                row += " " #just helps readability  
        stdscr.addstr(y, 0, row, curses.color_pair(1)) # adds row string with the normal color pair to screen

    stdscr.refresh() 
    stdscr.getkey()  # pause so player can see board

curses.wrapper(draw_board)