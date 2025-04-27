"""
    Viết 1 hàm nhận 2 tham số đầu vào là 2 ma trận,
    kết quả trả về là ma trận tổng của chúng. Nếu phép
    cộng không thực hiện được thì trả về giá trị 0
    Ví dụ:
    Input:
        mat1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    mat2 = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1],
    ]
    Output:
        array = [
        [10, 10, 10],
        [10, 10, 10],
        [10, 10, 10],
    ]

"""
mat1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
mat2 = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]]

def sum_matrix(mat1, mat2):
    result = []
    for i in range(len(mat1)):
        mat_temp = []
        for j in range(len(mat2)):
            mat_temp.append(mat1[i][j] + mat2[i][j])
        result.append(mat_temp)
    return result

print('Tổng 2 ma trận', sum_matrix(mat1, mat2))