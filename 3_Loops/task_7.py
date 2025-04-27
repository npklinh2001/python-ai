# Bài 7:
"""
    Tìm số lớn nhất và nhỏ nhất trong dãy sau
"""
numbers = [2, -3, 1, 5, -6, 3, 2, -4, 0, 5, 1, -3, -1, 2, 6, 3, -5, 0, 1, -4, 2, 3, -1, 0, 3, 2, -4, 2, 3]

def find_max_min(numbers):
    max_value = -9999
    min_value = 9999

    for i in numbers:
        if i > max_value:
            max_value = i
        if i < min_value:
            min_value = i
    return max_value, min_value
print(f'Giá trị lớn nhất {find_max_min(numbers)[0]} và Giá trị nhỏ nhất {find_max_min(numbers)[1]}')
