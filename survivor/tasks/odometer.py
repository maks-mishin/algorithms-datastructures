def odometer(oksana: list) -> int:
    """Return distance calculated without speedometer"""
    elapsed_time, distance, velocity = 0, 0, 0

    for i in range(0, len(oksana), 2):
        velocity = oksana[i]
        delta_time, elapsed_time = oksana[i + 1] - elapsed_time, oksana[i + 1]
        distance += velocity * delta_time
    return distance
