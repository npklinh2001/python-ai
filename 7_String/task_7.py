"""
    Viết 1 hàm nhận tham số đầu vào là 1 chuỗi ký tự bất kỳ,
    trả về số lần 1 ký tự lặp lại liên tiếp cho đến khi ký tự
    đó thay đổi
    Ví dụ, với input đầu vào là chuỗi "aabbbaccba"
    Output là [2, 3, 1, 2, 1, 1]
"""


def get_frequences(string):
    result = []
    count_duplicate = 1
    for i in range(1, len(string)):
        if string[i - 1] == string[i]:
            count_duplicate += 1
        else:
            result.append(count_duplicate)
            count_duplicate = 1
    result.append(count_duplicate)
    return result

text = "aabbbaccba"
print(get_frequences(text))