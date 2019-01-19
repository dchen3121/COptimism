# COptimism
A basic chess engine with graphic user interface built in Python. 

## Run
Run pygame_render.py to run COptimism; the depth that the AI will be running at can be adjusted inside the same file.

## Tools Used
Python 3.6, PyGame
The chess board is represented by a Board object while the pieces are represented by individual Piece objects.
The user interface is built with PyGame.

## Algorithms
The engine runs based on the **minimax algorithm**.
Inside the project there are two files named minimax.py and eval_board_state.py.
#### eval_board_state.py
- A function that returns a single number when given a Board object; the number returned is the AI's evaluation of the board inputted. The return value will be more positive if it favours white, while it will be more negative if it favours black.
- Sends the returned value to minimax.py where the board uses the evaluation to base its next move.
- Has 8 functionalities:
  1. Checks material value of each side on the board
  2. Checks piece activity for each side on the board (based on central control for the time being, will add more to this later)
  3. Checks if any pawns are close to promotion for each side
  4. Checks the king safety of both sides based on remaining material on the board and the length of the game
  5. Checks for double bishop advantage, assign extra bonus when position is open
  6. Checks for closed positions, assign extra bonus for knights under certain circumstances
  7. Checks for threats on opposing king and assigns a bonus accordingly, based on square control around the king
  8. Checks for checkmates (the most important one!)
#### minimax.py
- Includes functions that allow the AI to look through the list of possible boards that may occur as a result of the move. Can change depth accordingly, calculates the direct consequence of the next move when depth = 0, and calculates further ahead when depth is increased.
- Currently unable to perform past a certain depth due to exponentially increasing evaluation times.
- The AI runs the minimax algorithm: First, it takes in the current position and generates a list of possible boards that may result from its current move, then evaluates them all using eval_board_state(). If depth has not reached zero, for each of the positions generated, it will continue to attempt to evaluate the boards that may result from that board until depth 0 is reached. Returns a single best move based on its evaluations.

# Project
Made at: Starterhacks 2019 @ University of Waterloo
Team members: Abhishek Patel, Brianna Ai, Daniel Chen, Jessica Cao, Oliver Zhang 
