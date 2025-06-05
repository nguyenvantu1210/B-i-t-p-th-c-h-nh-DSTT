def scale(a,v):
    return[a*vi for vi in v]
v = [3,5,7]
print(scale(10,v))

def sumvector(v,w):
    return[vi+wi for(vi,wi)in zip(v,w)]
v =[3,5,7]
w=[2,4,6]
print(sumvector(v, w))

def dotvector(v, w):
    return sum([vi*wi for (vi, wi) in zip(v, w)])
print(dotvector(v, w)) 

def lenvector(v):
 return dotvector(v,v)
print( lenvector(w) )

import numpy as np
from scipy import linalg,sparse
D = np.mat([ [3,4], [5,6] ])
print(D)

C = np.mat(np.random.random((5,7)))
print(C)

A = np.mat(np.random.random((2,2)))
print(A)

b = np.array([(1+5j, 2j, 3j),(4, 5,6)])
B = np.asmatrix(b)
print(b)
print(B)
print(A.T)
print(A.I)

linalg.inv(A)
M = np.array([[-1,3,2],[0,-2,1],[1,5,-2]])
M_upper = np.triu(M)
print(M_upper)

M = np.array([[-1,3,2],[0,-2,1],[1,5,-2]])
v_diag = np.diag(M)
print (v_diag) 
M_diag = np.diag(v_diag)
print (M_diag) 
