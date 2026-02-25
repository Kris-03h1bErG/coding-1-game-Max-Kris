# Write your game here
import curses
import time
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
    'japan': "U+1F5FE",
    'hotel': "U+1F3E8", 
    "bball": "U+1F3C0",
    "caution_sign": "U+1F6A7",
    "pencil": "U+270F",
    "palette": "U+1F3A8",
    "top_hat": "U+1F3A9"
    
    
}

def draw_board():
    for i in range(15):
        print("H E L L O W O R L D H E L L O")
    print("Random stats")
    print("Random stats")
    print("Random stats")
# time.sleep(2)
draw_board()