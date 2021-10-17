def saddle_points(matrix):
    if is_matrix_invalid(matrix):
        raise ValueError("The supplied matrix is invalid.")
    else:
        rows, cols = matrix, list(zip(*matrix))

        return [{"row": x + 1, "column": y + 1}
                for x, row in enumerate(matrix)
                for y, _ in enumerate(row) if max(rows[x]) == min(cols[y])]

def is_matrix_invalid(matrix):
    return any(len(row) != len(matrix[0]) for row in matrix)
