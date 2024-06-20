# Name: Nguyen Nhat Khiem - ITDSIU21091
# Purpose: Implement a Sudoku Solver using Backtracking and AC-3 algorithms
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
from random import randint
from Backtrack import *
from AC3 import *
from csp import *
import time
import random
import threading
from tkinter import Toplevel, Text, Scrollbar, VERTICAL, RIGHT, Y


class SudokuSolver:
    _instance = None

    def __init__(self, root):
        self.root = root
        self.root.title('Sudoku Solver')
        self.root.geometry('1280x600')
        self.root.config(bg='gray')
        self.create_widgets()

    # add singleton pattern
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def get_instance(cls, root):
        if not cls._instance:
            cls._instance = cls(root)
        return cls._instance
    # validate the input of the user

    def create_widgets(self):
        def validate_input(P):
            if P.isdigit() and len(P) <= 1 or P == '':  # allow only digits and limit length to 1
                return True
            else:
                return False
        vcmd = (self.root.register(validate_input), '%P')
        # Sudoku grid
        self.grid_frame = Frame(self.root)
        self.grid_frame.place(x=50, y=100)

        self.cells = []
        for i in range(9):
            row = []
            for j in range(9):
                entry = Entry(self.grid_frame, width=5, font=(
                    'Fira Code', 20), justify='center', validate='key', validatecommand=vcmd)
                entry.grid(row=i, column=j)
                row.append(entry)
            self.cells.append(row)

        # add buttons for menu
        # Algorithm selection
        self.selected_algorithm = StringVar()
        self.algoLabel = Label(self.root, text='Algorithm: ', font=(
            'Fira Code', 15, 'italic'), bg='green', width=12, fg='black', relief=GROOVE, bd=5)
        self.algoLabel.place(x=1, y=5)

        self.algoMenu = ttk.Combobox(self.root, height=10, width=15, font=('Fira Code', 15, 'bold'), textvariable=self.selected_algorithm,
                                     values=['Backtracking', 'AC-3'])
        self.algoMenu.place(x=160, y=8)
        self.algoMenu.current(0)
        # Difficulty selection
        self.selected_difficulty = StringVar()
        self.difficultyLabel = Label(self.root, text='Difficulty: ', font=(
            'Fira Code', 15, 'italic',), justify='center', bg='green', width=12, fg='black', relief=GROOVE, bd=5)
        self.difficultyLabel.place(x=370, y=5)
        self.difficultyMenu = ttk.Combobox(self.root, height=10, width=12, font=('Fira Code', 15, 'bold'), justify='center', textvariable=self.selected_difficulty,
                                           values=['Problem1', 'Problem2', 'Problem3', 'Easy', 'Medium', 'Hard', 'Custom'])
        self.difficultyMenu.place(x=530, y=8)
        self.difficultyMenu.current(0)

        # Solve button
        self.solveButton = Button(self.root, text='Solve', font=(
            'Fira Code', 15, 'bold'), justify='center', bg='green', fg='black', relief=GROOVE, bd=5, command=self.solve)
        self.solveButton.place(x=750, y=5)
        # Clear button
        self.clearButton = Button(self.root, text='Clear', font=(
            'Fira Code', 15, 'bold'), justify='center', bg='green', fg='black', relief=GROOVE, bd=5, command=self.clear)
        self.clearButton.place(x=850, y=5)
        # validate button
        self.validateButton = Button(self.root, text='Validate', font=(
            'Fira Code', 15, 'bold'), bg='green', justify='center', fg='black', relief=GROOVE, bd=5, command=self.validate)
        self.validateButton.place(x=950, y=5)
        # generate random button
        self.generateButton = Button(self.root, text='Generate Random', font=(
            'Fira Code', 15, 'bold'), bg='green', justify='center', fg='black', relief=GROOVE, bd=5, command=self.generate_random)
        self.generateButton.place(x=1000, y=100)
        # time counter
        self.timeLabel = Label(self.root, text='Time', font=(
            'Segoe UI', 15, 'italic'), bg='green', justify='center', width=12, fg='black', relief=GROOVE, bd=5)
        self.timeLabel.place(x=850, y=100)
        self.time = StringVar()
        self.time.set('0 seconds')
        self.timeDisplay = Label(self.root, bg='gray', textvariable=self.time, font=(
            'Segoe UI', 15))
        self.timeDisplay.place(x=845, y=140)
        # open solution button
        self.openButton = Button(self.root, text='Open Solution', font=(
            'Fira Code', 15, 'bold'), bg='green', justify='center', fg='black', relief=GROOVE, bd=5, command=self.open_solution)
        self.openButton.place(x=1000, y=200)
    # Open the solution file for the selected problem

    def open_solution(self):
        if self.selected_difficulty.get() in ['Problem1', 'Problem2', 'Problem3', 'Easy', 'Medium', 'Hard', 'Custom']:
            try:
                with open(f'Sudoku Solver/output/{self.selected_difficulty.get()}_output.txt', 'r') as f:
                    solution = f.read()
                    # Split the solution into individual problems
                    solution_problems = solution.strip().split('\n')

                    # Format each problem with a bullet point and problem number
                    formatted_solution = ''
                    for i, line in enumerate(solution_problems):
                        if line.strip():
                            formatted_solution += f'Problem {i + 1}: {line.strip()}\n'

                    # Create a new Toplevel window
                    solution_window = Toplevel(self.root)
                    solution_window.title("Solution")
                    solution_window.geometry("850x750")

                    # Add a Text widget with a scrollbar
                    text_widget = Text(solution_window, wrap='word')
                    text_widget.insert('1.0', formatted_solution)

                    # Configure the font size and style
                    text_widget.tag_configure('font', font=('Fira Code', 12))
                    text_widget.tag_add('font', '1.0', 'end')

                    text_widget.config(state='disabled')

                    scrollbar = Scrollbar(
                        solution_window, orient=VERTICAL, command=text_widget.yview)
                    text_widget.config(yscrollcommand=scrollbar.set)

                    text_widget.pack(side='left', fill='both', expand=True)
                    scrollbar.pack(side=RIGHT, fill=Y)

                    # Make the window resizable
                    solution_window.resizable(True, True)

            except FileNotFoundError:
                messagebox.showerror(
                    'File Not Found', 'Solution file not found for this problem')
        else:
            messagebox.showerror(
                'Invalid Selection', 'Please select a problem to view its solution')

    def validate(self):
        sudoku_grid = ''
        invalid_input = False
        for i in range(9):
            for j in range(9):
                cell_value = self.cells[i][j].get()
                if cell_value == '':
                    sudoku_grid += '0'
                elif cell_value.isdigit():
                    sudoku_grid += cell_value
                else:
                    invalid_input = True
                    break
            if invalid_input:
                break
        if invalid_input:
            messagebox.showerror(
                'Invalid Input', 'Please enter valid digits only.')
        else:
            sudoku = csp(grid=sudoku_grid)
            # Check if any constraints are violated
            for var in sudoku.variables:
                if len(sudoku.values[var]) == 1:
                    d_val = sudoku.values[var]
                    for d2 in sudoku.peers[var]:
                        if sudoku.values[d2] == d_val:
                            messagebox.showerror(
                                "Invalid Input", "The Sudoku grid violates some constraints.")
                            return
            # If no constraints are violated, write the Sudoku grid string to a file
            messagebox.showinfo(
                "Valid Input", "The Sudoku grid violates no constraints.")
            with open('Sudoku Solver/input/Custom.txt', 'w') as f:
                f.write(sudoku_grid)
    # Solve the Sudoku puzzle with multithreading

    def solve(self):
        # Disable the Solve button to prevent multiple threads
        self.solveButton.config(state=DISABLED)

        # Start the solve process in a new thread
        solve_thread = threading.Thread(target=self._solve)
        solve_thread.start()
    # Solve the Sudoku puzzle

    def _solve(self):
        array = []
        if self.selected_difficulty.get() == 'Custom':
            # Read the grid from the GUI
            grid = ''
            self.initial_cells = set()
            for i in range(9):
                for j in range(9):
                    cell_value = self.cells[i][j].get()
                    if cell_value == '':
                        grid += '0'
                    elif cell_value.isdigit():
                        grid += cell_value
                        self.cells[i][j].config(fg='blue')
                        self.initial_cells.add((i, j))
                    else:
                        messagebox.showerror(
                            'Invalid Input', 'Please enter valid digits only.')
                        return
            array.append(grid)
        if self.selected_difficulty.get() in ['Problem1', 'Problem2', 'Problem3', 'Easy', 'Medium', 'Hard']:
            with open(f'Sudoku Solver/input/{self.selected_difficulty.get()}.txt', 'r') as ins:
                for line in ins:
                    array.append(line.strip())
            ins.close()
        start_time = time.time()
        with open(f'Sudoku Solver/output/{self.selected_difficulty.get()}_output.txt', 'w') as f:
            for grid in array:
                solution = None
                sudoku = csp(grid=grid)
                if self.selected_algorithm.get() == 'Backtracking':
                    solver = BacktrackingSolver(sudoku)
                    solution = solver.Backtracking_Search(sudoku)
                 #   f.write(solver.write(solution) + '\n')
                elif self.selected_algorithm.get() == 'AC-3':
                    solver = AC3Solver(sudoku)
                    solved = solver.AC3()
                    if solved and solver.isComplete():
                        solution = sudoku.values
                #        f.write(solver.write(solution) + '\n')
                if solution is None:
                    f.write('No solution found for this problem\n')
                    if self.selected_difficulty.get() in ['Custom', 'Easy', 'Medium', 'Hard']:
                        messagebox.showerror(
                            'No solution', 'No solution found for this problem')
                else:
                    f.write(solver.write(solution) + '\n')
                # Fill the grid in the GUI with the solution
                    if self.selected_difficulty.get() in ['Custom', 'Easy', 'Medium', 'Hard']:
                        for i in range(9):
                            for j in range(9):
                                self.cells[i][j].delete(0, 'end')
                                self.cells[i][j].insert(
                                    0, solution[f'{chr(65+i)}{j+1}'])
                                if (i, j) in self.initial_cells:
                                    self.cells[i][j].config(fg='blue')
                                else:
                                    self.cells[i][j].config(fg='green')
        end_time = time.time()  # End the timer
        elapsed_time = end_time - start_time
        self.time.set(f'{elapsed_time:.3f} seconds')
        # Re-enable the Solve button
        self.solveButton.config(state=NORMAL)
    # Generate a random Sudoku puzzle

    def generate_random(self):
        self.clear()

        # Create a partially filled board
        def create_initial_board():
            board = [['0'] * 9 for _ in range(9)]
            # Fill some cells with random numbers to create a partially filled board
            for _ in range(17):
                row, col = random.randint(0, 8), random.randint(0, 8)
                num = str(random.randint(1, 9))
                while not is_valid(board, row, col, num):
                    num = str(random.randint(1, 9))
                board[row][col] = num
            return board

        # Check if a number can be placed in the board without breaking the rules
        def is_valid(board, row, col, num):
            for i in range(9):
                if board[row][i] == num or board[i][col] == num:
                    return False
            start_row, start_col = 3 * (row // 3), 3 * (col // 3)
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    if board[i][j] == num:
                        return False
            return True

        # Convert the board to a grid string
        def board_to_grid(board):
            return ''.join(''.join(row) for row in board)

        # Use your existing solver to solve the board
        def solve_initial_board(board):
            grid = board_to_grid(board)
            sudoku = csp(grid=grid)
            # or the algorithm of your choice
            solver = BacktrackingSolver(sudoku)
            solution = solver.Backtracking_Search(sudoku)
            if solution:
                solved_board = [
                    [solution[f'{chr(65 + i)}{j + 1}'] for j in range(9)] for i in range(9)]
                return solved_board
            return None

        # Remove digits to create the puzzle
        def create_puzzle(board, num_holes):
            holes = set()
            while len(holes) < num_holes:
                row, col = random.randint(0, 8), random.randint(0, 8)
                if board[row][col] != '0':
                    holes.add((row, col))
                    board[row][col] = '0'
            return board

        initial_board = create_initial_board()
        solved_board = solve_initial_board(initial_board)

        if not solved_board:
            messagebox.showerror(
                'Error', 'Failed to generate a valid Sudoku puzzle.')
            return

        difficulty = self.selected_difficulty.get()
        if difficulty == 'Easy':
            num_holes = 30
        elif difficulty == 'Medium':
            num_holes = 40
        elif difficulty == 'Hard':
            num_holes = 50
        else:
            num_holes = 40

        puzzle_board = create_puzzle(solved_board, num_holes)
        puzzle_grid = board_to_grid(puzzle_board)

        # Ensure the grid length is 81 characters
        if len(puzzle_grid) != 81:
            messagebox.showerror('Invalid Puzzle Generation',
                                 'Generated puzzle is not 81 characters long.')
            return

        # Save the generated puzzle to a file
        with open(f'Sudoku Solver/input/{difficulty}.txt', 'w') as f:
            f.write(puzzle_grid)

        # Display the puzzle in the GUI
        self.initial_cells = set()
        for i in range(9):
            for j in range(9):
                if puzzle_board[i][j] != '0':
                    self.cells[i][j].insert(0, puzzle_board[i][j])
                    self.cells[i][j].config(fg='blue')
                    self.initial_cells.add((i, j))

    # Clear the Sudoku grid

    def clear(self):
        self.time.set('0 seconds')
        for i in range(9):
            for j in range(9):
                self.cells[i][j].delete(0, 'end')


if __name__ == "__main__":
    root = Tk()
    app = SudokuSolver.get_instance(root)
    root.mainloop()
