def check_total_control(place_of_arms: list) -> bool:
    """Returns True if all elements of the array are True"""
    return all(all(row) for row in place_of_arms)


def conquering_neighbor_cells(place_of_arms: list, row: int, col: int) -> set:
    """Returns the set of places captured for the current day"""
    result_set = set()
    rows, columns = len(place_of_arms), len(place_of_arms[0])

    for shift in [1, -1]:
        if 0 <= row + shift <= rows - 1:
            place_of_arms[row + shift][col] = True
            result_set.add(
                (row + shift, col)
            )
        if 0 <= col + shift <= columns - 1:
            place_of_arms[row][col + shift] = True
            result_set.add(
                (row, col + shift)
            )
    return result_set


def ConquestCampaign(rows: int, columns: int,
                     count_coords: int, battalion: list) -> int:
    """
    Returns the number of days for how many troops to
    completely capture the polygon
    """
    place_of_arms = [[False for _ in range(columns)] for __ in range(rows)]
    places_already_control = set()

    for i in range(0, len(battalion) - 1, 2):
        place_of_arms[battalion[i] - 1][battalion[i + 1] - 1] = True
        places_already_control.add((battalion[i] - 1, battalion[i + 1] - 1))

    day_total_control = 1
    if check_total_control(place_of_arms):
        return day_total_control

    while True:
        day_total_control += 1
        temp_places_control = set()
        for place in places_already_control:
            row, col = place[0], place[1]

            if place_of_arms[row][col]:
                temp_places_control = temp_places_control.union(
                    conquering_neighbor_cells(place_of_arms, row, col)
                )

        places_already_control = places_already_control.union(
            temp_places_control
        )
        if check_total_control(place_of_arms):
            break
    return day_total_control
