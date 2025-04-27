# Viết 1 hàm nhận 2 tham số đầu vào:
#  1. Chuỗi kí tự bất kì, 1 sô tự nhiên k bất kỳ
# Loại bỏ phần tử thứ k khỏi chuỗi và trả về chuỗi kết quả

string = "Hello my name is KL"
k = 6
results = ""
for i in range(len(string)):
    if i != 6:
        results += string[i]

print(results)

k = 6
print(string.replace(string[k], ""))

print(string[:k] + string[k+1:])
