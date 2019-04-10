def generate(n):
    if n == 0:
        return []
    triangle = []
    first_row = [1]
    triangle.append(first_row)
    for i in range(1, n):
        prev_row = triangle[i-1]
        cur_row = []
        cur_row.append(1)
        for j in range(1, i):
            cur_row.append(prev_row[j-1] + prev_row[j])
        cur_row.append(1)
        triangle.append(cur_row)
    return triangle

print(generate(5))