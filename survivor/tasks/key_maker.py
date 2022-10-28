def toggle_door(door: str) -> str:
    return '1' if door == '0' else '0'


def Keymaker(k: int) -> str:
    doors = ['0' for _ in range(k)]

    for step in range(1, k + 1):
        for i in range(step - 1, k, step):
            doors[i] = toggle_door(doors[i])
    return ''.join(doors)


def keymaker_math(k: int) -> str:
    doors = []
    key_position = 1

    for step in range(1, k + 1):
        if step == key_position ** 2:
            doors.append('1')
            key_position += 1
            continue
        doors.append('0')
    return ''.join(doors)


def verify_keymaker(k: int) -> bool:
    return Keymaker(k) == keymaker_math(k)
