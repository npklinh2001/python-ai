"""
    Cho list bao gồm các số bất kì
    Đếm xem số lần xuất hiện của mỗi số trong list đó
"""

numbers = [20, 10, -4, 5, 10, 36, -16, 3, 5, 10, 16, -5, 5]

def count_numbers(numbers):
    number_distionary = {}
    for number in numbers:
        if number in number_distionary:
            number_distionary[number] += 1
        else:
            number_distionary[number] = 1

    return number_distionary

print(count_numbers(numbers))


