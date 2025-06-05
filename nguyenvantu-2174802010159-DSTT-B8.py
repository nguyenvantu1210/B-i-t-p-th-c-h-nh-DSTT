#Bài tập 1 tính các vector
import numpy as np
u = np.array([2,-1,5,0])
v = np.array([4,3,1,-11])
w = np.array([-6,2,0,3])
x = 2*u-(v+3*w)
print('vector x= 2-( +3 ): ', x)
x1   =0.5*(2*u-v-3*w)
print('vector3(x +w )=2u −v +x :',x1)

#Bài Tập 2 tìm a,b,c
from numpy import linalg
A = np.matrix([[0, -1, 3],[1, 1, 1],[4, 2, 2]]) 
B = np.array([-1, -2, -2]) 
X = np.linalg.solve(A, B)
print('x = au + bv + cw : ',X)

#Bài Tập 3 chứng minh ma trận không khả nghịch ko phải là không hian con của không gian ma trận M2x2
A = np.matrix([[1,0],[0,0]]) 
B = np.matrix([[0,0],[0,1]]) 
from numpy import linalg as LA
a = LA.det(A)# numpy.linalg.LinAlgError: Singular matrix
b = LA.det(B)# ở đây cũng vậy
c = LA.det(A + B)
print('không gian con của A : ',c)
print('không gian con của B: ',a)
print('không gian con của A + B: ',b)


#Bài tập 4
import sympy as sp 
x, y = sp.symbols('x y')
A = sp.Matrix([[x, y],[y, x]])
x1, y1 = sp.symbols('x1 y1') # khai báo 2 biến x và y  
          # lưu ý: kiểu ma trận của sympy là ‘Matrix’ (viết hoa) 
A1 = sp.Matrix([[x1, y1],[y1, x1]]) 
x2, y2 = sp.symbols('x2 y2') 
A2 = sp.Matrix([[x2, y2],[y2, x2]])
print(A1.T) 
print(A1+A2.T)
print(((A1+A2).T).equals(A1+A2))
c= sp.symbols('c')
print(c*A)
print(((c*A).T).equals(c*A))

