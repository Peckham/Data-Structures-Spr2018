# Tavish Peckham - Assignment 4 - Due 3.6.18
import random


class Array2D:
    # Creates a 2-D array of size numRows x numCols.
    def __init__(self, numRows, numCols):
        # Create a 1-D array to store an array reference for each row.
        self._theRows = [None] * numRows

        # Create the 1-D arrays for each row of the 2-D array.
        for i in range(numRows):
            self._theRows[i] = [None] * numCols

    # Returns the number of rows in the 2-D array.
    def numRows(self):
        return len(self._theRows)

    # Returns the number of columns in the 2-D array.
    def numCols(self):
        return len(self._theRows[0])

    # Clears the array by setting every element to the given value.
    def clear(self, value):
        for row in range(self.numRows()):
            for col in range(self.numCols()):
                self[row, col] = value

    # Gets the contents of the element at position [i, j]
    def __getitem__(self, ndxTuple):
        assert len(ndxTuple) == 2, "Invalid number of array subscripts."
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row < self.numRows() \
            and col >= 0 and col < self.numCols(), \
            "Array subscript out of range."
        the1dArray = self._theRows[row]
        return the1dArray[col]

    # Sets the contents of the element at position [i,j] to value.
    def __setitem__(self, ndxTuple, value):
        assert len(ndxTuple) == 2, "Invalid number of array subscripts."
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row < self.numRows() \
            and col >= 0 and col < self.numCols(), \
            "Array subscript out of range."
        the1dArray = self._theRows[row]
        the1dArray[col] = value


class Matrix:
    # Creates a matrix of size numRows x numCols initialized to 0.
    def __init__(self, numRows, numCols):
        self._theGrid = Array2D(numRows, numCols)
        self._theGrid.clear(0)

    # Returns the number of rows in the matrix.
    def numRows(self):
        return self._theGrid.numRows()

    # Returns the number of columns in the matrix.
    def numCols(self):
        return self._theGrid.numCols()

    # Returns the value of element (i, j): x[i,j]
    def __getitem__(self, ndxTuple):
        return self._theGrid[ndxTuple[0], ndxTuple[1]]

    # Sets the value of element (i,j) to the value s: x[i,j] = s
    def __setitem__(self, ndxTuple, scalar):
        self._theGrid[ndxTuple[0], ndxTuple[1]] = scalar

    # Scales the matrix by the given scalar.
    def scaleBy(self, scalar):
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                self.__setitem__((i, j), self.__getitem__((i, j)) * scalar)

    # Creates and returns a new matrix that is the transpose of this matrix.
    def transpose(self):
        transposed = Matrix(self.numCols(), self.numRows())
        for i in range(self.numCols()):
            for j in range(self.numRows()):
                transposed.__setitem__((i, j), self.__getitem__((j, i)))
        return transposed

    # Creates and returns a new matrix that results from matrix addition.
    def __add__(self, rhsMatrix):
        added = Matrix(self.numRows(), self.numCols())
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                added.__setitem__((i, j), self.__getitem__((i, j)) +
                                  rhsMatrix.__getitem__((i, j)))
        return added

    # Creates and returns a new matrix that results from matrix subtraction.
    def __sub__(self, rhsMatrix):
        subtracted = Matrix(self.numRows(), self.numCols())
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                subtracted.__setitem__((i, j), self.__getitem__((i, j)) -
                                       rhsMatrix.__getitem__((i, j)))
        return subtracted

    # Creates and returns a new matrix resulting from matrix multiplication.
    def __mul__(self, rhsMatrix):
        multiplied = Matrix(self.numRows(), rhsMatrix.numCols())
        for i in range(self.numRows()):
            for j in range(rhsMatrix.numCols()):
                for k in range(rhsMatrix.numRows()):
                    multiplied.__setitem__((i, j), multiplied.__getitem__
                                           ((i, j)) + self.__getitem__((i, k))
                                           * rhsMatrix.__getitem__((k, j)))
        return multiplied

    def __str__(self):
        answer = []  # Use list for efficiency
        for row in range(self.numRows()):
            for col in range(self.numCols()):
                answer.append(str(self[row, col]) + '\t')
            answer.append('\n')
        return ''.join(answer)


# Test codes
m1 = Matrix(3, 2)
m2 = Matrix(2, 3)
m3 = Matrix(3, 2)

# Fill m1，m2, m3 with random values
for row in range(m1.numRows()):
    for col in range(m1.numCols()):
        m1[row, col] = random.randint(-9, 9)

for row in range(m2.numRows()):
    for col in range(m2.numCols()):
        m2[row, col] = random.randint(-9, 9)

for row in range(m3.numRows()):
    for col in range(m3.numCols()):
        m3[row, col] = random.randint(-9, 9)
"""
print("matrix 1 is: \n", m1, sep="")
print("matrix 2 is: \n", m2, sep="")
print("matrix 3 is: \n", m3, sep="")
print("------------------------------------------------------")
print("Transpose of matrix 1:\n", m1.transpose(), sep="")
print("Transpose of matrix 2:\n", m2.transpose(), sep="")
print("Transpose of matrix 3:\n", m3.transpose(), sep="")
print("------------------------------------------------------")
print("matrix 1 add matrix 3：\n", m1 + m3, sep="")
print("matrix 1 subtract matrix 3：\n", m1 - m3, sep="")
print("matrix 1 multiply matrix 2：\n", m1 * m2, sep="")
print("------------------------------------------------------")
m1.scaleBy(-4)
print("Scale matrix m1 -4 times: \n", m1, sep="")
"""

aa = Matrix(3, 3)
ab = Matrix(3, 3)

ba = Matrix(3, 3)
bb = Matrix(3, 4)

ca = Matrix(3, 2)
cb = Matrix(2, 5)

aal = [1, 0, 1, 0, -1, -1, -1, 1, 0]
abl = [0, 1, -1, 1, -1, 0, -1, 0, 1]
bal = [1, -3, 0, 1, 2, 2, 2, 1, -1]
bbl = [1, -1, 2, 3, -1, 0, 3, -1, -3, -2, 0, 2]
cal = [0, -1, 7, 2, -4, -3]
cbl = [4, -1, 2, 3, 0, -2, 0, 3, 4, 1]

for row in range(aa.numRows()):
    for col in range(aa.numCols()):
        aa[row, col] = aal.pop(0)

for row in range(ab.numRows()):
    for col in range(ab.numCols()):
        ab[row, col] = abl.pop(0)

for row in range(ba.numRows()):
    for col in range(ba.numCols()):
        ba[row, col] = bal.pop(0)

for row in range(bb.numRows()):
    for col in range(bb.numCols()):
        bb[row, col] = bbl.pop(0)

for row in range(ca.numRows()):
    for col in range(ca.numCols()):
        ca[row, col] = cal.pop(0)

for row in range(cb.numRows()):
    for col in range(cb.numCols()):
        cb[row, col] = cbl.pop(0)

print("A")
print(aa * ab, sep="")
print("B")
print(ba * bb, sep="")
print("C")
print(ca * cb, sep="")
