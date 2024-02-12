def rotate(sub_list: list) -> list:
    for _ in range(3):
        sub_list = [sub_list[1], sub_list[2], sub_list[0]]
        if sub_list == sorted(sub_list):
            break
    return sub_list


def MisterRobot(n: int, data: list) -> bool:
    if data == sorted(data):
        return True

    for _ in range(n):
        for i in range(n - 2):
            if data[i:i + 3] == sorted(data[i:i + 3]):
                continue
            data[i:i + 3] = rotate(data[i:i + 3])
        if data == sorted(data):
            return True
    return False
