"""
    A.
    Viết hàm is_member() nhận 2 tham số đầu vào:
    1. 1 giá trị (số, chuỗi ký tự, bool, ...)
    2. 1 List chứa các giá trị bất kì
    Hàm kiểm tra xem giá trị có xuất hiện trong List hay không
    (Không dùng toán tử in)

    B.
    Viết hàm overlapping() nhận 2 tham số đầu vào là 2 List
    Hàm trả về danh sách các phần tử nằm ở cả 2 List
    Gợi ý: Sử dụng hàm is_member()
"""

# Bài A

def is_member(value, list_of_values):
    if value in list_of_values:
        return "Giá trị có trong list"
    else:
        return "Giá trị không có trong list"


print(is_member("monday", ["rose", 5, True, "monday", "tuesday", -5.5]))
print(is_member("Monday", ["rose", 5, True, "monday", "tuesday", -5.5]))

# Bài B

def overlapping(list_1, list_2):
    results = []
    for i in list_1:
        for j in list_2:
            if i == j:
                results.append(i) 
    return results

list_1 = [0, 3, 45, 4, 9]
list_2 = [23, 45, 32, 235, 4]

print('Các giá trị giống nhau giữa 2 list là', overlapping(list_1, list_2))