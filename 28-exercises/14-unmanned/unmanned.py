def is_red_light(total_time: int, traffic_light: list) -> tuple:
    red_time, green_time = traffic_light[1], traffic_light[2]
    traffic_light_time = red_time + green_time

    if total_time % traffic_light_time == 0:
        return (True, red_time)

    remain_time = total_time % traffic_light_time
    if remain_time >= red_time:
        return (False, 0)
    return (True, red_time - remain_time)


def Unmanned(road_length: int, N: int, track: list) -> int:
    total_time, distance = 0, 0

    for traffic_light in track:
        if traffic_light[0] > road_length:
            continue

        total_time += traffic_light[0] - distance
        distance = traffic_light[0]

        is_red, remain_time = is_red_light(total_time, traffic_light)
        if is_red:
            total_time += remain_time
    total_time += road_length - distance
    return total_time
