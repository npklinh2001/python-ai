# Cho list, đếm số lần xuất hiện của mỗi số trong list 

numbers = [20, 10, -4, 5, 10, 36]

result = {}
for number in numbers:
    if number in result.keys():
        result[number] += 1
    else:
        result[number] = 1

print(result)