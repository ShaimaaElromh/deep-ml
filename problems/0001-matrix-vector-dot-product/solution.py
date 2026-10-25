def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
    # Return a list where each element is the dot product of a row of 'a' with 'b'.
    # If the number of columns in 'a' does not match the length of 'b', return -1.
    multi_result = []
    if len(a[0]) != len(b):
        return -1

    result = 0
    for row in range(len(a)):
        for col in range(len(a[0])):
            result = result + a[row][col] * b[col]
        multi_result.append(result)
        result = 0
    return multi_result