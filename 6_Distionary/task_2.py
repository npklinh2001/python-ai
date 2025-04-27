"""
    Yêu cầu người dùng nhập vào 1 số tự nhiên n bất kì
    Tạo ra 1 dictionary với key lần lượt là các số từ
    0 đến n, và value là bình phương của key
"""

n = int(input("Enter a number: "))
def square_key(n):
    distionary_n = {}
    for i in range(n):
        distionary_n[i] = i**2

    return distionary_n

print(square_key(n))
