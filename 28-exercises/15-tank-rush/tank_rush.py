def TankRush(rows1: int, cols1: int, S1: str, 
             rows2: int, cols2: int, S2: str) -> bool:
    if rows2 > rows1 or cols2 > cols1:
        return False

    overall_map, searched_map = S1.split(), S2.split()
    is_included = False

    for i in range(rows1 - rows2 + 1):
        is_included = True
        for j in range(rows2):
            is_included = is_included and searched_map[j] in overall_map[i + j]
        if is_included:
            break
    return is_included
