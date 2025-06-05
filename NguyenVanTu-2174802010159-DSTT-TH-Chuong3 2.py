#khoi tao MT:
# 1. Khai bao them thu vien scipylinalg va mot so cac vector khoi tao:
from scipy import linalg
import numpy as np
a = np.array([1,2,3])
b = np.array([(1+9j, 2j, 3j), (4j, 5j, 6j)]) # số phức
c = np.array([[ (0.5, 1.5, 10), (3,2,1) ] , [(6,5,4), (7,8,9)]]) # ma trận số thực 
## 2. Cac kieu khai bao va khoi tao MT:
A = np.matrix(np.random.random( (2,2) ) )
B = np.asmatrix(b)# Chuyển b thành dạng ma trận
C = np.matrix(np.random.random( (10,5) ) )
D = np.matrix([ [4, 3], [2, 6] ])
F = np.eye(3, k=1)# tạo ma trận đường chéo. 3 là ma trận 3x3, k=1 là đường chéo nằm phía trên đường chéo chính (k = 0). 
### 3. VD lien qua den 1 so cau lenh:
F = np.eye(3, k=0)
F = np.eye(3, k=-1) 
#### 4. Cac phep xu ly don gian.
# xem hang MT
np.linalg.matrix_rank(C)
print('hang MT C: ',np.linalg.matrix_rank(C))
# tinh MT nghich dao 
print('ma tran nghich dao A.I :',A.I)
linalg.inv(A)# đây là lệnh của gói scipy, nên có thể sử dụng scipy.linalg.inv(A) 
# dinh thuc MT
linalg.det(A)
print('dinh thuc MT A:',A) 
# chuyen doi MT
print('chuyển vị (dòng  cột): ',A.T) #chuyển vị (dòng  cột) 
print('chuyển vị liên hợp : ',A.H) # chuyển vị liên hợp
##### 5. Giai cac loai pghuong trinh tuyn tinh
linalg.solve(A, b)
print('PT tuyen tinh A ,b: ', linalg.solve(A, b)) 
E = np.matrix(a).T
print('PT tuyen tinh E: ', E)
linalg.lstsq(F, E)
print('PT tuyen tinh F, E: ',linalg.lstsq(F, E)) 
np.add(A, D)
print('Cong mT A + D: ', A + D)
np.subtract(A, D)
print('tu mT A - D: ', A - D)
np.divide(A, D) 
print('Chia mT A / D : ', A / D)
print('Nhan mT A @ D : ', A @ D)
np.multiply(D, A)
print('Nhan mT D * A : ', D * A)
np.dot(A, D)
print('Nhan mT A . D : ', np.dot(A,D))
np.vdot(A, D)
print('Nhan mT A . D : ', np.vdot(A,D))
linalg.expm(A)
print('Hàm mũ của ma trận A:', linalg.expm(A))
linalg.logm(A) 
print('Logarithm của ma trận A:', linalg.logm(A))
print('ma tran A la: ', A)
print('ma tran B la: ',B)
print('ma tran C la: ',C)
print('ma tran D la: ',D)
print('ma tran F la: ',F)

##MT phan ky
S = np.array([ [0,1], [1,0]])
print('ma tran S la: ',S)
temp = S.dot(S)
print(temp)
k= 6 
for i in range(k-1):
 temp = temp.dot(S)
 print (temp)
 print('---') 

G = np.array([ [0,-1], [-1,0]])
print(G) 
k= 5
for i in range(k-1):
 temp = temp.dot(G)
 print (temp)
 print('---')

import numpy as np

# Định nghĩa ma trận C
C = np.array([[1, 0, 0], 
              [0, 0.5, 1], 
              [0, 0, 0.5]])

# In ma trận C
print("Ma trận C:")
print(C)

# Tính toán ma trận C lần thứ 2 (C.dot(C))
temp = C.dot(C)
print("\nMa trận sau khi nhân C với C lần 1:")
print(temp)

# Lặp lại phép nhân 1000 lần
k = 1000
for i in range(k - 1):
    temp = temp.dot(C)

print("\nMa trận sau khi nhân 1000 lần:")
print(temp)

# Thực hiện thêm một lần nhân 1000 lần nữa
for i in range(k - 1):
    temp = temp.dot(C)

print("\nMa trận sau khi nhân 1000 lần nữa:")
print(temp)

import numpy as np

# Khởi tạo ma trận M
M = np.array([[0.8, 0.3], 
              [0.2, 0.7]])

# Tính M^2 (tức là M nhân với M)
MM = M.dot(M)
print("M^2:")
print(MM)

# Tính M^3 (tức là M^2 nhân với M)
MM = M.dot(MM)
print("\nM^3:")
print(MM)

# Tính M^100 (lặp lại phép nhân 100 lần)
for i in range(100):
    MM = MM.dot(M)

print("\nM^100:")
print(MM)

# Thử với ma trận mới như yêu cầu
M_new = np.array([[0.5, 0.5], 
                  [0.5, 0.5]])

# Tính M_new^2
MM_new = M_new.dot(M_new)
print("\nM_new^2:")
print(MM_new)

# Tính M_new^3
MM_new = M_new.dot(MM_new)
print("\nM_new^3:")
print(MM_new)

# Tính M_new^100
for i in range(100):
    MM_new = MM_new.dot(M_new)

print("\nM_new^100:")
print(MM_new)


import numpy as np
from scipy import linalg

# Khởi tạo ma trận M
M = np.array([[0.8, 0.3], 
              [0.2, 0.7]])

# Phân rã LU của ma trận M
P, L, U = linalg.lu(M)

# In ra các ma trận P, L, U
print("Ma trận P:")
print(P)

print("\nMa trận L:")
print(L)

print("\nMa trận U:")
print(U)

# Kiểm tra xem phép nhân L * U có bằng ma trận M ban đầu hay không
result = L.dot(U)
print("\nKết quả của L.dot(U) có bằng M không:")
print(result)

# Kiểm tra xem L * U có bằng M hay không
if np.allclose(result, M):
    print("\nL.dot(U) bằng với ma trận M ban đầu!")
else:
    print("\nL.dot(U) không bằng ma trận M ban đầu!")

import numpy as np

# Khởi tạo ma trận A
A = np.array([[0, 1, 0, 1],
              [0, 0, 1, 0],
              [1, 0, 0, 1],
              [1, 1, 0, 0]])

# Khởi tạo sumA và tính A^2
sumA = A
temp = A.dot(A)

# Số lần lặp lại (k = 3)
k = 3
sumA = sumA + temp

# Lặp lại phép nhân ma trận A cho các bước còn lại
for i in range(1, k - 1):
    temp = temp.dot(A)
    sumA = sumA + temp

# In kết quả của phép nhân cuối cùng và tổng sumA
print("Kết quả của A^k:")
print(temp)

print("\nTổng sumA (tính các đường đi có độ dài từ 0 đến k):")
print(sumA)






















