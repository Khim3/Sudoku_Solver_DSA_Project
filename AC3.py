from csp import *
from copy import deepcopy
import util
import queue
from copy import deepcopy


class AC3:
    def __init__(self, csp):
        self.csp = csp

    def AC3(self):
        q = queue.Queue()
        for arc in self.csp.constraints:
            q.put(arc)
        i = 0
        while not q.empty():
            (Xi, Xj) = q.get()
            i = i + 1
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
