def TankRush(rows1: int, cols1: int, S1: str,
             rows2: int, cols2: int, S2: str) -> bool:
    if rows2 > rows1 or cols2 > cols1:
        return False
    if rows2 * cols2 == 0:
        return True

    overall_map, searched_map = S1.split(), S2.split()
    start_row = 0
    for i in range(rows1 - rows2 + 1):
        is_included = True
        for j in range(rows2):
            is_included = is_included and searched_map[j] in overall_map[i + j]
        if is_included:
            start_row = i
            break

    index_tank = overall_map[start_row].find(searched_map[0])
    for i in range(start_row, rows1 - rows2 + 1):
        for j in range(1, rows2):
            matching_index = (
                index_tank == overall_map[i + j].find(searched_map[j])
            )
            is_included = is_included and matching_index
    return is_included
