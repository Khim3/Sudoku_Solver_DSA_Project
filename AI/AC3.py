
import queue
from csp import *

def AC3(csp):
    q = queue.Queue()
    for arc in csp.constraints:
        q.put(arc)
    i = 0 
    while not q.empty():
        (Xi, Xj) = q.get()
        i = i + 1
        if Revise(csp, Xi, Xj):
            if len(csp.values[Xi]) == 0:
                return False
            for Xk in (csp.peers[Xi] - set(Xj)):
                q.put((Xk, Xi))
    return True

def Revise(csp, Xi, Xj):
    revised = False
    values = set(csp.values[Xi])
    for x in values: 
        if not isConsistent(csp, x, Xi, Xj):
            csp.values[Xi] = csp.values[Xi].replace(x, '')
            revised = True
    return revised

def isConsistent(csp, x, Xi, Xj):
    for y in csp.values[Xj]:
        if Xj in csp.peers[Xi] and y!=x:
            return True
    return False

def isComplete(csp):
    for variable in squares:
        if len(csp.values[variable])>1:
            return False
    return True

def display(values):
    """
    Display the solved sudoku on screen
    """
    for row in rows:
        if row in 'DG':
            print("-------------------------------------------")
        for col in cols:
            if col in '47':
                print(' | ', values[row + col], ' ', end=' ')
            else:
                print(values[row + col], ' ', end=' ')
        print(end='\n')

def write(values):
    output = ""
    for variable in squares:
        output = output + values[variable]
    return output

