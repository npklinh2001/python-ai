# Bài 1
"""
    Yêu cầu người dùng nhập vào 1 số tự nhiên
    1. Kiểm tra xem đó có phải là số nguyên tố hay không
    2. In ra màn hình tất cả các số nguyên tố nhỏ hơn hoặc bằng n
"""


n = int(input("Enter a number: "))

def check_a_number_is_prime(n):
    if n < 2: 
        print('Không phải số nguyên tố')
    elif (n == 2) or (n == 3): 
        print('Số nguyên tố')
    else:
        a = int(n ** 0.5 + 1)
        is_prime = True
        for i in range(3, a + 1, 2):
            if n % i == 0: 
                is_prime = False
                print('Không phải số nguyên tố')
            
        if is_prime:
            print('Số nguyên tố')

check_a_number_is_prime(n)