from csp import *
from copy import deepcopy


class BacktrackingSolver:
    def __init__(self, csp):
        self.csp = csp
        self.assignment = {}

    def Backtracking_Search(self, csp_instance):
        self.csp = csp_instance
        return self.Recursive_Backtracking()

    def Recursive_Backtracking(self):
        if self.isComplete():
            return self.assignment

        var = self.Select_Unassigned_Variables()
        domain = deepcopy(self.csp.values)

        for value in self.csp.values[var]:
            if self.isConsistent(var, value):
                self.assignment[var] = value
                inferences = {}
                inferences = self.Inference(inferences, var, value)
                if inferences != "FAILURE":
                    result = self.Recursive_Backtracking()
                    if result != "FAILURE":
                        return result

                del self.assignment[var]
                self.csp.values.update(domain)

        return "FAILURE"

    def Inference(self, inferences, var, value):
        inferences[var] = value

        for neighbor in self.csp.peers[var]:
            if neighbor not in self.assignment and value in self.csp.values[neighbor]:
                if len(self.csp.values[neighbor]) == 1:
                    return "FAILURE"

                remaining = self.csp.values[neighbor] = self.csp.values[neighbor].replace(
                    value, "")

                if len(remaining) == 1:
                    flag = self.Inference(inferences, neighbor, remaining)
                    if flag == "FAILURE":
                        return "FAILURE"

        return inferences

    def Select_Unassigned_Variables(self):
        unassigned_variables = dict((squares, len(
            self.csp.values[squares])) for squares in self.csp.values if squares not in self.assignment.keys())
        mrv = min(unassigned_variables, key=unassigned_variables.get)
        return mrv

    def isComplete(self):
        return set(self.assignment.keys()) == set(squares)

    def isConsistent(self, var, value):
        for neighbor in self.csp.peers[var]:
            if neighbor in self.assignment.keys() and self.assignment[neighbor] == value:
                return False
        return True

    def write(self, values):
        output = ""
        for variable in squares:
            output += values[variable]
        return output
