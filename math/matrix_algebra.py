# Matrix Algebra

import numpy as np

##### Define matrices, vectors, and constants
A = np.array([[1, 2, 3], [2, 7, 4]])
B = np.array([[1, -1], [0, 1]])
C = np.array([[5, -1], [9, 1], [6, 0]])
D = np.array([[3, -2, -1], [1, 2, 3]])
u = np.array([[6, 2, -3, 5]])
v = np.array([[3, 5, -1, 4]])
w = np.array([[1], [8], [0], [5]])
alpha = 6

##### 1. Matrix Dimensions
print('\n1. Matrix Dimensions')
print('======================')
print('\n1.1) A =\n', A, '=>', A.shape)
print('\n1.2) B =\n', B, '=>', B.shape)
print('\n1.3) C =\n', C, '=>', C.shape)
print('\n1.4) D =\n', D, '=>', D.shape)
print('\n1.5) u =\n', u, '=>', u.shape)
print('\n1.6) w =\n', w, '=>', w.shape)

##### 2. Vector Operations
print('\n2. Vector Operations')
print('======================')
print('\n2.1) u + v =\n', u + v)
print('\n2.2) u - v =\n', u - v)
print('\n2.3) alpha * u =\n', alpha * u)
print('\n2.4) u * v =\n', u * v)
print('\n2.5) ||u|| =\n', np.linalg.norm(u))

##### 3. Matrix Operations
print('\n3. Matrix Operations')
print('======================')
print('\n3.1) A + C =')
try: 
    print(A + C)
except ValueError as e:
    print('Not Defined:', e)

print('\n3.2) A - C^T\n', A - C.transpose())
print('\n3.3) C^T + 3 * D =\n', C.transpose() + 3 * D)
print('\n3.4) B * A =\n', np.dot(B, A))

print('\n3.5) B * A^T =')
try:
    print(np.dot(B, A.transpose()))
except ValueError as e:
    print('Not Defined:', e)

print('\n3.6) B * C =')
try:
    print(np.dot(B, C))
except ValueError as e:
    print('Not Defined:', e)

print('\n3.7) C * B =\n', np.dot(C, B))
print('\n3.8) B^4 => B * B * B * B =\n', np.dot(B, np.dot(B, np.dot(B, B))))
print('\n3.9) A * A^T', np.dot(A, A.transpose()))
print('\n3.10) D^T * D ', np.dot(D.transpose(), D))


