import tkinter as tk
from tkinter import *
from tkinter import ttk
from random import randint
from search import Backtracking, AC3
import random
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
        self.algoMenu.current(0)
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
        if self.selected_difficulty.get() != 'Custom':
            # Read the Sudoku problem from a file
            with open(f'input/{self.selected_difficulty.get()}.txt', 'r') as f:
                problem = [list(map(int, line.strip())) for line in f]
        else:
            # Get the Sudoku problem from the grid
            problem = [[int(self.cells[i][j].get()) if self.cells[i][j].get(
            ) != '' else 0 for j in range(9)] for i in range(9)]

    def clear(self):
        for i in range(9):
            for j in range(9):
                self.cells[i][j].delete(0, 'end')


if __name__ == "__main__":
    root = Tk()
    app = SudokuSolver.get_instance(root)
    root.mainloop()
