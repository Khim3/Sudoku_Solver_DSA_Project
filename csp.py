from util import *

class csp:
    def __init__(self, domain=digits, grid=""):
        self.variables = cross(rows, cols)
        self.domain = {variable: domain for variable in self.variables}
        self.unitlist = ([cross(rows, c) for c in cols] +
                         [cross(r, cols) for r in rows] +
                         [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')])
        self.units = {variable: [
            unit for unit in self.unitlist if variable in unit] for variable in self.variables}
        self.peers = {variable: set(
            sum(self.units[variable], [])) - {variable} for variable in self.variables}
        self.constraints = lambda x, y: x != y
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
