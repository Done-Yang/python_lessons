# Dimension in array 

"""
import numpy as np
# 3D
arr = np.array([[[1, 2, 3], [11, 22, 33]], [[1, 22, 333], [123, 132, 213]]])
print(arr)
print(arr.ndim)

"""

# Array data type(Integer, Float, String, Boolean, Complex, Object)
"""
# import numpy as np
a = np.array([1, 2, 3, 4, 5])
b = np.array([1, 2, 3, 4, 5], dtype='float')
print(a)
print(a.dtype)
print(b)
print(b.dtype)
A = np.array([[1, 2, 3, 4, 5], [1, 3, 2, 5, 6]], dtype='complex')
print(A)
print(A.dtype)
"""

# <<ARRAY 2D=Matrix>>

# array = matrix0
"""
import numpy as np
print(np.zeros((5, 5)))
"""

# matrix1
"""
import numpy as np
print(np.ones((3, 3), dtype='int'))
"""

# matrix full
"""
import numpy as np
print(np.full((3, 3), 5))
"""

# Array Empty = matrix empty
"""
import numpy as np
print(np.empty([2, 3]))
"""

# identity matrix 'ມາຕິດເອກະລັດ'
"""
import numpy as np
print(np.identity(3, dtype='int'))
print()
print(np.eye(2, 3))   # to define the size of identity matrix
print()
print(np.eye(3, 4, k=1))    # to move the identity number 'move down k=(-), move right k=(+)'
print()
print(np.eye(3, 4, k=-1))
"""

# linspace defining 1D
# "numpy.linspace(start, stop, number)"
"""
import numpy as np
print(np.linspace(1, 3))
print()
print(np.linspace(1, 5, 4))
print()
print(np.linspace(1, 3, endpoint=False))
"""

# Arange numpy.arange(start, stop, step, dtype)
"""
import numpy as np
print(np.arange(0, 11))
print()
print(np.arange(0, 11, 2))
print()
print(np.arange(11, 0, -1, dtype='complex'))
"""

# Array Random
"""
import numpy as np

print(np.random.random((3, 3)))
"""

# NumPy Attribute
"""
numpy.dtype 
numpy.itemsize 
numpy.ndim  
numpy.shape
numpy.size
"""

"""
import numpy as np
ar = np.array([[1, 22, 333], [1, 2, 3], [11, 22, 33]])
print(ar)
print(ar.dtype)     # ('what type:int, complex, float')
print(ar.itemsize)      # ('how many byte by cover from bit: 'size in type')
print(ar.ndim)      # ('what Dimension "D"')
print(ar.shape)     # ('the array shape: "how long are the array, hlw many floor of the matrix"')
print(ar.size)      # ('how many content in the array')
print(ar[2, 2])     # ('index index2 row and index2 col
"""

# slice array 2D
"""
import numpy as np

ar = np.array([[1, 2, 3], [11, 222, 3333], [123, 456, 789]])
print(ar[:, 1:2])
index = np.array([[0, 2], [2, 1]])
print()
print(ar[[0, 2], [2, 0]])
"""

# index operator
"""
operators in array:('use array call index in another array, math operators: +, -, *, /,...')
"""
"""
import numpy as np
import math as m

ar = np.array([1, 22, 333, 4444, 55555, 666666, 7777777])
index = np.array([0, 2, 4])
print(ar[index])
ar2 = np.array([1, -3, 2, -4, 3, -5, 4])

pluss = ar2[ar2<0]
print(pluss)
print(ar2*2)
print(max(ar2))
print(m.sqrt(ar2[2]))
print(sum(ar2))
print(ar2 + ar)
matrix1 = np.array([[1, 3, 4], [2, 1, 3], [4, 2, 1]])
matrix2 = np.array([[5, 3, 1], [2, 4, 1], [3, 2, 5]])
print(matrix1 * matrix2)
second_matrix1 = np.array([[3], [4]])
second_matrix2 = np.array([[2, 5]])
print(second_matrix1, second_matrix2)
print(second_matrix2 * second_matrix1)
"""

