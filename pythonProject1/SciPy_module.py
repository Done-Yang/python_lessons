"""
from scipy import constants

# constants
print(constants.year)
print(constants.liter)
# optimizer
from scipy.optimize import root
from math import cos

def eqn(x):
    return x + cos(x)

myroot = root(eqn, 0)

print(myroot.x)
"""
# solve equation
"""
from scipy.optimize import minimize

def eqn(x):
    return x**2 + x + 2

mymin = minimize(eqn, 0, method='BFGS')

print(mymin)
"""

# compressed the sparse row (csr)
"""
import numpy as np
from scipy.sparse import csr_matrix

arr = np.array([0, 0, 0, 0, 0, 1, 1, 0, 2])

print(csr_matrix(arr))
"""

# Sparse matrix method

import numpy as np
from scipy.sparse import csr_matrix

arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0 , 2]])

print(arr)
print('viewing data (not the zero items)')
print(csr_matrix(arr).data)
# counting nonzero
print('counting non-zero: ', csr_matrix(arr).count_nonzero())

# removing zero-entries (eliminate_zero)
mat = csr_matrix(arr)
mat.eliminate_zeros()
print('eliminate_zeros')
print(mat)
# eliminating duplicates entries
print('eliminating duplicates entries')
mat.sum_duplicates()
print(mat)
# converting csr to csc
print('csr to csc')
newarr = csr_matrix(arr).tocsc()

print(newarr)

