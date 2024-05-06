# THE FUNCTION WHICH SOLVES ALL THE SUDOKU PROBLEMS
# IN THE INPUT FILE USING BACKTRACKING AND WRITES THE OUTPUT TO THE OUTPUT FILE
from search import *
import time
import argparse

if __name__ == "__main__":
    argument_parser = argparse.ArgumentParser(description="Sudoku Solving Problem")
    argument_parser.add_argument("--inputFiles", type=str, nargs='+', help="Sudoku Input Files")
    args = argument_parser.parse_args()

    filenames = args.inputFiles
    start = time.time()
    f = open("output.txt", "w")

    for filename in filenames:
        array = []
        with open(filename, "r") as ins:
            for line in ins:
                array.append(line)
        ins.close()

        # Write the header to the output file
        f.write("------------------------------------" + filename.upper() + "----------------------------------\n")

        i = 0
        boardno = 0
        for grid in array:
            startpuzle = time.time()
            boardno = boardno + 1
            sudoku = csp(grid=grid)
            solved = Backtracking_Search(sudoku)
            print("The board - ", boardno, " takes ", time.time() - startpuzle, " seconds")
            if solved != "FAILURE":
                print("After solving: ")
                display(solved)
                f.write(write(solved)+"\n")
                i = i + 1

    f.close()
    print ("Number of problems solved is: ", i)
    print ("Time taken to solve the puzzles is: ", time.time() - start)
