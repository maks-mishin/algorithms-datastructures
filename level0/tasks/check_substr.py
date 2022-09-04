def CheckSubstr(s1: str, s2: str) -> bool:
    for i in range(len(s1) - len(s2) + 1):
        is_substr = True
        for j in range(len(s2)):
            if s1[i + j] != s2[j]:
                is_substr = False
                break
        if is_substr:
            return True
    return False
