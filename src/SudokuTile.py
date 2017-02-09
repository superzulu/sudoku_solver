'''
Created on Feb 9, 2017

@author: Alan Matthews
'''

class SudokuTile(object):
    '''
    classdocs
    '''

    '''
    Constructor
    '''
    def __init__(self, params):
        self.values_ = set([1,2,3,4,5,6,7,8,9])
        
    def removeValue(self, value):
        self.values_.discard(value)
        
    def getValue(self):
        if len(self.values_) == 1:
            return self.values_[0]
        else:
            return -1