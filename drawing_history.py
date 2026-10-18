patterns = []
next_id = 1

def save_pattern(matrix,operation):
    global next_id

    pattern = {
        "id":next_id,
        "operation":operation,
        "matrix":[row[:] for row in matrix],
    }

    patterns.append(pattern)
    next_id += 1

    return pattern