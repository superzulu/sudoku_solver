'''
Created on Feb 9, 2017

@author: Alan Matthews
'''

import sys

class SudokuTile(object):
    '''
    classdocs
    '''

    def __init__(self, row, col, box):
        '''
        Constructor
        
        TODO: Get rid of the _row, _col, _box
        '''
        self._row = row
        self._col = col
        self._box = box
        self._values = set([1,2,3,4,5,6,7,8,9])
        self._sameRow = set()
        self._sameCol = set()
        self._sameBox = set()
        self._allAssociates = set()
        
    def removeValue(self, value):
        if len(self._values) > 1:
            self._values.discard(value)
            
            if len(self._values) == 0:
                print("Error, zero possible values!")
                sys.exit(1)
            elif len(self._values) == 1:
                for i in self._allAssociates:
                    i.removeValue(list(self._values)[0])
        
    def setValue(self, value):
        self._values = set([value])
        
        for a in self._allAssociates:
            a.removeValue(value)
        
    def getPossibles(self):
        return self._values
        
    def getValue(self):
        if len(self._values) == 1:
            return list(self._values)[0]
        else:
            return 0
        
    def addAssociate(self, setType, tile):
        if setType == "Row":
            self._sameRow.add(tile)
        elif setType == "Col":
            self._sameCol.add(tile)
        elif setType == "Box":
            self._sameBox.add(tile)
        else:
            print("Error, invalid type: " + setType)
            sys.exit(1)
            
        self._allAssociates.add(tile)