"""
    Viết chương trình kết hợp 2 dictionary vào làm 1.
    Nếu key xuất hiện ở cả 2 dictionary thì cộng 2 value
    tương ứng lại
"""

dict1 = {'a': 100, 'b': 200, 'c': 300}
dict2 = {'a': 300, 'b': 200, 'd': 400}

def union_distionary(dict1, dict2):
    new_dist = {}
    all_keys = dict1.keys() | dict2.keys()

    for i in all_keys:
        new_dist[i] = dict1.get(i, 0) + dict2.get(i, 0)  

    return new_dist

print(union_distionary(dict1, dict2))