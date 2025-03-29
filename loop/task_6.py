# Bài 6:
"""
    Yêu cầu người dùng nhập vào 1 số dạng nhị phân (e.g. 1001)
    In ra giá trị dạng thập phân tương ứng của số đó
"""
n = int(input("Enter a binary number: "))

def binary_to_number(n):
    total = 0 
    length = len(str(n)) - 1

    for i in str(n):
        total += 2 ** length * int(i)
        length -= 1
    return total

print(f'Số nhị phân {n} có dạng thập phân là {binary_to_number(n)}')
