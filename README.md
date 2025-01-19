# Tetronomical

**Tetronomical** is a terminal-based Tetris game implemented in Python using the `curses` library. It features a classic Tetris gameplay experience, with colorful shapes, high score tracking, and game-over functionality. The game is rendered directly in the terminal, with a neat border around the game field for a polished look.

## Features

- **Classic Tetris Gameplay**: The game includes the familiar Tetris shapes (I, O, T, S, Z, L, J) that the player must rotate and fit into the board.
- **Colorful Shapes**: Different shapes are assigned distinct colors, making the game visually appealing and easier to play.
- **High Score Tracking**: The game tracks high scores and displays the top scores in a high-score leaderboard.
- **Game Over**: Once the player cannot place the next shape on the board, the game ends, and the score is saved.
- **Controls**:
  - Left Arrow: Move the shape left
  - Right Arrow: Move the shape right
  - Down Arrow: Move the shape down
  - Spacebar: Rotate the shape
  - Q: Quit the game

## Installation

### Prerequisites

You need Python 3 installed on your machine.

The 'curses' dependency is automatically downloaded on first install on windows machines, unless you don't have python installed.

### Clone the Repository

Clone the Tetronomical repository to your local machine:

```bash
git clone https://github.com/literal-gargoyle/tetronomical.git
cd tetronomical
```

## Running the Game

Run the following command to start playing the game:

```bash
python tetronomical.py
```

## Controls

- **Arrow Keys**: Move shapes left, right, and down.
- **Spacebar**: Rotate shapes.
- **Q**: Quit the game.

## High Scores

The game will save the top 5 high scores in a text file called `highscores.txt`. The leaderboard is displayed on the right side of the screen.

*This is a local leaderboard; it is not global*

## Customization

- **Game Board Dimensions**: The game board size can be customized by modifying the `SCREEN_WIDTH` and `SCREEN_HEIGHT` constants in the `tetronomical.py` file.
- **Colors**: The color scheme for the shapes is adjustable by modifying the `COLORS` list in the code.

## License

This project is licensed under the GNU V3 License, so feel free to download and modify with credit! :D - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **curses**: For handling the terminal interface and providing a way to draw on the terminal screen.
- **Tetris**: For providing the inspiration for this project!

## Owner

- **literal-gargoyle**: 100% of the code
