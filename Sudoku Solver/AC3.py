# Name: Nguyen Nhat Khiem - ITDSIU21091
# Purpose: Implementing the AC3Solver class for the Sudoku Solver
from csp import *
from copy import deepcopy
import queue


class AC3Solver:
    def __init__(self, csp):
        self.csp = csp

    def AC3(self):
        q = queue.Queue()
        for Xi in self.csp.variables:
            for Xj in self.csp.peers[Xi]:
                q.put((Xi, Xj))
        while not q.empty():
            (Xi, Xj) = q.get()
            if self.Revise(Xi, Xj):
                if len(self.csp.values[Xi]) == 0:
                    return False
                for Xk in (self.csp.peers[Xi] - set(Xj)):
                    q.put((Xk, Xi))
        return True

    def Revise(self, Xi, Xj):
        revised = False
        values = set(self.csp.values[Xi])
        for x in values:
            if not self.isConsistent(x, Xi, Xj):
                self.csp.values[Xi] = self.csp.values[Xi].replace(x, '')
                revised = True
        return revised

    def isConsistent(self, x, Xi, Xj):
        for y in self.csp.values[Xj]:
            if Xj in self.csp.peers[Xi] and y != x:
                return True
        return False

    def isComplete(self):
        for variable in squares:
            if len(self.csp.values[variable]) > 1:
                return False
        return True

    def write(self, values):
        output = ""
        for variable in squares:
            output = output + values[variable]
        return output
