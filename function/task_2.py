"""
    Viết hàm nhận 3 số đầu vào, và trả về số lớn nhất trong 3 số
    (Không dùng hàm max())
"""

numbers = [4, 5, 10, 9]
def max_number(number):
    max_value = float('-inf')
    for i in number:
        if i > max_value:
            max_value = i
    return max_value

print(max_number(numbers))