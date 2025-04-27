# Trả lại sô lần liên tiếp cho đến khi bị đổi


text = "aabbbaccba"

def get_frequences(text):
    count_list = []
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i-1]:
            count +=1
        else:
            count_list.append(count)
            count = 1
    return count_list
print(get_frequences(text))