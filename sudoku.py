import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
from random import randint
from Backtrack import *
from AC3 import *
from csp import *
from HiddenSingle import *
import time


class SudokuSolver:
    _instance = None

    def __init__(self, root):
        self.root = root
        self.root.title('Sudoku Solver')
        self.root.geometry('1280x720')
        self.root.config(bg='gray')
        self.create_widgets()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def get_instance(cls, root):
        if not cls._instance:
            cls._instance = cls(root)
        return cls._instance

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
        # Algorithm selection
        self.selected_algorithm = StringVar()
        self.algoLabel = Label(self.root, text='Algorithm: ', font=(
            'Fira Code', 15, 'italic'), bg='green', width=12, fg='black', relief=GROOVE, bd=5)
        self.algoLabel.place(x=1, y=5)

        self.algoMenu = ttk.Combobox(self.root, height=10, width=15, font=('Fira Code', 15, 'bold'), textvariable=self.selected_algorithm,
                                     values=['Backtracking', 'AC-3', 'DLX'])
        self.algoMenu.place(x=160, y=8)
        self.algoMenu.current(2)
        # Difficulty selection
        self.selected_difficulty = StringVar()
        self.difficultyLabel = Label(self.root, text='Difficulty: ', font=(
            'Fira Code', 15, 'italic'), bg='green', width=11, fg='black', relief=GROOVE, bd=5)
        self.difficultyLabel.place(x=370, y=5)
        self.difficultyMenu = ttk.Combobox(self.root, height=10, width=12, font=('Fira Code', 15, 'bold'), textvariable=self.selected_difficulty,
                                           values=['Easy', 'Medium', 'Hard', 'Custom'])
        self.difficultyMenu.place(x=515, y=8)
        self.difficultyMenu.current(0)

        # Solve button
        self.solveButton = Button(self.root, text='Solve', font=(
            'Fira Code', 15, 'bold'), bg='green', fg='black', relief=GROOVE, bd=5, command=self.solve)
        self.solveButton.place(x=700, y=5)
        # Clear button
        self.clearButton = Button(self.root, text='Clear', font=(
            'Fira Code', 15, 'bold'), bg='green', fg='black', relief=GROOVE, bd=5, command=self.clear)
        self.clearButton.place(x=800, y=5)
        # validate button
        self.validateButton = Button(self.root, text='Validate', font=(
            'Fira Code', 15, 'bold'), bg='green', fg='black', relief=GROOVE, bd=5, command=self.validate)
        self.validateButton.place(x=900, y=5)

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
            with open('input/Custom.txt', 'w') as f:
                f.write(sudoku_grid)


    def solve(self):
        array = []
        with open(f'input/{self.selected_difficulty.get()}.txt', 'r') as ins:
            for line in ins:
                array.append(line.strip())
        ins.close()
        with open(f'output/{self.selected_difficulty.get()}_output.txt', 'w') as f:
            for grid in array:
                solution = None
                sudoku = csp(grid=grid)
                if self.selected_algorithm.get() == 'Backtracking':
                    solver = BacktrackingSolver(sudoku)
                    solution = solver.Backtracking_Search(sudoku)
                    f.write(solver.write(solution) + '\n')
                if self.selected_algorithm.get() == 'AC-3':
                    solver = AC3Solver(sudoku)
                    solved = solver.AC3()
                    if solved and solver.isComplete():
                        solution = sudoku.values
                        f.write(solver.write(solution) + '\n')
                if self.selected_algorithm.get() == 'Hidden Single':
                    pass
                if solution is None:
                    f.write('No solution found for this problem\n')

    def clear(self):
        for i in range(9):
            for j in range(9):
                self.cells[i][j].delete(0, 'end')


if __name__ == "__main__":
    root = Tk()
    app = SudokuSolver.get_instance(root)
    root.mainloop()
