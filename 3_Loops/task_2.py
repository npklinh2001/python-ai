# Bài 2:
"""
    Yêu cầu người dùng nhập vào 1 số tự nhiên n khác 0
    Tính n! theo 2 cách:
    - Sử dụng vòng lặp for
    - Sử dụng vòng lặp while
"""
n = int(input("Enter a number: "))

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(f'Giai thừa của {n} là: ', factorial(n))