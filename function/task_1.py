"""
    Viết hàm tính và trả về khoảng cách giữa 2 điểm:
    - A(xa, ya, za)
    - B(xb, yb, zb)
    trong không gian 3 chiều
"""


def calculate_distance(a, b):
    sum = 0
    for i in range(0, 3):
        sum += (a[i] - b[i])**2
    return sum ** 0.5

a_coord = (1, 3, 6)
b_coord = (2, -1, -3)

print(calculate_distance(a_coord, b_coord))