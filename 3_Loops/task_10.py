# Bài 10:

"""
    In ra các số có ít hơn 4 chữ số và chia hết cho cả 5 và 7
"""

def number_divisible_5_7(n):
    max_value = 10**n
    result = []
    for i in range(0, max_value, 35):
        if (i % 7 == 0) and (i % 5 == 0): 
            result.append(i)
            
    return result

print('Những số chia hết cho cả 5 và 7', number_divisible_5_7(4))