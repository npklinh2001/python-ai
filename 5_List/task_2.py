"""
    Viết 1 hàm nhận 2 tham số đầu vào:
    1. 1 list bao gồm các số bất kì
    2. 1 số tự nhiên k
    tách hàm ban đầu thành 2 nửa, được phân cách bởi
    phần tử có chỉ số là k (phần tử này sẽ thuộc về
    nửa thứ 2) rồi sau đó nối chúng lại sao cho nửa
    thứ 2 đứng ở trước nửa thứ nhất.
    Ví dụ:
    Input:
        array = [1, 2, 3, 4, 5]
        k = 3
    Output:
        array = [4, 5, 1, 2, 3]
"""


def split_array(array, k):
    array1 = array[k+1:]
    array2 = array[:k+1]
    new_array = array1 + array2
    return new_array

array = [1, 2, 3, 4, 5]
k = 2
print('Mảng mới là', split_array(array, k))