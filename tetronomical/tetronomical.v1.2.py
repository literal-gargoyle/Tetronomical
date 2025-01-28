import random
import os
import sys
import subprocess
import time




#                ▄████▄   ██▀███  ▓█████ ▓█████▄  ██▓▄▄▄█████▓  ██████    
#                ▒██▀ ▀█  ▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌▓██▒▓  ██▒ ▓▒▒██    ▒    
#                ▒▓█    ▄ ▓██ ░▄█ ▒▒███   ░██   █▌▒██▒▒ ▓██░ ▒░░ ▓██▄      
#                ▒▓▓▄ ▄██▒▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌░██░░ ▓██▓ ░   ▒   ██▒  
#                ▒ ▓███▀ ░░██▓ ▒██▒░▒████▒░▒████▓ ░██░  ▒██▒ ░ ▒██████▒▒   
#                ░ ░▒ ▒  ░░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒ ░▓    ▒ ░░   ▒ ▒▓▒ ▒ ░   
#                ░  ▒     ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒  ▒ ░    ░    ░ ░▒  ░ ░   
#                ░          ░░   ░    ░    ░ ░  ░  ▒ ░  ░      ░  ░  ░     
#                ░ ░         ░        ░  ░   ░     ░                 ░     
#                ░                         ░                               

#                   ██▓   ▓█████▄▄▄     ▓█████▄    ▓█████▄▓███████▒   █▓
#                  ▓██▒   ▓█   ▒████▄   ▒██▀ ██▌   ▒██▀ ██▓█   ▓██░   █▒
#                  ▒██░   ▒███ ▒██  ▀█▄ ░██   █▌   ░██   █▒███  ▓██  █▒░
#                  ▒██░   ▒▓█  ░██▄▄▄▄██░▓█▄   ▌   ░▓█▄   ▒▓█  ▄ ▒██ █░░
#                  ░██████░▒████▓█   ▓██░▒████▓    ░▒████▓░▒████▒ ▒▀█░  
#                   ░ ▒░▓  ░░ ▒░ ▒▒   ▓▒█░▒▒▓  ▒     ▒▒▓  ▒░░ ▒░ ░ ░ ▐░  
#                   ░ ░ ▒  ░░ ░  ░▒   ▒▒ ░░ ▒  ▒     ░ ▒  ▒ ░ ░  ░ ░ ░░  
#                     ░ ░     ░   ░   ▒   ░ ░  ░     ░ ░  ░   ░      ░░  
#                       ░  ░  ░  ░    ░  ░  ░          ░      ░  ░    ░  
#                                          ░          ░               ░   
#                             
#
# ██▓    ██▄▄▄█████▓█████ ██▀███  ▄▄▄      ██▓     ▄████ ▄▄▄      ██▀███   ▄████ ▒█████▓██   ██▓██▓   ▓█████ 
#▓██▒   ▓██▓  ██▒ ▓▓█   ▀▓██ ▒ ██▒████▄   ▓██▒    ██▒ ▀█▒████▄   ▓██ ▒ ██▒██▒ ▀█▒██▒  ██▒██  ██▓██▒   ▓█   ▀ 
#▒██░   ▒██▒ ▓██░ ▒▒███  ▓██ ░▄█ ▒██  ▀█▄ ▒██░   ▒██░▄▄▄▒██  ▀█▄ ▓██ ░▄█ ▒██░▄▄▄▒██░  ██▒▒██ ██▒██░   ▒███   
#▒██░   ░██░ ▓██▓ ░▒▓█  ▄▒██▀▀█▄ ░██▄▄▄▄██▒██░   ░▓█  ██░██▄▄▄▄██▒██▀▀█▄ ░▓█  ██▒██   ██░░ ▐██▓▒██░   ▒▓█  ▄ 
#░██████░██░ ▒██▒ ░░▒████░██▓ ▒██▒▓█   ▓██░██████░▒▓███▀▒▓█   ▓██░██▓ ▒██░▒▓███▀░ ████▓▒░░ ██▒▓░██████░▒████▒
#░ ▒░▓  ░▓   ▒ ░░  ░░ ▒░ ░ ▒▓ ░▒▓░▒▒   ▓▒█░ ▒░▓  ░░▒   ▒ ▒▒   ▓▒█░ ▒▓ ░▒▓░░▒   ▒░ ▒░▒░▒░  ██▒▒▒░ ▒░▓  ░░ ▒░ ░
#░ ░ ▒  ░▒ ░   ░    ░ ░  ░ ░▒ ░ ▒░ ▒   ▒▒ ░ ░ ▒  ░ ░   ░  ▒   ▒▒ ░ ░▒ ░ ▒░ ░   ░  ░ ▒ ▒░▓██ ░▒░░ ░ ▒  ░░ ░  ░
#  ░ ░   ▒ ░ ░        ░    ░░   ░  ░   ▒    ░ ░  ░ ░   ░  ░   ▒    ░░   ░░ ░   ░░ ░ ░ ▒ ▒ ▒ ░░   ░ ░     ░   
#    ░  ░░            ░  ░  ░          ░  ░   ░  ░     ░      ░  ░  ░          ░    ░ ░ ░ ░        ░  ░  ░  ░
#                                  https:github.com/literal-gargoyle/                                      ░ ░                  
#


