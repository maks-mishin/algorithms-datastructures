def MadMax(tele_length: int, tele: list) -> list:
    max_elem = tele.pop(tele.index(max(tele)))
    tele.sort()

    start_pulse = tele[: tele_length // 2]
    start_pulse.append(max_elem)

    right_part = sorted(tele[tele_length // 2:], reverse=True)
    start_pulse.extend(right_part)
    return start_pulse
