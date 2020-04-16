import numpy as np

def isSingular(A):
    try:
        fix(A)
    except MatrixIsSingular:
        return True
    return False

class MatrixIsSingular(Exception): pass

def fixRow(A, i):
    adjust(A, i)
    for j in range(i+1, len(A)):
        if (A[i,i] == 0):
            A[i] = A[i] + A[j]
            adjust(A,i)
        else:
            break
    if (A[i,i] == 0):
        raise MatrixIsSingular()
    A[i] = A[i]/A[i,i]
    return A

def adjust(A, i):
    for j in range(0, i):
        A[i] = A[i] - A[i,j] * A[j]

def fix(A):
    B = np.array(A, dtype=np.float_)
    for i in range(0,len(A)):
        fixRow(B, i)
    return B;

A = np.array([
        [0, 7, -5, 3],
        [2, 8, 0, 4],
        [3, 12, 0, 5],
        [1, 3, 1, 3]
    ], dtype=np.float_)
print(fix(A))