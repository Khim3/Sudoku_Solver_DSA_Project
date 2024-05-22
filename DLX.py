from DLXNode import *

class DLXSolver:
    def __init__(self, matrix):
        self.header = DLXColumn('header')
        self.columns = []
        self.nodes = []

        # Initialize columns
        for col_name in range(len(matrix[0])):
            column = DLXColumn(col_name)
            self.columns.append(column)
            self.header.hook_right(column)

        # Initialize nodes
        for row_index, row in enumerate(matrix):
            prev = None
            for col_index, cell in enumerate(row):
                if cell == 1:
                    column = self.columns[col_index]
                    node = DLXNode(row_index, col_index)
                    column.size += 1
                    if prev is None:
                        prev = node
                    else:
                        prev.hook_right(node)
                    column.hook_down(node)
                    node.column = column
                    self.nodes.append(node)

    def search(self, k=0, solution=[]):
        if self.header.right == self.header:
            return solution

        column = min(self.header.right_iter(), key=lambda col: col.size)
        column.cover()

        for r in column.down_iter():
            solution.append(r.rowID)

            for j in r.right_iter():
                j.column.cover()

            result = self.search(k + 1, solution)
            if result is not None:
                return result

            solution.pop()
            column = r.column

            for j in r.left_iter():
                j.column.uncover()

        column.uncover()
        return None

    def solve(self):
        solution = self.search()
        return solution

    @staticmethod
    def sudoku_to_exact_cover(board):
        matrix = []
        digits = '123456789'

        def cell_to_index(row, col, num):
            return row * 81 + col * 9 + num - 1

        for row in range(9):
            for col in range(9):
                num = board[row * 9 + col]
                if num == '0':
                    for d in digits:
                        matrix.append([0] * 324)
                        matrix[-1][row * 9 + int(d) - 1] = 1
                        matrix[-1][81 + col * 9 + int(d) - 1] = 1
                        matrix[-1][162 + ((row // 3) * 3 + (col // 3)) * 9 + int(d) - 1] = 1
                        matrix[-1][243 + row * 9 + col] = 1
                else:
                    d = int(num)
                    matrix.append([0] * 324)
                    matrix[-1][row * 9 + d - 1] = 1
                    matrix[-1][81 + col * 9 + d - 1] = 1
                    matrix[-1][162 + ((row // 3) * 3 + (col // 3)) * 9 + d - 1] = 1
                    matrix[-1][243 + row * 9 + col] = 1
        return matrix

    @staticmethod
    def exact_cover_to_sudoku(solution):
        board = ['0'] * 81
        for r in solution:
            row = r // 81
            col = (r % 81) // 9
            num = (r % 9) + 1
            board[row * 9 + col] = str(num)
        return ''.join(board)

