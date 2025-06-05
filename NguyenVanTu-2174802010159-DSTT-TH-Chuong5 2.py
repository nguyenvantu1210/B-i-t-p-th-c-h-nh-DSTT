import numpy as np
D = np.array([[1,2],[3,4]]) 
E = np.array([[1,2],[3,4]])
np.copyto(E, D) 
print(E)


from numpy import matlib
G = matlib.identity(5)
print(G)

H = matlib.randn(3,2)
print(H)

K = matlib.zeros([4,4])
print (K)

L = matlib.empty((3,3))
print(L)

F = matlib.ones((3,3))
print(F)

C = np.eye(3)
print(C)

T = np.tile(np.array([[1, 2], [3, 4]]), (2, 2))
print(T)

Y = np.random.rand(3, 3)
print(Y)

import numpy as np
c = [3, 7, 15, 1, 292, 1, 1, 1, 2, 1, 3, 1, 14, 2] 
M = np.matrix([[1,2],[3,4]]) 
for i in range(len(c)):
    ci = np.matrix([[1,1],[1,0]])
    ci[0, 0] = c[i]
    if (i==0):
        M = ci
    else:
        M = M.dot(ci) 

print(M)
print (M[0,0]/M[1,0])


import numpy as np

# Nhập ma trận X (5x2) và vector Y (5x1)
X = np.array([[1, 1], [1, 2], [1, 3], [1, 4], [1, 5]])
Y = np.array([1, 2, 4, 4, 6])

# Tính ma trận chuyển vị của X
XT = X.T

# Tính A1 = (X^T * X)^-1
A1 = np.linalg.inv(XT.dot(X))

# Tính A2 = X^T * Y
A2 = XT.dot(Y)

# Tính A = A1 * A2
A = A1.dot(A2)

# Hiển thị các hệ số của phương trình Y = A[0] + A[1] * X
print("Phương trình gần đúng Y = A[0] + A[1] * X la :", A[0] + A[1] * X)

# Tính giá trị Y tính theo phương trình
Y_tinh = A[0] + A[1] * X[:, 1]

# Tính sai số (sai số bình phương)
sai_so = np.sum((Y - Y_tinh) ** 2)

# In kết quả sai số
print("Sai số bình phương tổng là: ", sai_so)








