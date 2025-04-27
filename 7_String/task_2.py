"""
    Yêu cầu người dùng nhập vào 2 chuỗi ký tự bất kỳ.
    Kiểm tra xem chúng có phải anagrams (phép đảo chữ)
    của nhau không?
    Định nghĩa anagram: 2 từ là anagram của nhau nếu ta có thể
    thu được từ này bằng cách đổi vị trí các ký tự của từ kia
    Các ví dụ:
    "New York Times" và "monkeys write"
    "coronavirus" và "carnivorous"
    "a gentleman" = "elegant man"
    "silent" = "listen"
"""

str1 = "coronavirus" 
str2 = "carnivorous"
def are_anagrams(str1, str2):
    clean_str1 = sorted(str1.lower().replace(" ", ""))
    clean_str2 = sorted(str2.lower().replace(" ", ""))
    if clean_str1 == clean_str2:
        return 'Đảo ngữ'
    else:
        return 'Không đảo ngữ'
    
print(are_anagrams(str1, str2))