# reshape the shape of the array
"""
import numpy as np

ar = np.array([78, 86, 95, 84, 92, 99, 78, 71, 92])

print(ar)
print(ar.reshape(3, 3))     # reshape from 1D to 3row and 3col "Temporarily"
ar.resize((3, 3))    # resize from 1D to 3row and 3col "Permanent"
print(ar)
"""

# reshape to 1D (don't touch with firs info)
"""
import numpy as np
ar = np.array([[13, 24], [53, 42]])

print(ar)
rv = ar.flatten()   # the changing is not longer
rv[0] = 23
print(rv)
print(ar)

print()
print(ar)
rv2 = ar.ravel()    # Able to change the first info
rv2[0] = 33
print(rv2)
print(ar)
"""
"""
# chang row matrix to col
import numpy as np
ar = np.array([[1, 3, 2], [5, 4, 6], [4, 2, 3]])
print(ar)
print()
trp = ar.transpose()  # transpose() row to colum
print(trp)
"""

# Statistic Function
# 1D
"""
mport numpy as np
ar = np.array([10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
print('numpylist: ', ar)
print('sum', sum(ar))
print('min', min(ar))
print('max', max(ar))
print('mean', ar.mean())
print('argmax', ar.argmax())
print('argmin', ar.argmin())
"""

# 2D
"""
import numpy as np
ar = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print(ar)
print('min by axis=1 (look through gant X)', np.min(ar, axis=1))
print('max by axis=0 (look through gantY)', np.max(ar, axis=0))
print('max of all: ', np.max(ar))
print(ar.sum())
"""

# dot product
"""
import numpy as np
ar = np.array([[2, 3], [4, 1]])
ar2 = np.array([[4, 5], [2, 6]])
print(ar)
print()
print(ar2)
dot = ar.dot(ar2)   # Before dot(), the shape must be equal each other
print('after dot()')
print(dot)  # ຄູນມາຕິກ
"""

# concatenate
"""
import numpy as np
ar1 = np.array([[3, 4], [4, 1]])
ar2 = np.array([[6, 7], [9, 8]])
ar = np.concatenate((ar1, ar2), axis=0)     # concatenate two array together
print(ar)
ar11 = np.array([[3, 4], [4, 1], [3, 5]])
ar22 = np.append(ar11, [[10], [17], [8]], axis=1)   # append new info to the array by define the axis
print(ar22)
"""

# insert
# 1D
"""
import numpy as np
ar = np.array([12, 23, 23])
ar1 = np.array([23, 54, 43, 21])
ar = np.insert(ar, 1, ar1)
print(ar)
"""

# 2D
"""
import numpy as np
ar = np.array([[12, 23], [34, 45]])
ar = np.insert(ar, 2, 9, axis=0)
print(ar)
print()

ar = np.array([[12, 23], [43, 32], [11, 22]])
print(ar)
ar2 = np.insert(ar, 2, [10, 20, 30], axis=1)
print(ar2)
"""

# delete the info in array
# 1D and 2D
"""
import numpy as np
ar = np.array([12, 32, 43, 42, 43, 54])
print(np.delete(ar, 1))

# 2D
art = np.array([[12, 23, 34], [43, 32, 21], [11, 22, 33]])
print(art)
print()
print(np.delete(art, 1, axis=1))
"""

# split
"""
import numpy as np
ar = np.arange(0, 25)
print(np.split(ar, 5))  # split the array to five array
ar_resize = ar.reshape((5, 5))  # resize to 2D array
print(ar_resize) # show the result of resize
print(np.hsplit(ar_resize, 5))  # vertical index
print(np.vsplit(ar_resize, 5))  # horizontal index
"""

import numpy as np

arr = np.ceil([-3.1666, 3.4])

print(arr)


