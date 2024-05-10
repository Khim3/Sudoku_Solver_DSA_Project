import inspect
import sys

digits = cols = "123456789"
rows = "ABCDEFGHI"


def raiseNotDefined():
    fileName = inspect.stack()[1][1]
    line = inspect.stack()[1][2]
    method = inspect.stack()[1][3]
    sys.exit(1)


def cross(A, B):

    return [a + b for a in A for b in B]

squares = cross(rows, cols)
