def is_total_matching(tanks_map: list, place_map: list, i: int, j: int) -> bool:
    tanks_map_rows, tanks_map_cols = len(tanks_map), len(tanks_map[0])
    
    is_match_position = True
    for row in range(tanks_map_rows):
        is_match_position = (
            is_match_position and
            tanks_map[row] == place_map[i + row][j:tanks_map_cols + j]
        )
    return is_match_position


def TankRush(rows1: int, cols1: int, S1: str,
             rows2: int, cols2: int, S2: str) -> bool:
    if rows2 > rows1 or cols2 > cols1:
        return False
    if rows2 * cols2 == 0:
        return True

    place_map, tanks_map = S1.split(), S2.split()
    for i in range(rows1 - rows2 + 1):
        for j in range(cols1 - cols2 + 1):
            if (
                place_map[i][j] == tanks_map[0][0] and
                is_total_matching(tanks_map, place_map, i, j)
            ):
                return True
    return False
