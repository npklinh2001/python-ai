"""
    Viết hàm nhận 1 tham số đầu vào là 1 số tự nhiên n
    In ra kết quả là tích các thừa số nguyên tố của số đó
    Ví dụ, với n = 100
    Kết quả in ra màn hình là:
        100 = 2 x 2 x 5 x 5
"""


# def get_string(n):
def is_prime(n): #-> returns True if n is prime, False otherwise
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

n = 1400
results = prime_sequence(n)

result_2 = []

def product_prime(n, results, result_2):
    if n == 1:
        return result_2
    for i in results:
        if n % i == 0:
            result_2.append(i)
            break

    n = n // i

    return product_prime(n, results, result_2)



print(product_prime(n, results, result_2))

   