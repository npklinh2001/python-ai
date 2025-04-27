"""
    Viết 1 hàm nhận tham số đầu vào là 1 chuỗi ký tự bất kỳ,
    hãy loại bỏ toàn bộ các dấu câu cũng như ký tự đặc biệt
    khỏi chuỗi ký tự đó và trả về kết quả
"""
from string import punctuation


def remove_punctuations(input_string):
    for i in punctuation:
        input_string = input_string.replace(i, "")
    return input_string

input_string = """
    Maya Angelo said, "If you don't like something, change it. 
    If you can't change it, change your attitude."
"""

print(remove_punctuations(input_string))
