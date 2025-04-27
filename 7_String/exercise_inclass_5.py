# Kí tự nào xuất hiện nhiều nhất


# def get_most_frequent_char()

text = "Today is a beautiful day. Everything will be better"


def get_most_frequent_char(text):
    text = text.upper().replace(" ", "")
    text_dict = {}
    for i in text:
        if i not in text_dict:
            text_dict[i] = 1
        else:
            text_dict[i] += 1

    max_char = None
    max_count = 0
    for char, count in text_dict.items():
        if count > max_count:
            max_count = count
            max_char = char
    return max_char, max_count


print(get_most_frequent_char(text))
print(get_most_frequent_char(text))
print(get_most_frequent_char(text))
print(get_most_frequent_char(text))

