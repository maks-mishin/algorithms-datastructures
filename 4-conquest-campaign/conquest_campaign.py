def check_total_control(N: int, M: int, place_of_arms: list) -> bool:
    flag = True
    for i in range(N):
        for j in range(M):
            flag = flag and place_of_arms[i][j]
    return flag


def ConquestCampaign(rows: int, columns: int, L: int, battalion: list) -> int:
    place_of_arms = [[False for j in range(columns)] for i in range(rows)]
    places_already_control = set()

    for i in range(0, len(battalion) - 1, 2):
        place_of_arms[battalion[i] - 1][battalion[i + 1] - 1] = True
        places_already_control.add((battalion[i] - 1, battalion[i + 1] - 1))

    day_total_control = 1
    if check_total_control(rows, columns, place_of_arms):
        return day_total_control

    while True:
        day_total_control += 1

        temp_places_control = []
        for place in places_already_control:
            i, j = place[0], place[1]

            if place_of_arms[i][j]:
                for shift in [1, -1]:
                    if 0 <= i + shift <= rows - 1:
                        place_of_arms[i + shift][j] = True
                        temp_places_control.append(
                            (i + shift, j)
                        )
                    if 0 <= j + shift <= columns - 1:
                        place_of_arms[i][j + shift] = True
                        temp_places_control.append(
                            (i, j + shift)
                        )

        for place in temp_places_control:
            places_already_control.add(place)

        if check_total_control(rows, columns, place_of_arms):
            break
    return day_total_control
