"""
    Viết 1 hàm nhận 2 tham số đầu vào là 2 chuỗi ký tự bất kỳ,
    hàm trả về 1 danh sách bao gồm các ký tự xuất hiện ở cả
    2 chuỗi

"""
str1 = 'coronavirus'
str2 = 'caronoy'

def common_chars(str1, str2):
    intersect_str = set(str1) & set(str2)
    return intersect_str

print(common_chars(str1, str2))

