import numpy as np
n =4 
X = np.array(range(1,n+1))
sigma = np.array([4,3,2,1])
def sgn_by_def(sigma):
    ket_qua = 1.0
    for i in range(len(X)-1):
        for j in range(i +1, len(X)):
            ket_qua = ket_qua* ((X[i] - X[j]) / sigma[i] -sigma[j])
            return int(ket_qua)

sigma = np.array([2,1,3,4])
print(sgn_by_def(sigma))

###

from itertools import permutations
n =3
X = []
for i in range(1, n+1):
    X.append(i)
    Sn=list(permutations(X))
    print(Sn)

 
###
import numpy as np
det =0
def phatsinh_dinhthuc(n):
    X = []
    for i in range(1, n+1):
        X.append(i)
    Sn=list(permutations(X))
    dinhthuc = ""
    for sn in Sn:
            sigma = np.array([1])
            sigma.resize([n])
            product = ""
            for i in range(1,n+1):
                sigma[sn.index(i)] = i
                product = product+ "a"+str(i)+str(sn.index(i)+1)
            dau = sgn_by_def(sigma)
            if (dau != 1):
                product = "-"+product
            else:
                product = "+"+product
                dinhthuc =dinhthuc+product
    return dinhthuc
print(phatsinh_dinhthuc(2))
print(phatsinh_dinhthuc(3))

def phatsinh_dinhthuc(A):
    X = []
    import math
    n = int(math.sqrt(A.size))
    for i in range(1, n+1):
        X.append(i)
    Sn=list(permutations(X))
    dinhthuc = 0
    for sn in Sn:
            sigma = np.array([1])
            sigma.resize([n])
            product = 1
            for i in range(1,n+1):
                sigma[sn.index(i)] = i
                product = product+ A[i-1][sn.index(i)]
                print(A[i-1][sn.index(i)])
            dau = sgn_by_def(sigma)
            if (dau != 1):
                product = product * (-1)
                dinhthuc =dinhthuc+product
    return dinhthuc
matran = np.array([[3,5,-8],[4,12,-1],[2,5,3]])
print(tinhtoan_dinhthuc(A))


##baitapchuong4
import numpy as np
from sympy import symbols, Matrix, Eq, solve

def ma_tran_he_so_kep(A):
    """Tính ma trận hệ số kép (cofactor matrix) của A."""
    n = A.shape[0]
    cofactor = np.zeros((n, n))
    
    for i in range(n):
        for j in range(n):
            minor = np.delete(np.delete(A, i, axis=0), j, axis=1)
            cofactor[i, j] = ((-1) ** (i + j)) * np.linalg.det(minor)
    
    return cofactor

def ma_tran_lien_hop(A):
    """Tính ma trận liên hợp (adjoint matrix) của A."""
    return ma_tran_he_so_kep(A).T

def tim_phuong_trinh_duong_tron(diem):
    """Tìm phương trình đường tròn đi qua ba điểm đã cho."""
    x1, y1 = diem[0]
    x2, y2 = diem[1]
    x3, y3 = diem[2]
    
    x, y = symbols('x y')
    A = Matrix([
        [x1**2 + y1**2, x1, y1, 1],
        [x2**2 + y2**2, x2, y2, 1],
        [x3**2 + y3**2, x3, y3, 1],
        [x**2 + y**2, x, y, 1]
    ])
    
    phuong_trinh = Eq(A.det(), 0)
    return phuong_trinh

# Ví dụ sử dụng
A = np.array([[2, -1, 0], [3, 4, 5], [1, 0, 6]])
print("Ma trận hệ số kép:")
print(ma_tran_he_so_kep(A))
print("Ma trận liên hợp:")
print(ma_tran_lien_hop(A))

# Ví dụ phương trình đường tròn
diem = [(1, 2), (3, 4), (5, 6)]
print("Phương trình đường tròn:")
print(tim_phuong_trinh_duong_tron(diem))
