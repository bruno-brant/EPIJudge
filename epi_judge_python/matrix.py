def make_matrix(num_lines: int, num_columns: int, value=0):
    return [[value] * num_columns for _ in range(num_lines)]
