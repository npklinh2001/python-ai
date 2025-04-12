"""
    Viết 1 hàm nhận 2 tham số đầu vào:
    1. 1 list bao gồm các số bất kì
    2. 1 số tự nhiên k
    Trả về kết quả là 1 list, trong đó các phần tử bị dịch
    sang trái k đơn vị
    Ví dụ:
    Input:
        array = [1, 2, 3, 4, 5]
        k = 2
    Output:
        array = [3, 4, 5, 1, 2]
"""


def shift_array(array, k):
    array1 = array[k:]
    array2 = array[:k]
    new_array = array1 + array2
    return new_array

array = [1, 2, 3, 4, 5]
k = 2
print('Mảng mới là', shift_array(array, k))

def shift_array(array, k):
    length = len(array)
    result = [0] * length
    for i in range(length):
        result[i] = array[(i + k) % length]
    return result
array = [1, 2, 3, 4, 5]
k = 2
print('Mảng mới là', shift_array(array, k))