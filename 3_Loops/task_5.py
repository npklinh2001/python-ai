# Bài 5: 
"""
    Đếm số chẵn, lẻ, âm, dương trong dãy sau
"""
numbers = [2, -3, 1, 5, -6, 3, 2, -4, 0, 5, 1, -3, -1, 2, 6, 3, -5, 0, 1, -4, 2, 3, -1, 0, 3, 2, -4, 2, 3]

def even_odd_negative_positive(numbers):
    even_count, odd_count, negative_count, positive_count = 0, 0, 0, 0
    for i in numbers:
        if i % 2 == 0:
            even_count += 1
        if i % 2 != 0:
            odd_count += 1
        if i < 0:
            negative_count += 1
        if i > 0:
            positive_count += 1     
    return even_count, odd_count, negative_count, positive_count

print(f'Tổng số chẵn: {even_odd_negative_positive(numbers)[0]} \n Tổng số lẻ: {even_odd_negative_positive(numbers)[1]}')
print(f'Tổng số âm: {even_odd_negative_positive(numbers)[2]} \n Tổng số dương: {even_odd_negative_positive(numbers)[3]}')
