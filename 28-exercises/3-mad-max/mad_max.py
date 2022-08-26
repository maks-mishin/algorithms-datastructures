def MadMax(N: int, Tele: list) -> list:
    max_elem = Tele.pop(Tele.index(max(Tele)))

    Tele.sort()
    left_part = Tele[: N // 2]
    rigth_part = sorted(Tele[N // 2:], reverse=True)

    start_pulse = left_part
    start_pulse.append(max_elem)
    start_pulse.extend(rigth_part)
    return start_pulse
