from csp import *
from copy import deepcopy

class HiddenSingleSolver:
    def __init__(self, csp):
        self.csp = csp

    def Hidden_Single(self):
        while True:
            solved_values_before = len([cell for cell in self.csp.values if len(self.csp.values[cell]) == 1])
            self.hidden_single()
            solved_values_after = len([cell for cell in self.csp.values if len(self.csp.values[cell]) == 1])
            if solved_values_before == solved_values_after:
                break
        return self.isComplete()

    def hidden_single(self):
        for unit in self.csp.unitlist:
            for digit in self.csp.domain:
                dplaces = [cell for cell in unit if digit in self.csp.values[cell]]
                if len(dplaces) == 1:
                    print(f"Hidden single found for digit {digit} in cell {dplaces[0]}")  # Debugging statement
                    # Assign the digit to the cell
                    self.csp.values[dplaces[0]] = digit

    def isComplete(self):
        return all(len(self.csp.values[cell]) == 1 for cell in self.csp.values)

    def display(self, values):
        for row in rows:
            if row in 'DG':
                print("-------------------------------------------")
            for col in cols:
                if col in '47':
                    print(' | ', values[row + col], ' ', end=' ')
                else:
                    print(values[row + col], ' ', end=' ')
            print(end='\n')

    def write(self, values):
        output = ""
        for variable in squares:
            output = output + values[variable]
        return output


