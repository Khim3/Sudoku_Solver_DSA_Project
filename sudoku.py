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
        self.root.title('Sorting Visualizer')
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

if __name__ == "__main__":
    root = Tk()
    app = SudokuSolver.get_instance(root)
    root.mainloop()
