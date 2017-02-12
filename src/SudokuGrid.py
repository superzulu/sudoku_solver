'''
Created on Feb 11, 2017

@author: Alan
'''

from src import SudokuTile

class SudokuGrid(object):
    '''
    classdocs
    '''

    def __init__(self, initialValues):
        '''
        Constructor
        '''
        self._tiles = []
        self._rows = [[] for _ in range(9)]
        self._cols = [[] for _ in range(9)]
        self._boxs = [[] for _ in range(9)]

        for i in range(81):
            row = int(i / 9)
            col = i % 9
            box = (int(row / 3) * 3) + int(col / 3)
            
            self._tiles.append(SudokuTile.SudokuTile(row, col, box))

            self._rows[row].append(self._tiles[i])
            self._cols[col].append(self._tiles[i])
            self._boxs[box].append(self._tiles[i])  

        
        for i in range(9):
            for j in self._rows[i]:
                for k in self._rows[i]:
                    if (j != k):
                        j.addAssociate("Row", k)
                        
            for j in self._cols[i]:
                for k in self._cols[i]:
                    if (j != k):
                        j.addAssociate("Col", k)
                        
            for j in self._boxs[i]:
                for k in self._boxs[i]:
                    if (j != k):
                        j.addAssociate("Box", k)

        for i in range(81):
            if initialValues[i] >= 1 and initialValues[i] <= 9:
                self._tiles[i].setValue(initialValues[i])

    def printSolution(self):
        for row in self._rows:
            print(" ".join([str(i.getPossibles()) for i in row]))
             
    def getSolutionString(self):
        return ",".join([str(tile.getValue()) for tile in self._tiles])   