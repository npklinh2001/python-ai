# hiệu số lớn nhất trừ số nhỏ nhất bằng số được cho
# ví dụ 297 = 431 - 134

x = 314
results = []

def max_diff(x):
    for i in str(x):
        results.append(int(i))

    sorted_asc = sorted(results, reverse=True)
    max = int(''.join(map(str, sorted_asc)))

    sorted_desc = sorted(results, reverse=False)
    min = int(''.join(map(str, sorted_desc)))
    return max - min

print(max_diff(x))

## Cách anh Việt

number = "314"
def max_diff(number):
    digits = sorted(number)
    min_number = int("".join(digits))
    max_number = int("".join(digits[::-1]))
    return max_number - min_number

print(max_diff(number))