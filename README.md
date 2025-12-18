# Classic_Battleship
Input Format:

The game uses simple text input from the user.
During ship placement, the player enters coordinates (for example A5) and chooses the ship orientation (H for horizontal or V for vertical).
During gameplay, the player enters a single coordinate to attack.

All input is case-insensitive, so a5 and A5 work the same way.

Ship Placement Validation:

Ship placement is validated step by step:
	•	The coordinates must be inside the game board
	•	Ships cannot go outside the grid
	•	Ships cannot overlap with other ships
	•	Ships cannot be placed too close to each other (no touching, even diagonally)

If the placement is invalid, the user gets a clear message and is asked to try again.

Game State Update and Display:

The game board is updated after every action:
	•	When a player hits a ship, the cell is marked as a hit
	•	When a player misses, the cell is marked as a miss
	•	Destroyed ships are fully revealed on the board

The board is printed to the console after each move, so the player always sees the current game state.

Design Decisions and Trade-offs:
	•	The game is console-based to keep the logic simple and clear
	•	The board is stored as a 2D list for easy access and updates
	•	Input validation is separated from game logic to make the code easier to read and maintain
	•	Animations and graphics were not added to keep the focus on gameplay mechanics and correctness
