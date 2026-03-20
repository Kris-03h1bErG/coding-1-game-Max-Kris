# Copy this python3 game.py
# Ripoff flappybird
import curses
import time
import random 

game_data = {
    # Store board dimensions, player/enemy positions, score, energy, collectibles, and icons
    'width': 7,
    'height': 10,
        'pipes_order' : [   
                    [   [random.randint(0,4)] , [random.randint(0,4)] , [random.randint(0,4)] , [random.randint(0,4)]],
                    [   [random.randint(0,4)] , [random.randint(0,4)] , [random.randint(0,4)] , [random.randint(0,4)]],
                    [   [random.randint(0,4)] , [random.randint(0,4)] , [random.randint(0,4)] , [random.randint(0,4)]], 
                    [   [random.randint(0,4)] , [random.randint(0,4)] , [random.randint(0,4)] , [random.randint(0,4)]],
                    [   [random.randint(0,4)] , [random.randint(0,4)] , [random.randint(0,4)] , [random.randint(0,4)]]
                    ], 
    'order_list' : [ random.randint(0,4) , random.randint(0,4) , random.randint(0,4) , random.randint(0,4) , random.randint(0,4)],
    'current_order' : random.randint(0,4),
    'current_pipe': random.randint(0,4),
    'next_pipe' : [0, 0], 
    'player': {"x": 2, "y": 5, "score": 0, "seed" : random.randint(1,100)} , 
    'pipes': [ 
    [
        {"x": 7, "y": 0}, # normal 
        {"x": 7, "y": 1},
        {"x": 7, "y": 2},
        {"x": 7, "y": 3},
        {"x": 7, "y": 7},
        {"x": 7, "y": 8},
        {"x": 7, "y": 9},
        {"x": 7, "y": 10} 
    ],
    [
        {"x": 7, "y": 0}, # slightly lower
        {"x": 7, "y": 1},
        {"x": 7, "y": 2},
        {"x": 7, "y": 3},
        {"x": 7, "y": 4},
        {"x": 7, "y": 5},
        {"x": 7, "y": 9},
        {"x": 7, "y": 10} 
    ],

    [
        {"x": 7, "y": 3}, # need to be high 
        {"x": 7, "y": 4},
        {"x": 7, "y": 5},
        {"x": 7, "y": 6},
        {"x": 7, "y": 7},
        {"x": 7, "y": 8},
        {"x": 7, "y": 9},
        {"x": 7, "y": 10} 
    ],

    [
        {"x": 7, "y": 0}, # low
        {"x": 7, "y": 1},
        {"x": 7, "y": 2},
        {"x": 7, "y": 3},
        {"x": 7, "y": 4},
        {"x": 7, "y": 5},
        {"x": 7, "y": 6},
        {"x": 7, "y": 7} 
    ],

    [
        {"x": 7, "y": 0},
        {"x": 7, "y": 1},
        {"x": 7, "y": 2},
        {"x": 7, "y": 3},
        {"x": 7, "y": 7},
        {"x": 7, "y": 8},
        {"x": 7, "y": 9},
        {"x": 7, "y": 10}
    ],
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

    x = game_data['player']['x']
    y = game_data['player']['y']
    new_x, new_y = x, y
    key = key.lower()

    if key == "w": #checks player input and  changes according vlaues 
        #stdscr.addstr(y, 15, 0, new_y)
        new_y -= 1 
    else: #every other key moves down to avoid a cheat to stay floating
        new_y += 1

    if new_y == -1: 
        new_y = 0
    elif new_y == 11:
        new_y = 10
        
    game_data['player']['x'] = new_x
    game_data['player']['y'] = new_y

    # if any(o['x'] == new_x and o['y'] == new_y for o in game_data['pipes']) or game_data["player"]["y"] == 11:
    #     exit

def draw_board(stdscr):
    curses.start_color() # initialize requirements for color
    curses.use_default_colors() # Checks for terminals normal color scheme  
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_CYAN) # sets up basic color scheme
    stdscr.clear() # sets up termninal to look like game 
    for y in range(game_data['height'] + 1): #iterates through hight in dict (10) 
        row = ""
        for x in range(game_data['width'] + 1): #iterates through width in dict (7)
            # Random player
            if x == game_data['player']['x'] and y == game_data['player']['y']: #checks if XY equals players x and y 
                row += random_player(game_data["icons"], game_data["player"]["seed"]) #then  adds player icon to str
                # Space in code for readability
            # Pipes                                                         #need to get same pipe each time 
            elif any(p['x'] == x and p['y'] == y for p in game_data['pipes'][game_data['next_pipe'][0]]):
                row += game_data['pipe']
            # Blue sky stuff (I don't think this is actually used)
            else: # need to add more elif's to display more 
                row += game_data['sky'] #adds skys dict value to the string
                row += " " #just helps readability  
        stdscr.addstr(y, 0, row, curses.color_pair(1)) # adds row string with the normal color pair to screen

    stdscr.refresh() 
def pipe_movement():
    curent_pipes = game_data["pipes"][game_data["next_pipe"][0]]
    if curent_pipes[0]["x"] > 0:
        for p in curent_pipes:
            p['x'] -= 1
    else:
        for p in curent_pipes:
            p['x'] = 7
        pick_next_pipe( game_data['order_list'] , game_data['pipes_order'] , game_data['current_order'], game_data['current_pipe'])    
        #pick_next_pipe(game_data['pipe_seed'] , game_data['order_list'] , game_data['pipes_order'] , game_data['current_order'], ['current_pipe'])
        
    # random.seed(random.randint(1,1000))
    # game_data['pipe_seed'] = random.randint(0,4)

# def pick_next_pipe(starting_position_in_pol , pipe_order_list , pipes_order_in_list , position_in_pol, position_in_poll):
#     pipe_order_list[starting_position_in_pol]

def pick_next_pipe( pipe_order_list , pipes_order_in_list , position_in_pol, position_in_poll):
    position_in_poll += 1

    if position_in_poll > 3:
        position_in_poll = 0
        position_in_pol = (position_in_pol + 1) % 5

    actual_pipe_set = pipes_order_in_list[position_in_pol]
    new_pipe_index = actual_pipe_set[position_in_poll][0]
    
    game_data["current_order"] = position_in_pol
    game_data["current_pipe"] = position_in_poll
    game_data["next_pipe"] = [new_pipe_index, position_in_poll]

    

def run_game(stdscr):
    curses.curs_set(0) # sets cursor to invisible 
    stdscr.nodelay(True) # allows inputs now 

    #draw_board(stdscr) # prints board 
    while True:
        try: 
            key = stdscr.getkey()
        except: #basic data filterin
            key = None
        if key:
            if key.lower() == "q": # if input is q then break
                break

            move_player(key)
            draw_board(stdscr)
            pipe_movement()
            if any(o['x'] == game_data["player"]["x"] and o['y'] == game_data["player"]["y"] for o in game_data['pipes'][game_data['next_pipe'][0]]) or game_data["player"]["y"] == 10:
                break
            time.sleep(.2)
            
curses.wrapper(run_game)
#pipe_movement()