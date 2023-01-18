def is_template_line(line: str) -> bool:
    template = ''
    for ch in line[1:]:
        if ch == '*':
            template += ch
            break
        template += ch

    # construct the source line by template
    constructed_line = '*'
    while len(constructed_line) < len(line):
        constructed_line += template
    return constructed_line == line


def LineAnalysis(line: str) -> bool:
    # check the source line contains only '*' and '.'
    is_correct_line = all(map(lambda x: x == '*' or x == '.', line))
    if not is_correct_line:
        return False

    if not line[0] == line[-1] == '*':
        return False
    return is_template_line(line)
