def odometer( oksana ):
    elapsed_time = 0
    distance = 0
    current_velocity = 0

    for i in range(len(oksana)):
        if i % 2 == 0:
            current_velocity = oksana[i]
        else:
            delta_time = oksana[i] - elapsed_time
            elapsed_time = oksana[i]
            distance += current_velocity * delta_time
    return distance