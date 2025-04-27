"""
    Viết 1 hàm nhận tham số đầu vào là 1 chuỗi ký tự bất kỳ,
    đếm và trả về số lượng nguyên âm trong chuỗi đó
"""


def count_vowels(string):
    vowels = 'aeiou'
    clean_text = string.lower()
    list_vowels = []
    dist_vowels = {}
    for i in clean_text:
        if i in vowels:
            list_vowels.append(i)
    for i in list_vowels:
        if i in dist_vowels:
            dist_vowels[i] += 1
        else:
            dist_vowels[i] = 1
    return dist_vowels
text = "Today is a beautiful day"
print(count_vowels(text))