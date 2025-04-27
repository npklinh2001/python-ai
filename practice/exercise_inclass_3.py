# Số liên tiếp từ 1 đến n:

def find_missing_values(array):
    n = len(array)
    for i in range(n - 1):
        if array[0] == 1:
            if array[i + 1] - array[i] != 1:
                array.insert(i + 1, array[i] + 1)
        else:
            array.insert(0, 1)
    return array
array = [2, 3, 4, 5, 6, 7, 8, 9]
print(find_missing_values(array))


# Cách anh Việt:

def find_missing_values(array):
    current_length = len(array)
    current_sum = sum(array)
    expected_length = current_length + 1 
    expected_sum = expected_length*(expected_length + 1) / 2
    return expected_sum - current_sum 

array = [1, 2, 3, 4, 5, 7, 8, 9]
print(find_missing_values(array))