# Ensure windows-curses is installed on Windows
if os.name == "nt":
    try:
        import curses
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "windows-curses"])
        import curses

if os.name == "darwin":
    try:
        import curses
    except ImportError:
        print("Please use python 3.10 or lower to run this program,\n the curses module is not available on python 3.11 or higher")

if os.name =="posix":
    try:
        import curses
    except ImportError:
        print("Please use python 3.10 or lower to run this program,\n the curses module is not available on python 3.11 or higher")

# Constants
SCREEN_WIDTH = 10
SCREEN_HEIGHT = 20
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]],  # Z
    [[1, 0, 0], [1, 1, 1]],  # L
    [[0, 0, 1], [1, 1, 1]],  # J
]
COLORS = [
    curses.COLOR_CYAN,
    curses.COLOR_YELLOW,
    curses.COLOR_MAGENTA,
    curses.COLOR_GREEN,
    curses.COLOR_RED,
    curses.COLOR_BLUE,
    curses.COLOR_WHITE,
]

HIGH_SCORES_FILE = "newhighscores.txt"

# Initialize the game board
def create_board():
    return [[0 for _ in range(SCREEN_WIDTH)] for _ in range(SCREEN_HEIGHT)]

# Rotate a shape clockwise
def rotate_shape(shape):
    return [list(row) for row in zip(*shape[::-1])]

# Check if a shape can move to a specific position
def is_valid_position(board, shape, offset):
    offset_x, offset_y = offset
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                new_x = offset_x + x
                new_y = offset_y + y
                if (
                    new_x < 0
                    or new_x >= SCREEN_WIDTH
                    or new_y >= SCREEN_HEIGHT
                    or (new_y >= 0 and board[new_y][new_x])
                ):
                    return False
    return True

# Merge the shape into the board
def merge_shape(board, shape, offset, color):
    offset_x, offset_y = offset
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                board[offset_y + y][offset_x + x] = color

# Clear completed lines and return the number of cleared lines
def clear_lines(board):
    lines_cleared = 0
    for y in range(SCREEN_HEIGHT):
        if all(board[y]):
            del board[y]
            board.insert(0, [0 for _ in range(SCREEN_WIDTH)])
            lines_cleared += 1
    return lines_cleared

# Update high score functions to include initials
# Saves to a .txt file (highscores.txt)
def load_high_scores():
    if not os.path.exists(HIGH_SCORES_FILE):
        return []
    with open(HIGH_SCORES_FILE, "r") as f:
        scores = []
        for line in f:
            initials, score = line.strip().split(":")
            scores.append((initials, int(score)))
        return scores

def save_high_scores(high_scores):
    with open(HIGH_SCORES_FILE, "w") as f:
        for initials, score in high_scores:
            f.write(f"{initials}:{score}\n")

# Instantly place the current shape
def instant_place(board, shape, position):
    x, y = position
    while is_valid_position(board, shape, (x, y)):
        y += 1
    return (x, y - 1)

