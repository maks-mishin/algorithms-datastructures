def ConquestCampaign(N: int, M: int, L: int, battalion: list) -> int:
    place_of_arms = []

    for i in range(N):
        tmp_list = []
        for j in range(M):
            tmp_list.append(False)
        place_of_arms.append(tmp_list)

    places_already_control = set()

    for i in range(0, len(battalion) - 1, 2):
        y_coord = battalion[i] - 1
        x_coord = battalion[i + 1] - 1
        place_of_arms[y_coord][x_coord] = True

        places_already_control.add((y_coord, x_coord))

    day_total_control = 1

    neighbours = [1, -1]

    flag = True
    for i in range(N):
        for j in range(M):
            flag = flag and place_of_arms[i][j]
    if flag:
        return day_total_control

    while True:
        flag = True
        day_total_control += 1
        temp_places_already_control = []

        for place in places_already_control:
            i = place[0]
            j = place[1]

            if place_of_arms[i][j]:
                for neighbour in neighbours:
                    cell_vertical = i + neighbour
                    if 0 <= cell_vertical <= N - 1:
                        place_of_arms[cell_vertical][j] = True
                        temp_places_already_control.append(
                            (cell_vertical, j)
                        )

                    cell_horizontal = j + neighbour
                    if 0 <= cell_horizontal <= M - 1:
                        place_of_arms[i][cell_horizontal] = True
                        temp_places_already_control.append(
                            (i, cell_horizontal)
                        )

        for place in temp_places_already_control:
            places_already_control.add(place)

        for i in range(N):
            for j in range(M):
                flag = flag and place_of_arms[i][j]

        if flag:
            break
    return day_total_control
