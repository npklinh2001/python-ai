"""
    Cho 1 danh sách gồm các số
    Viết các chương trình để tìm ra:
    1. Số lớn nhất
    2. Số lớn thứ nhì
    3. k số lớn nhất

"""

numbers = [20, 10, -4, 5, 15, 36, -16, 36]
def max_second(numbers):
    max_value = float("-inf")
    second_value = float("-inf")
    count_max = 0
    for i in numbers:
        if i >= max_value:
            max_value = i
        if (i != max_value) and (i >= second_value):
            second_value = i
    for j in numbers:
        if j == max_value:
            count_max += 1
    return max_value, count_max, second_value

print(f'giá trị lớn nhất: {max_second(numbers)[0]} với số lần: {max_second(numbers)[1]} và giá trị lớn nhì: {max_second(numbers)[2]}')
