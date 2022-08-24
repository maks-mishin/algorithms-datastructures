def PatternUnlock(N, hits):
    keyboard_coords = {
        6: (1, 1), 1: (1, 2), 9: (1, 3),
        5: (2, 1), 2: (2, 2), 8: (2, 3),
        4: (3, 1), 3: (3, 2), 7: (3, 3)
    }

    total_lenght_line = 0
    for i in range(N - 1):
        x_dist = abs(
            keyboard_coords[hits[i]][0] - keyboard_coords[hits[i + 1]][0]
        )
        y_dist = abs(
            keyboard_coords[hits[i]][1] - keyboard_coords[hits[i + 1]][1]
        )
        if x_dist == 1 and y_dist == 1:
            total_lenght_line += 2 ** (1/2)
        else:
            total_lenght_line += 1

    total_lenght_line = round(total_lenght_line, 5)
    result_str = str(total_lenght_line).replace('0', '').replace('.', '')
    return result_str
