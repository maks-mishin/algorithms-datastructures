def odometer(oksana: list) -> int:
    """Return distance calculated without speedometer"""
    elapsed_time, distance, current_velocity = 0, 0, 0

    for i in range(0, len(oksana), 2):
        current_velocity = oksana[i]
        delta_time, elapsed_time = oksana[i + 1] - elapsed_time, oksana[i + 1]
        distance += current_velocity * delta_time
    return distance
