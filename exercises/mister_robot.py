def rotate(sub_list: list) -> list:
    for i in range(3):
        sub_list = [sub_list[1], sub_list[2], sub_list[0]]
        if sub_list == sorted(sub_list):
            break
    return sub_list


def MisterRobot(n: int, data: list) -> bool:
    correct_data = sorted(data)
    if data == correct_data:
        return True

    for j in range(n):
        for i in range(n - 2):
            sub_list = data[i:i + 3]
            if sub_list == sorted(data[i:i + 3]):
                continue
            data[i:i + 3] = rotate(sub_list)
        if data == correct_data:
            return True
    return False
