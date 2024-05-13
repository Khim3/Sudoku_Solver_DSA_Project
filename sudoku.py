import tkinter as tk
from tkinter import *
from tkinter import ttk
from random import randint
from Backtrack import *
from AC3 import *
from HiddenSingle import *
from csp import *
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
        # Sudoku grid
        self.grid_frame = Frame(self.root)
        self.grid_frame.place(x=50, y=100)

        self.cells = []
        for i in range(9):
            row = []
            for j in range(9):
                entry = Entry(self.grid_frame, width=5, font=(
                    'Fira Code', 20), justify='center')
                entry.grid(row=i, column=j)
                row.append(entry)
            self.cells.append(row)
        # Algorithm selection
        self.selected_algorithm = StringVar()
        self.algoLabel = Label(self.root, text='Algorithm: ', font=(
            'Fira Code', 15, 'italic'), bg='green', width=12, fg='black', relief=GROOVE, bd=5)
        self.algoLabel.place(x=1, y=5)

        self.algoMenu = ttk.Combobox(self.root, height=10, width=15, font=('Fira Code', 15, 'bold'), textvariable=self.selected_algorithm,
                                     values=['Backtracking', 'AC-3', 'Hidden Single'])
        self.algoMenu.place(x=160, y=8)
        self.algoMenu.current(1)
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

    def solve(self):
        array = []
        # Open the input file and read the problems
        with open(f'input/{self.selected_difficulty.get()}.txt', 'r') as ins:
            for line in ins:
                array.append(line)
        ins.close()
        # Open the output file
        with open('output.txt', 'w') as f:
            # Solve each problem
            for grid in array:
                solution = None
                # Create a CSP object
                sudoku = csp(grid=grid)
                # Solve the problem using the selected algorithm
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
                    solver = HiddenSingle()
                    solution = solver.Hidden_Single(sudoku)
                # If a solution was found, write it to the output file
                if solution is  None:                
                    f.write('No solution found for this problem.\n')

    def clear(self):
        for i in range(9):
            for j in range(9):
                self.cells[i][j].delete(0, 'end')


if __name__ == "__main__":
    root = Tk()
    app = SudokuSolver.get_instance(root)
    root.mainloop()
