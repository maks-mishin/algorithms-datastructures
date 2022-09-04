def MadMax(tele_length: int, tele: list) -> list:
    max_elem = tele.pop(tele.index(max(tele)))

    tele.sort()
    left_part = tele[: tele_length // 2]
    right_part = sorted(tele[tele_length // 2:], reverse=True)

    start_pulse = left_part
    start_pulse.append(max_elem)
    start_pulse.extend(right_part)
    return start_pulse
