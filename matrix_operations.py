import time
import math

from decimal import *
getcontext().prec = 6


## TODO: implemenet a Matrix class with computations

## TODO: implement a Vector class with computations

## transposition

def transpose(amatrix):
    nrow = len(amatrix)
    ncol = len(amatrix[0])
    C = amatrix.copy()
    for i in range(nrow):
        for j in range(ncol):
            C[i][j] = amatrix[i][j]
    return C


## addition of two matrices

def addition(amatrix, another):
    nrow = len(amatrix)
    ncol = len(amatrix[0])
    C = amatrix.copy()
    for i in range(nrow):
        for j in range(ncol):
            C[i][j] = amatrix[i][j] + another[i][j]
    return C


## scalar multiplication

def scalar_multiplication(amatrix, scalar):
    nrow = len(amatrix)
    ncol = len(amatrix[0])
    C = amatrix.copy()
    for i in range(nrow):
        for j in range(ncol):
            C[i][j] = scalar * A[i][j]
    return C


def multiplication(amatrix, another):
    ## create product

    m = len(amatrix)
    n = len(another[0])
    p = len(amatrix[0])

    C = []

    for i in range(m):
        temp = []
        C.append(temp)
        for j in range(n):
            C[i].append(0)

    for i in range(m):
        for j in range(n):
            for k in range(p):
                C[i][j] += amatrix[i][k] * another[k][j]

    return C


## pointwise multiplication

def pw_multiplication(amatrix, another):
    nrow = len(amatrix)
    ncol = len(amatrix[0])
    C = amatrix.copy()
    for i in range(nrow):
        for j in range(ncol):
            C[i][j] = amatrix[i][j] * another[i][j]

    return C


C = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]


def pw_division(amatrix, another):
    nrow = len(amatrix)
    ncol = len(amatrix[0])
    C = amatrix.copy()

    for i in range(nrow):
        for j in range(ncol):
            C[i][j] = amatrix[i][j] / another[i][j]


    return C


print(C)

## vector operations

def vector_scal_addition(scalar, avector) : return  [scalar * i for i in avector]

# print(x)

x = [1, 2, 3, 4, 5, 6]
y = [-1, 2, 6, 200000, 4, 5]

nelement = len(x)

def vector_addition(avector, another) : nelement=len(avector) ; return  [avector[i] + another[i] for i in range(nelement)]


# print(z)


## inner product
z = 0

def vector_inner_product(avector,another):
    z = 0
    nelement=len(avector)
    for i in range(nelement):
        z += avector[i] * another[i]

    return z

## saxpy

def saxpy(scalar,x,y):
    nelement=len(x)
    for i in range(nelement):
        y[i] = scalar * x[i]

print(y)

## matrix-vector multiplication and the gapxy

A = [[2, 333333, 44273], [23837364, 8373645, 202222]]

x = [1203023, 22323232, 2323232];
y = [12323, 2232323]

nrow = len(A)
ncol = len(A[0])

for i in range(nrow):
    for j in range(ncol):
        y[i] = y[i] + A[i][j] * x[j]

print(y)

## partition matrix


## outer product

A = [[2, 333333, 44273], [23837364, 8373645, 202222]]

x = [10234234, 23423423423];
y = [12929393, 12123, 3423423]

m = len(x)
n = len(y)

for i in range(m):
    for j in range(n):
        A[i][j] = A[i][j] + x[i] * y[j]

print(A)


## data structures
## band storage


class DOK_matrix:
    def __init__(self):
        self.dictionary={}


    def __get__(self, row,col):
        return self.dictionary.get([row,col])

    def __setitem__(self, row, col, value):
        self[[row, col]]=value


    def __str__(self):
        return str(self.dictionary)

    def toSparse(self, sparsematrix):
        for i in range(4):
            for j in range(3):
                if sparsematrix[i][j] != 0:
                    self.dictionary[i, j] = sparsematrix[i][j]

    def transpose(self):
        transpose={}
        for k in self.dictionary:
            reversed=self.reverse(k)
            transpose[reversed]=self.dictionary[k]

        return transpose

    def reverse(self, tuple):
        new_tup=tuple[::-1]
        return new_tup

    def scalar_addition(self,scalar):
        C={}
        for key in self.dictionary:
            C[key]=self.dictionary[key] * scalar

        return C

    # def gauss(A, b, x, n):
    #
    #     L = np.tril(A)
    #     U = A - L
    #     for i in range(n):
    #         x = np.dot(np.linalg.inv(L), b - np.dot(U, x))
    #         print(x)
    #     return x
    #
    # A = np.array([[4.0, -2.0, 1.0], [1.0, -3.0, 2.0], [-1.0, 2.0, 6.0]])
    # b = [1.0, 2.0, 3.0]
    # x = [1, 1, 1]
    # n = 20
    #
    # print(gauss(A, b, x, n))
    # end=time.time()
    # total=end-start

    ## region: using linked list for sparse matrix : https://www.geeksforgeeks.org/sparse-matrix-representation/

    class compactMatrixNode:
        def __init__(self):
            self.data = None
            self.row = None
            self.column = None
            self.next = None

        def getData(self):
            return self.data

        def getRow(self):
            return self.row

        def getColumn(self):
            return self.column

        def getNext(self):
            return self.next

        def setData(self, newdata):
            self.data = newdata

        def setRow(self, rownum):
            self.row = rownum

        def setColumn(self, columnnum):
            self.column = columnnum

        def setNext(self, newnext):
            self.next = newnext

        def __repr__(self):
            return f'{self.data},{self.row},{self.column},{self.next}'

    class compactMatrixLinkedList:
        def __init__(self):
            self.head = None

        def add(self, item, row, column):
            if self.head is None:
                n = compactMatrixNode()
                n.setData(item)
                n.setRow(row)
                n.setColumn(column)
                self.head = n
            else:
                self._add(item, row, column)

        def _add(self, item, row, column):
            node = compactMatrixNode()
            node.setData(item)
            node.setNext(self.head)
            node.setRow(row)
            node.setColumn(column)
            self.head = node

        def __repr__(self):
            return f'{self.head}'

    def convertSparsetoCompact(nested_list):
        compactMatrix = compactMatrixLinkedList()
        for row in range(len(nested_list[0:])):
            for column in range(len(nested_list[row:][0])):
                if nested_list[row][column] != 0:
                    print('Storing {} in row {} and column {}'.format(nested_list[row][column], row, column))
                    compactMatrix.add(nested_list[row][column], row, column)

        return compactMatrix
