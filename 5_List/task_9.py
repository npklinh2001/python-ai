"""
    Viết hàm nhận 1 tham số đầu vào là 1 số tự nhiên n
    In ra kết quả là tích các thừa số nguyên tố của số đó
    Ví dụ, với n = 100
    Kết quả in ra màn hình là:
        100 = 2 x 2 x 5 x 5
"""

def is_prime(n):
    if n == 3 or n == 2: return True
    if n % 2 == 0 or n < 2: return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def prime_sequence(n):
    prime_less_than_number = []
    for i in range(2, n+1):
        if is_prime(i):
            prime_less_than_number.append(i)
    return prime_less_than_number

def product_prime(n, results, result_2):
    if n == 1:
        return result_2
    for i in results:
        if n % i == 0:
            result_2.append(i)
            break
    n = n // i
    return product_prime(n, results, result_2)


n = 19
results = prime_sequence(n)
result_2 = []
print(product_prime(n, results, result_2))



# Cách 2:

def get_string(n):
    i = 2
    list_numbers = []
    while n > 1:
        if n % i == 0:
            list_numbers.append(i)
            n = n // i
        else:
            i = i + 1
    return list_numbers

print(get_string(9))    