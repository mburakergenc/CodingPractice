def generate(n):
    # If n = 0 return an empty array
    if n == 0:
        return []
    # Create a triangle array (This is the main(outer) array)
    triangle = []
    # First row will ony have 1 in it.
    first_row = [1]
    # Append the first row into the triangle array
    triangle.append(first_row)
    # Create a loop starting from one up to n, since we already have the first row
    for i in range(1, n):
        # Get the previous row from the triangle array
        prev_row = triangle[i-1]
        # Create the current row
        cur_row = []
        # Add 1 at the beginning of the current row
        cur_row.append(1)
        # Loop through items in the previous row, add them up then append them into the current row
        for j in range(1, i):
            cur_row.append(prev_row[j-1] + prev_row[j])
        # Append 1 at the end of the current row
        cur_row.append(1)
        # Append current row to the triangle
        triangle.append(cur_row)
    return triangle

print(generate(5))