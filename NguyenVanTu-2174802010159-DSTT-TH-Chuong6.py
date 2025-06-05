import numpy as np
import math

# Câu 1: Các cách tính chuẩn 2 của vector a
def norm_2_vector(a):
    mag1 = np.sqrt(a.dot(a))
    mag2 = np.sqrt(a @ a)
    mag3 = np.sqrt(np.inner(a, a))
    mag4 = math.sqrt(sum(i**2 for i in a))
    return mag1, mag2, mag3, mag4

# Câu 2a: Tính khoảng cách giữa hai vector u và v
def vector_distance(u, v):
    return np.linalg.norm(u - v)

# Câu 2b: Tính góc giữa hai vector u và v
def vector_angle(u, v):
    dot_product = np.dot(u, v)
    norm_u = np.linalg.norm(u)
    norm_v = np.linalg.norm(v)
    angle = math.acos(dot_product / (norm_u * norm_v))
    return math.degrees(angle)  # Chuyển từ radian sang độ

# Câu 2c: Tính phép chiếu trực giao của u lên v
def orthogonal_projection(u, v):
    projection = (np.dot(u, v) / np.dot(v, v)) * v
    return projection

# Chạy thử với các vector mẫu
if __name__ == "__main__":
    a = np.array([1, 2, 3])
    print("Chuẩn 2 của vector a:", norm_2_vector(a))

    u = np.array([3, 4, 5])
    v = np.array([1, 0, -1])
    
    print("Khoảng cách giữa u và v:", vector_distance(u, v))
    print("Góc giữa u và v:", vector_angle(u, v), "độ")
    print("Phép chiếu trực giao của u lên v:", orthogonal_projection(u, v))