# Game over logic with added initials input
def game_over(stdscr, score):
    global high_scores
    stdscr.addstr(SCREEN_HEIGHT // 2, SCREEN_WIDTH, "GAME OVER")
    stdscr.addstr(SCREEN_HEIGHT // 2 + 1, SCREEN_WIDTH, f"Final Score: {score}")
    stdscr.addstr(SCREEN_HEIGHT // 2 + 3, SCREEN_WIDTH, "Enter your initials (3 letters):")
    stdscr.refresh()

    initials = ""
    while len(initials) < 3:
        key = stdscr.getch()
        if key in range(65, 91) or key in range(97, 123):  # A-Z or a-z
            initials += chr(key).upper()
            stdscr.addstr(SCREEN_HEIGHT // 2 + 4, SCREEN_WIDTH, initials)
            stdscr.refresh()

    # Save the score with initials
    high_scores.append((initials, score))
    high_scores = sorted(high_scores, key=lambda x: x[1], reverse=True)[:5]
    save_high_scores(high_scores)

    stdscr.addstr(SCREEN_HEIGHT // 2 + 6, SCREEN_WIDTH, "Press any key to return to the menu...")
    stdscr.refresh()
    stdscr.getch()
    
# v1.1 updated teris game logic, added new gameOver screen /\ plus initals
def tetris(stdscr):
    global score
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(300)

    curses.start_color()
    for i, color in enumerate(COLORS, start=1):
        curses.init_pair(i, color, curses.COLOR_BLACK)

    board = create_board()
    current_shape = random.choice(SHAPES)
    current_color = random.randint(1, len(COLORS))
    next_shape = random.choice(SHAPES)
    next_color = random.randint(1, len(COLORS))
    current_position = [SCREEN_WIDTH // 2 - len(current_shape[0]) // 2, 0]

    score = 0
    high_scores = load_high_scores()

    while True:
        # Draw board
        stdscr.clear()
        for y, row in enumerate(board):
            for x, cell in enumerate(row):
                if cell:
                    stdscr.addstr(y, x * 2, "[]", curses.color_pair(cell))

        # Draw current shape
        for y, row in enumerate(current_shape):
            for x, cell in enumerate(row):
                if cell:
                    stdscr.addstr(current_position[1] + y, (current_position[0] + x) * 2, "[]", curses.color_pair(current_color))

        # Display next shape
        stdscr.addstr(0, SCREEN_WIDTH * 2 + 2, "Next:")
        for y, row in enumerate(next_shape):
            for x, cell in enumerate(row):
                if cell:
                    stdscr.addstr(1 + y, (SCREEN_WIDTH * 2 + 4 + x) * 2, "[]", curses.color_pair(next_color))

        # Display score and high scores
        stdscr.addstr(8, SCREEN_WIDTH * 2 + 2, f"Score: {score}")
        stdscr.addstr(10, SCREEN_WIDTH * 2 + 2, "High Scores:")
        for i, (initials, hs) in enumerate(high_scores):
            stdscr.addstr(11 + i, SCREEN_WIDTH * 2 + 2, f"{i + 1}. {initials}: {hs}")

        # Display controls
        stdscr.addstr(18, SCREEN_WIDTH * 2 + 2, "Controls:")
        stdscr.addstr(19, SCREEN_WIDTH * 2 + 2, "Left: Arrow Left")
        stdscr.addstr(20, SCREEN_WIDTH * 2 + 2, "Right: Arrow Right")
        stdscr.addstr(21, SCREEN_WIDTH * 2 + 2, "Down: Arrow Down")
        stdscr.addstr(22, SCREEN_WIDTH * 2 + 2, "Rotate: Space")
        stdscr.addstr(23, SCREEN_WIDTH * 2 + 2, "Instant Place: Arrow Up")
        stdscr.addstr(24, SCREEN_WIDTH * 2 + 2, "Quit: Q")

        stdscr.refresh()

        # Input handling
        key = stdscr.getch()
        if key == curses.KEY_LEFT:
            new_position = [current_position[0] - 1, current_position[1]]
            if is_valid_position(board, current_shape, new_position):
                current_position = new_position
        elif key == curses.KEY_RIGHT:
            new_position = [current_position[0] + 1, current_position[1]]
            if is_valid_position(board, current_shape, new_position):
                current_position = new_position
        elif key == curses.KEY_DOWN:
            new_position = [current_position[0], current_position[1] + 1]
            if is_valid_position(board, current_shape, new_position):
                current_position = new_position
        elif key == curses.KEY_UP:
            current_position = instant_place(board, current_shape, current_position)
        elif key == ord("q"):
            break
        elif key == ord(" "):
            rotated_shape = rotate_shape(current_shape)
            if is_valid_position(board, rotated_shape, current_position):
                current_shape = rotated_shape

        # Move shape down
        new_position = [current_position[0], current_position[1] + 1]
        if is_valid_position(board, current_shape, new_position):
            current_position = new_position
        else:
            merge_shape(board, current_shape, current_position, current_color)
            score += clear_lines(board) * 100
            current_shape = next_shape
            current_color = next_color
            next_shape = random.choice(SHAPES)
            next_color = random.randint(1, len(COLORS))
            current_position = [SCREEN_WIDTH // 2 - len(current_shape[0]) // 2, 0]

            if not is_valid_position(board, current_shape, current_position):
                game_over(stdscr, score)
                break
            
# Menu screen logic
def show_menu(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(0)
    stdscr.clear()
    stdscr.refresh()

    logo = """
▄▄▄█████▓▓█████▄▄▄█████▓ ██▀███   ▒█████   ███▄    █  ▒█████   ███▄ ▄███▓ ██▓ ▄████▄   ▄▄▄       ██▓    
▓  ██▒ ▓▒▓█   ▀▓  ██▒ ▓▒▓██ ▒ ██▒▒██▒  ██▒ ██ ▀█   █ ▒██▒  ██▒▓██▒▀█▀ ██▒▓██▒▒██▀ ▀█  ▒████▄    ▓██▒    
▒ ▓██░ ▒░▒███  ▒ ▓██░ ▒░▓██ ░▄█ ▒▒██░  ██▒▓██  ▀█ ██▒▒██░  ██▒▓██    ▓██░▒██▒▒▓█    ▄ ▒██  ▀█▄  ▒██░    
░ ▓██▓ ░ ▒▓█  ▄░ ▓██▓ ░ ▒██▀▀█▄  ▒██   ██░▓██▒  ▐▌██▒▒██   ██░▒██    ▒██ ░██░▒▓▓▄ ▄██▒░██▄▄▄▄██ ▒██░    
  ▒██▒ ░ ░▒████▒ ▒██▒ ░ ░██▓ ▒██▒░ ████▓▒░▒██░   ▓██░░ ████▓▒░▒██▒   ░██▒░██░▒ ▓███▀ ░ ▓█   ▓██▒░██████▒
  ▒ ░░   ░░ ▒░ ░ ▒ ░░   ░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░ ▒░▒░▒░ ░ ▒░   ░  ░░▓  ░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░▓  ░
    ░     ░ ░  ░   ░      ░▒ ░ ▒░  ░ ▒ ▒░ ░ ░░   ░ ▒░  ░ ▒ ▒░ ░  ░      ░ ▒ ░  ░  ▒     ▒   ▒▒ ░░ ░ ▒  ░
  ░         ░    ░        ░░   ░ ░ ░ ░ ▒     ░   ░ ░ ░ ░ ░ ▒  ░      ░    ▒ ░░          ░   ▒     ░ ░   
            ░  ░           ░         ░ ░           ░     ░ ░         ░    ░  ░ ░            ░  ░    ░  ░
                                                                             ░                          
    """

    stdscr.addstr(0, 0, logo)
    height, width = stdscr.getmaxyx()
    # Adjust the position of the text based on terminal size
    stdscr.addstr(18, 0, "Press 'S' to Start")
    stdscr.addstr(19, 0, "Press 'I' for Instructions")
    stdscr.addstr(20, 0, "Press 'Q' to Quit")
    stdscr.refresh()

    while True:
        key = stdscr.getch()
        if key == ord('s'):
            tetris(stdscr)
            break
        elif key == ord('i'):
            show_instructions(stdscr)
            break
        elif key == ord('q'):
            break

# Instructions screen
def show_instructions(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Tetris Instructions:")
    stdscr.addstr(2, 0, "Use the arrow keys to move the blocks.")
    stdscr.addstr(3, 0, "Press 'Space' to rotate the blocks.")
    stdscr.addstr(4, 0, "Clear lines to score points.")
    stdscr.addstr(5, 0, "Press 'Q' to quit the game.")
    stdscr.addstr(7, 0, "Press any key to go back to the menu...")
    stdscr.refresh()
    stdscr.getch()
    show_menu(stdscr)

if __name__ == "__main__":
    curses.wrapper(show_menu)