from csp import *
from copy import deepcopy
import util
import queue


class Backtracking:
  # Backtracking Search Algorithm
    def Backtracking_Search(self, csp):
        return self.Backtrack({}, csp)

    # THE RECURSIVE FUNCTION WHICH ASSIGNS VALUE USING BACKTRACKING
    def Backtrack(self, assignment, csp):
        if self.isComplete(assignment):
            return assignment

        var = self.Select_Unassigned_Variables(assignment, csp)
        domain = deepcopy(csp.values)

        for value in csp.values[var]:
            if self.isConsistent(var, value, assignment, csp):
                assignment[var] = value
                inferences = {}
                inferences = self.Inference(
                    assignment, inferences, csp, var, value)
                if inferences != "FAILURE":
                    result = self.Backtrack(assignment, csp)
                    if result != "FAILURE":
                        return result

                del assignment[var]
                csp.values.update(domain)

        return "FAILURE"

    # FORWARD CHECKING USING THE CONCEPT OF INFERENCES

    def Inference(assignment, inferences, csp, var, value):
        inferences[var] = value

        for neighbor in csp.peers[var]:
            if neighbor not in assignment and value in csp.values[neighbor]:
                if len(csp.values[neighbor]) == 1:
                    return "FAILURE"

                remaining = csp.values[neighbor] = csp.values[neighbor].replace(
                    value, "")

                if len(remaining) == 1:
                    flag = Inference(assignment, inferences,
                                     csp, neighbor, remaining)
                    if flag == "FAILURE":
                        return "FAILURE"

        return inferences

    # CHECKS IF THE ASSIGNMENT IS COMPLETE

    def isComplete(assignment):
        return set(assignment.keys()) == set(squares)

    # SELECTS THE NEXT VARIABLE TO BE ASSIGNED USING MRV

    def Select_Unassigned_Variables(assignment, csp):
        unassigned_variables = dict((squares, len(
            csp.values[squares])) for squares in csp.values if squares not in assignment.keys())
        mrv = min(unassigned_variables, key=unassigned_variables.get)
        return mrv

    # RETURNS THE STRING OF VALUES OF THE GIVEN VARIABLE

    def Order_Domain_Values(var, assignment, csp):
        return csp.values[var]

    # CHECKS IF THE GIVEN NEW ASSIGNMENT IS CONSISTENT

    def isConsistent(var, value, assignment, csp):
        for neighbor in csp.peers[var]:
            if neighbor in assignment.keys() and assignment[neighbor] == value:
                return False
        return True

    # PERFORMS FORWARD-CHECKING

    def forward_check(csp, assignment, var, value):
        csp.values[var] = value
        for neighbor in csp.peers[var]:
            csp.values[neighbor] = csp.values[neighbor].replace(value, '')

    # WRITES THE SOLVED SUDOKU IN THE FORM OF A STRING

    def write(values):
        output = ""
        for variable in squares:
            output = output + values[variable]
        return output
# -----------------------------------------------------------------------------------------------------------


class AC3:
    # AC-3 Algorithm
    def AC3(self, csp):
        q = queue.Queue()

        for arc in csp.constraints:
            q.put(arc)

        while not q.empty():
            (Xi, Xj) = q.get()

            if self.Revise(csp, Xi, Xj):
                if len(csp.values[Xi]) == 0:
                    return False

                for Xk in (csp.peers[Xi] - set(Xj)):
                    q.put((Xk, Xi))

        return True

    # WORKING OF THE REVISE ALGORITHM
    def Revise(self, csp, Xi, Xj):
        revised = False
        values = set(csp.values[Xi])

        for x in values:
            if not self.isconsistent(csp, x, Xi, Xj):
                csp.values[Xi] = csp.values[Xi].replace(x, '')
                revised = True

        return revised

    # CHECKS IF THE GIVEN ASSIGNMENT IS CONSISTENT
    def isconsistent(self, csp, x, Xi, Xj):
        for y in csp.values[Xj]:
            if Xj in csp.peers[Xi] and y != x:
                return True

        return False

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
