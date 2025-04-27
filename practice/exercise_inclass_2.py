# Tam giác pascal

n = 5

results = []


def pascals_triangle(n):
    for i in range(2, n + 2):
        element = [1] * i + [0] * (n - i + 1)
        results.append(element)
    length = len(results)
    for i in range(length):
        for j in range(length):
            if i != 0 and j != 0:
                results[i][j] = results[i - 1][j - 1] + results[i - 1][j]
    return results 

print(pascals_triangle(n))


# Cách anh Việt

def pascals_triangle(rows):
    triangle = []
    for i in range(rows):
        row = [1] * (i + 2)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        print(row)
        triangle.append(row)
    
pascals_triangle(5)