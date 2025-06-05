from sympy import Symbol, solve

# Bài tập 1 - Giải phương trình x + 3 - 5 = 0
x = Symbol('x')
bieuthuc = x + 3 - 5
nghiemx = solve(bieuthuc)
print(f"Phương trình x + 3 - 5 = 0, nghiệm x = {nghiemx}")

# Bài tập 1 - Phương trình bậc 2 x^2 + 3 - 5 = 0
bieuthuc = x**2 + 3 - 5
nghiemx = solve(bieuthuc)
print(f"Phương trình x^2 + 3 - 5 = 0, nghiệm x = {nghiemx}")

# Bài tập 2 - Phương trình bậc 2 x^2 + 9*x + 8 = 0
ptb2 = x**2 + 9*x + 8
nghiemx = solve(ptb2, dict=True)
print(f"Nghiệm phương trình x^2 + 9*x + 8 = 0: {nghiemx}")

# Phương trình có số ảo x^2 + x + 10 = 0
ptb2 = x**2 + x + 10
nghiemx = solve(ptb2, dict=True)
print(f"Nghiệm phương trình x^2 + x + 10 = 0: {nghiemx}")

# Bài tập 3 - Giải phương trình tổng quát với a, b, c
a = Symbol('a')
b = Symbol('b')
c = Symbol('c')
ptb2 = a*x**2 + b*x + c
nghiem = solve(ptb2, x, dict=True)
print(f"Nghiệm của phương trình tổng quát a*x^2 + b*x + c = 0: {nghiem}")


# Bài tập 4 - Hệ phương trình 2x + 3y = 12 và 3x - 2y = 5
y = Symbol('y')
pt1 = 2*x + 3*y - 12
pt2 = 3*x - 2*y - 5

nghiem = solve((pt1, pt2), dict=True)
print(f"Nghiệm của hệ phương trình: {nghiem}")

# Thử lại nghiệm trong các phương trình
nghiem = nghiem[0]
print(f"Thay nghiệm vào pt1: {pt1.subs({x: nghiem[x], y: nghiem[y]})}")
print(f"Thay nghiệm vào pt2: {pt2.subs({x: nghiem[x], y: nghiem[y]})}")


import numpy as np

# Ma trận M1
M1 = np.array([[9, 12], [23, 30]])
print(f"Ma trận M1: \n{M1}")

# Tích của ma trận M1 với vector u
u = np.array([2, 1])
tichM1u = M1.dot(u)
print(f"Tích của M1 và u: {tichM1u}")

# Tích ngược u.M1
tichuM1 = u.dot(M1)
print(f"Tích của u và M1: {tichuM1}")

# Dùng np.dot
print(f"Tích của M1 và u với np.dot: {np.dot(M1, u)}")
print(f"Tích của u và M1 với np.dot: {np.dot(u, M1)}")

# Ma trận với giá trị mặc định
mat1 = np.zeros([5,5])
print(f"mat1: \n{mat1}")

mat2 = np.ones([5,5])
print(f"mat2: \n{mat2}")

# Các phép toán với ma trận
mat3 = mat1 + 2 * mat2
print(f"mat3: \n{mat3}")

mat4 = mat3
mat3[3][2] = 10
print(f"mat3: \n{mat3}")
print(f"mat4: \n{mat4}")  # mat4 sẽ thay đổi khi mat3 thay đổi

mat5 = np.copy(mat3)
mat3[3][2] = 10
print(f"mat3: \n{mat3}")
print(f"mat4: \n{mat4}")
print(f"mat5: \n{mat5}")  # mat5 không thay đổi khi mat3 thay đổi

# Các ma trận khác
mat6 = np.empty([4, 5])
print(f"mat6: \n{mat6}")

mat7 = np.identity(4)
print(f"mat7: \n{mat7}")

# Ma trận ngẫu nhiên
mat8 = np.random.random([4, 5])
print(f"mat8: \n{mat8}")


# Lưới nguy cơ
A = np.array([[0, 1, 3, 1, 0], [0, 0, 1, 0, 1], [5, 2, 2, 0, 1], [0, 1, 2, 1, 2]])
B = np.array([[0, 1, 2, 2, 2], [2, 0, 2, 0, 1], [1, 4, 2, 4, 2], [1, 2, 2, 2, 1]])
C = np.array([[0, 1, 1, 3, 1], [1, 1, 1, 1, 3], [0, 1, 1, 3, 0], [3, 3, 0, 2, 1]])
D = np.array([[1, 0, 0, 0, 0], [0, 10, 0, 0, 0], [15, 0, 0, 0, 0], [5, 0, 0, 0, 5]])
E = np.array([[0, 5, 10, 15, 20], [0, 5, 10, 15, 20], [0, 5, 10, 15, 20], [0, 5, 10, 15, 20]])

# Tạo ma trận tổng mức nguy cơ cho các kịch bản đóng quân

def check_safe_area(*areas):
    return np.sum(areas, axis=0) <= 5

# Các kịch bản đóng quân
safe_area_1 = check_safe_area(A, E)  # chiến dịch ngắn hạn tránh lộ bí mật
print(f"An toàn trong chiến dịch ngắn hạn: \n{safe_area_1}")

safe_area_2 = check_safe_area(A, B, C, D)  # tập luyện thời bình
print(f"An toàn trong tập luyện thời bình: \n{safe_area_2}")

safe_area_3 = check_safe_area(A, D)  # mùa khô
print(f"An toàn trong mùa khô: \n{safe_area_3}")

safe_area_4 = check_safe_area(B, C, D)  # mùa mưa
print(f"An toàn trong mùa mưa: \n{safe_area_4}")

safe_area_5 = check_safe_area(A, B, C, D, E)  # 8 tháng
print(f"An toàn trong 8 tháng: \n{safe_area_5}")






