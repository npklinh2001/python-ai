# Bài 3:
"""
    Yêu cầu người dùng nhập vào 1 số tự nhiên n khác 0
    In ra n số Fibonacci đầu tiên
    Định nghĩa dãy Fibonacci: Dãy Fibonacci bắt đầu với 2 số 1
    Các số sau được xác định bẳng tồng của 2 số ngay trước nó.
    1 vài số Fibonacci đầu tiên trong dãy: 1, 1, 2, 3, 5, 8
"""

n = int(input("Enter a number: "))

def fibonacci_sequence(n):
    a = 1
    b = 1
    next_number = 0
    result = [a, b]
    for i in range(1, n + 1):
        next_number = a + b
        a = b
        b = next_number
        result.append(b)
    return result

print(f'Chuỗi fibonacci của {n}', fibonacci_sequence(n))