def Keymaker(k: int) -> str:
    doors = []
    count = 1
    for step in range(1, k + 1):
        if step == count ** 2:
            doors.append('1')
            count += 1
            continue
        doors.append('0')
    print(''.join(doors))
    return ''.join(doors)


Keymaker(19)