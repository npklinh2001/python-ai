# Bài 4: 
"""
    Yêu cầu người dùng nhập vào 1 số tự nhiên n khác 0
    In ra tất cả các số Armstrong nhỏ hơn hoặc bằng n
    Định nghĩa số Armstrong: 1 số n được gọi là số Armstrong nếu:
    Tổng các chữ số của số đó, với mỗi chữ số được lũy thừa với
    số mũ k bằng chính số đó, với k là số chữ số của n
    Ví dụ: 153 là số Armstrong vì:
    153 có 3 chữ số, và 153 = 1^3 + 5^3 + 3^3
"""
n = int(input("Enter a number: "))

def armstrong_number(n):
    total = 0
    for i in str(n):
        total += int(i) ** 3

    if n == total:
        print('Là số Armstrong')
    else:
        print('Không phải số Armstrong')

armstrong_number(n)