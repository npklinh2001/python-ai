# Bài 9:
"""
    Cho 1 mảng gồm các số tùy ý
    Kiểm tra xem mảng đó có phải mảng đơn điệu hay không.
    Định nghĩa mảng đơn điệu: mảng đơn điệu là mảng
    không tăng hoặc không giảm
"""
array = [1, 3, 3, 4, 6, 7, 7]

def is_monotonous_array(array):

    len_array = len(array)
    max_value = - 999999
    max_count = 0
    min_value = 99999
    min_count = 0

    for i in array:
        if i >= max_value:
            max_count += 1
        if i <= min_value:
            min_count += 1
    if (max_count == len_array) or (min_count == len_array):
        return False
    else:
        return True
    
if is_monotonous_array(array):
    print('Mảng đơn điệu')
else:
    print('Mảng không đơn điệu')
