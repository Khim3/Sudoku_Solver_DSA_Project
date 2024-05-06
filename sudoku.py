import tkinter as tk
from tkinter import *
from tkinter import ttk
from random import randint
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
        # Algorithm selection
        self.selected_algorithm = StringVar()
        self.algoLabel = Label(self.root, text='Algorithm: ', font=(
            'Segoe UI', 15, 'italic'), bg='green', width=10, fg='black', relief=GROOVE, bd=5)
        self.algoLabel.place(x=1, y=5)

        self.algoMenu = ttk.Combobox(self.root, height=10, width=15, font=('Segoe UI', 15, 'bold'), textvariable=self.selected_algorithm,
                                     values=['Backtracking', 'AC-3', 'Constraint'])
        self.algoMenu.place(x=125, y=8)
        self.algoMenu.current(0)
        # Difficulty selection
        self.selected_difficulty = StringVar()
        self.difficultyLabel = Label(self.root, text='Difficulty: ', font=(
            'Segoe UI', 15, 'italic'), bg='green', width=10, fg='black', relief=GROOVE, bd=5)
        self.difficultyLabel.place(x=250, y=5)
        self.difficultyMenu = ttk.Combobox(self.root, height=10, width=15, font=('Segoe UI', 15, 'bold'), textvariable=self.selected_difficulty,
                                           values=['Easy', 'Medium', 'Hard'])
        self.difficultyMenu.place(x=375, y=8)
        self.algoMenu.current(0)
        

if __name__ == "__main__":
    root = Tk()
    app = SudokuSolver.get_instance(root)
    root.mainloop()
