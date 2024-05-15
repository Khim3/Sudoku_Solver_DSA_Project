from csp import *
from copy import deepcopy
import util
import queue
from copy import deepcopy



class HiddenSingle:
    def __init__(self):
        self.csp = csp
    # HIDDEN SINGLE ALGORITHM
    def Hidden_Single(self, csp):
        for unit in csp.unitlist:
            for digit in digits:
                dplaces = [squares for squares in unit if digit in csp.values[squares]]
                if len(dplaces) == 1:
                    csp.values[dplaces[0]] = digit
        return csp
    # CHECKS IF THE SUDOKU IS COMPLETE OR NOT
    def isComplete(self, csp):
        for variable in squares:
            if len(csp.values[variable]) > 1:
                return False
        return True
    # WRITES THE SOLVED SUDOKU IN THE FORM OF A STRING
    def write(self, values):
        output = ""
        for variable in squares:
            output = output + values[variable]
        return output