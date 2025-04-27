"""
    Viết 1 hàm nhận 2 tham số đầu vào:
    1. 1 chuỗi ký tự bất kỳ
    2. 1 số tự nhiên k bất kỳ
    Loại bỏ phần tử thứ k khỏi chuỗi và trả về chuỗi kết quả
"""
string = "Today is a beautiful day!"
k = 6
def remove_postion_k(string, k):
    new_string = ''
    for i in range(len(string)):
        if i != (k - 1):
            new_string += string[i]
    return new_string

print(remove_postion_k(string, k))