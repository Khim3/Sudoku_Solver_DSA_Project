from csp import *
from copy import deepcopy
import util
import queue


class NakedSingleSolver:
    def __init__(self, csp):
        self.csp = csp

    def solve(self):
        while True:
            progress = False
            for var in self.csp.variables:
                if len(self.csp.values[var]) == 1:
                    continue  # Skip already solved cells

                possible_values = self.csp.values[var]
                single_value = None

                for value in possible_values:
                    if self.is_single_candidate(var, value):
                        if single_value is not None:
                            single_value = None
                            break
                        single_value = value

                if single_value:
                    self.csp.values[var] = single_value
                    progress = True

            if not progress:
                break

        return self.csp.values

    def is_single_candidate(self, var, value):
        """Check if value is the only candidate for the variable var."""
        for peer in self.csp.peers[var]:
            if value in self.csp.values[peer]:
                return False
        return True

    def write(self, solution):
        """Convert the solution to a formatted string."""
        output = ''
        for i, var in enumerate(self.csp.variables):
            output += solution[var]
            if (i + 1) % 9 == 0:
                output += '\n'
        return output