# Kiểm tra chuỗi có phải anagrams (phép đảo ngữ)
# Ví dụ
# "New York Times" vs "monkeys write"


str1 = "New York Times"
str2 = "monkeys write"
def anagrams(str1, str2):
    str1_clean = sorted(str1.replace(" ", "").upper())
    str2_clean = sorted(str2.replace(" ", "").upper())

    if str1_clean == str2_clean:
        return 'Phép đảo ngữ'
    else:
        return 'Không phải đảo ngữ'
print(anagrams(str1, str2))