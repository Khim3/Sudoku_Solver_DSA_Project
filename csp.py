from util import *

class csp:
    def __init__(self, domain=digits, grid=""):
        # Variables: All cells in the Sudoku grid
        self.variables = cross(rows, cols)
        # Domain for each variable: 1-9
        self.domain = {variable: domain for variable in self.variables}
        # Unitlist: Three types of units (rows, columns, sub-boxes)
        self.unitlist = ([cross(rows, c) for c in cols] +
                         [cross(r, cols) for r in rows] +
                         [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')])
        # Units: Dictionary mapping each variable to its units
        self.units = {variable: [
            unit for unit in self.unitlist if variable in unit] for variable in self.variables}
        # Peers: Dictionary mapping each variable to its peers (variables in the same unit)
        self.peers = {variable: set(
            sum(self.units[variable], [])) - {variable} for variable in self.variables}
        # Constraints: Ensures no two variables in the same unit have the same value
        self.constraints = lambda x, y: x != y
        # Values: Dictionary representing the current assignment of values to variables
        self.values = self.getDict(grid)

    def getDict(self, grid=""):
        i = 0
        values = dict()
        for cell in self.variables:
            if grid[i] != '0':
                values[cell] = grid[i]
            else:
                values[cell] = digits
            i = i + 1
        return values
