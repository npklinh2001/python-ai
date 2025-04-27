"""
    Viết 1 hàm kiểm tra xem 1 mảng 2 chiều (nested list) có phải là
    magic square (ma phương) hay không?
    Hàm nhận tham số đầu vào là 1 nested list, và trả về
    True nếu đó là ma phương, hoặc False nếu không phải

    Định nghĩa:
    một ma trận kì ảo bậc n (còn gọi là ma phương)
    là một cách sắp xếp n² số, là các số nguyên phân biệt,
    trong một bảng vuông sao cho tổng n số trên mỗi hàng, cột,
    và đường chéo đều bằng nhau.
"""

def is_magic_square(matrix):
    n = len(matrix)
    target_sum = sum(matrix[0])
    set_matrix = set()
    for row in matrix:
        for value in row:
            set_matrix.add(value)
    if len(set_matrix) == n**2:
        for i in range(n):
            if target_sum != sum(matrix[i]):
                return False
        for col in range(n):
            if sum(matrix[row][col] for row in range(n)) != target_sum:
                return False
        # Kiểm tra tổng 2 đường chéo
        if sum(matrix[i][i] for i in range(n)) != target_sum:
            return False
        if sum(matrix[i][n - i - 1] for i in range(n)) != target_sum:
            return False
    else:
        False

    return True

matrix1 = [
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8]
]
print(is_magic_square(matrix1))     # True
matrix2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(is_magic_square(matrix2))     # False
matrix3 = [
    [4, 9, 2],
    [3, 5, 7],
    [8, 1, 6]
]
print(is_magic_square(matrix3))     # True
