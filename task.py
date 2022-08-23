def MadMax( N, Tele ):
    start_pulse = []
    index_max_elem = Tele.index(max(Tele))
    max_elem = Tele.pop(index_max_elem)

    Tele.sort()
    left_part = Tele[: N // 2]
    rigth_part = sorted(Tele[N // 2 :], reverse=True)

    start_pulse.extend(left_part)
    start_pulse.append(max_elem)
    start_pulse.extend(rigth_part)
    return start_pulse
