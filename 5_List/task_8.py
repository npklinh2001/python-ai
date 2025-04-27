"""
    Viết 1 hàm nhận 2 tham số đầu vào:
    1. 1 list bao gồm các từ bất kì
    2. 1 số tự nhiên k
    In ra các từ trong list có độ dài lớn hơn k ký tự
"""


def list_greater_k(word_list, k):
    result = []
    for i in word_list:
        if k < len(i):
            result.append(i)
    return result

word_list = ["apple", "banana", "cherry", "date", "monkey", "blackpink"]
k = 5

print('Các danh sách lớn hơn k tự kí tự', list_greater_k(word_list, k))