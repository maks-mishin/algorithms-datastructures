def CheckSubstring(s1: str, s2: str) -> bool:
    """Return True if s2 is a substring of s1"""
    len_s1, len_s2 = len(s1), len(s2)
    for i in range(len_s1 - len_s2 + 1):
        is_substring = True
        for j in range(len_s2):
            if s1[i + j] != s2[j]:
                is_substring = False
                break
        if is_substring:
            return True
    return False
