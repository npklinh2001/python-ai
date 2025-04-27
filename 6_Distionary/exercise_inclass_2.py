# Viết chương trình kết hợp 2 dictionary vào làm 1.
# Nếu key xuất hiện ở cả 2 dictionary thì công 2 vào value tương ứng lại

dic1 = {'a': 100, 'b': 200, 'c': 300}
dic2 = {'a': 300, 'b': 200, 'd': 400}

all_keys = dic1.keys() | dic2.keys()
results = {}
for i in all_keys:
    results[i] =  dic1.get(i, 0) + dic2.get(i, 0)

print(results)