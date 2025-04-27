# viết 1 hàm nhận 2 tham số đầu vào là 2 chuỗi ký tự bất kỳ,
# hàm trả về 2 danh sách bao gồm các ký tự xuất hiện ở cả 2 chuỗi

str1 = 'ssdakjfhkjsda'
str2 = 'sdafebcaws'

def intersection(str1, str2):
    intersection_set = set(str1) & set(str2)
    return intersection_set

print(intersection(str1, str2))


print(set(str1).intersection(set(str2)))