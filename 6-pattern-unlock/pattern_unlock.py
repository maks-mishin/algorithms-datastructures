def PatternUnlock(N, hits):
    keyboard = {
        6: (1, 1), 1: (1, 2), 9: (1, 3),
        5: (2, 1), 2: (2, 2), 8: (2, 3),
        4: (3, 1), 3: (3, 2), 7: (3, 3)
    }

    total_lenght_line = 0
    for i in range(N - 1):
        is_diag = True
        for j in [0, 1]:
            is_diag = is_diag and abs(keyboard[hits[i]][j] - keyboard[hits[i + 1]][j]) == 1

        next_dist = 2 ** (1/2) if is_diag else 1
        total_lenght_line += next_dist

    total_lenght_line = round(total_lenght_line, 5)
    result_str = str(total_lenght_line).replace('0', '').replace('.', '')
    return result_str
