'''
This problem is an interactive problem.
You can't access the Binary Matrix directly.  
You may only access the matrix using a BinaryMatrix interface:
1. BinaryMatrix.get(x, y) returns the element of the matrix at index (x, y) (0-indexed).
2. BinaryMatrix.dimensions() returns a list of 2 elements [n, m], which means the matrix is n * m.
'''

# Hint (Optimal Approach) 
# Imagine there is a pointer p(x, y) starting from top right corner 
# p can only move left or down 
# If the value at p is 0, move down 
# If the value at p is 1, move left

#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()
        
        currentRow = 0
        currentColumn = cols - 1
        
        while currentRow < rows and currentColumn >= 0:
            if binaryMatrix.get(currentRow, currentColumn) == 0:
                currentRow += 1
            else:
                currentColumn -= 1
            
        if currentColumn != cols - 1:
            return currentColumn + 1
        else:
            return -1