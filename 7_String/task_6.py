"""
    Viết 1 hàm nhận tham số đầu vào là 1 chuỗi ký tự bất kỳ,
    trả về ký tự xuất hiện nhiều nhất trong chuỗi cùng với số
    lần ký t đó xuất hiện(không tính ký tự khoảng trắng,
    không phân biệt chữ biết hoa chữ viết thường)
"""


def get_most_frequent_char(string):
    dist_test = {}
    clean_text = string.lower().replace(" ", "")
    for i in clean_text:
        if i in dist_test:
            dist_test[i] += 1
        else:
            dist_test[i] = 1
    max_count_value = float("-inf")
    max_key = None
    for key, value in dist_test.items():
        if value > max_count_value:
            max_count_value = value
            max_key = key
    return max_key        
text = "Today is a beautiful day. Everything will be better"
print(get_most_frequent_char(text))
