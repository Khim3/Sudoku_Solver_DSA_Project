from Backtrack import *
from AC3 import *
import time
import argparse

#THE MAIN FUNCTION GOES HERE
if __name__ == "__main__":
    """
    The function takes arguments from command line as follow
    python3 sudoku.py --inputFile data/euler.txt --algorithm backtrack or ac3 
    """
    argument_parser = argparse.ArgumentParser(description="Sudoku Solving Problem")
    argument_parser.add_argument("--inputFile", type=str, help="Sudoku Input File")
    argument_parser.add_argument("--algorithm", type=str, choices=["backtrack", "ac3"], default="backtrack", help="Sudoku Search Algorithm")
    try:
        args = argument_parser.parse_args()

        filename = args.inputFile
        algorithm = args.algorithm
        array = []
        with open(filename, "r") as ins:
            for line in ins:
                array.append(line)
        ins.close()
        i = 0
        boardno = 0
        start = time.time()
        f = open("output.txt", "w")
        for grid in array:
            startpuzle = time.time()
            boardno = boardno + 1
            sudoku = csp(grid=grid)
            if (algorithm == "backtrack"):
                solved = Backtracking_Search(sudoku)
                print("The board - ", boardno, " takes ", time.time() - startpuzle, " seconds")
                if solved != "FAILURE":
                    print("After solving: ")
                    display(solved)
                    f.write(write(solved)+"\n")
                    i = i + 1
                else: print("Unable to solve!")
            else:
                solved = AC3(sudoku)
                print("The board - ", boardno, " takes ", time.time() - startpuzle, " seconds")
                if isComplete(sudoku) and solved:
                    print("After solving: ")
                    display(sudoku.values)
                    f.write(write(sudoku.values)+"\n")
                    i = i + 1
                else: print("Unable to solve!")

        f.close()
        print ("Number of problems solved is: ", i)
        print ("Time taken to solve the puzzles is: ", time.time() - start)

    except argparse.ArgumentTypeError as e:
        print(f"Invalid argument: {e}")

