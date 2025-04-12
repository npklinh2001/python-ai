"""
    Viết 1 hàm nhận 2 tham số đầu vào là 2 ma trận cùng kích thước,
    kết quả trả về là ma trận tích của chúng
    Ví dụ:
    Input:
        mat1 = [
        [1, 2, 3],
        [4, 5, 6],
    ]
    mat2 = [
        [7, 8],
        [9, 10],
        [11, 12],
    ]
    Output:
        array = [
        [58,  64],
        [139, 154],
    ]

"""

A = [[1, 3], 
     [2, 5], 
     [4, 6]]
B = [[7, 6, 3], 
     [4, 1, 5]]

def product_2_matrix(A, B):
    row_A = len(A)
    col_A = len(A[0])
    row_B = len(B)
    col_B = len(B[0])
    if col_A != row_B:
        return 'Phép nhân không hợp lệ'
    else:
        C = [[0] * col_B for _ in range(row_A)]
        for i in range(row_A):
            for j in range(col_B):
                for p in range(col_A):
                    C[i][j] += A[i][p] * B[p][j]
        return C

print('Kết quả nhân 2 ma trận là: ', product_2_matrix(A, B))
