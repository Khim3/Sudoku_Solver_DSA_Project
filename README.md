# Sudoku Solver

This is a Sudoku Solver implemented as part of a Data Structures and Algorithms (DSA) project. The solver provides multiple algorithms to solve Sudoku puzzles, including Backtracking, AC-3 algorithms. Additionally, it includes a GUI for easy interaction and visualization.

## Features

- **Multiple Solving Algorithms**: Choose from different algorithms including Backtracking and AC-3 (Arc Consistency) to solve Sudoku puzzles.
- **Random Puzzle Generation**: Generate Sudoku puzzles with varying difficulties (Easy, Medium, Hard) for endless solving challenges.
- **Interactive GUI**: Visualize the solving process through an interactive GUI, making puzzle solving both efficient and enjoyable.
- **File I/O**: Load puzzles from files and save solutions, allowing for easy sharing and persistence of puzzle states.
- **Scrollable Solutions**: View solutions in a scrollable and resizable window for convenience.

## Requirements

- Python 3.x (3.6 or above)
- `tkinter` for GUI
- Additional Python libraries (listed in `requirements.txt`)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Khim3/Sudoku_Solver_DSA_Project.git
    ```

2. Install the required Python libraries:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Sudoku solver GUI:
    ```bash
    python sudoku.py
    ```

2. Use the GUI to:
    - Enter a custom Sudoku puzzle.
    - Load and solve selected predefined puzzles.
    - Generate a random puzzle.
    - Solve the puzzle using the selected algorithm.
    - Count the taken for each puzzle for each algorithm.
    - View the solution in a scrollable and resizable window.

## File Structure

- `sudoku.py`: The main script to run the GUI.
- `AC3.py`: Contains the implementation of the AC-3 algorithm.
- `Backtrack.py`: Contains the implementation of the Backtracking algorithm.
- `csp.py`: Defines the CSP (Constraint Satisfaction Problem) structure.
- `util.py`: Difines the encoded rows and columns of each puzzle.
- `input/`: Directory containing input Sudoku puzzles.
- `output/`: Directory where solutions are saved.

## Instructions

1. Open the GUI by running `sudoku.py`.
2. Select a predefined puzzle, create random puzzle or enter a custom puzzle.
3. Choose the solving algorithm (Backtracking, AC-3).
4. Click the "Solve" button to solve the puzzle.
5. View the solution in a new window by clicking the "Open Solution" button.


## Contributing

This is a personal project and is currently being developed and maintained solely by me. I really appreciate your interest, please give me constructive feedbacks for improving my project.

