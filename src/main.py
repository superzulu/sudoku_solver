'''
Created on Feb 11, 2017

@author: Alan
'''

import sys
import time
from src import SudokuGrid

if __name__ == '__main__':
    test = SudokuGrid.SudokuGrid([int(i) for i in sys.argv[1].split(",")])
    test.printSolution()
    print(test.getSolutionString())
    print("Run Time:", time.process_time(), "seconds")