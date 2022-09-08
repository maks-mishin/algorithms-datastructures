def swap_symbols(in_string: str, index1: int, index2: int) -> str:
    tmp_list = list(in_string)
    tmp_list[index1], tmp_list[index2] = tmp_list[index2], tmp_list[index1]
    return ''.join(tmp_list)


def check_boundary_cases(in_string: str) -> bool:
    impossible_magic = True
    for ch in in_string:
        impossible_magic = impossible_magic and ch == in_string[0]
    return impossible_magic


def BiggerGreater(in_string: str) -> str:
    if check_boundary_cases(in_string):
        return ''
    
    invocations = set()
    invocation = in_string
    for i, ch1 in enumerate(in_string):
        for j, ch2 in enumerate(in_string):
            invocation = swap_symbols(invocation, j, i)
            invocations.add(invocation)
    
    filtered_invocations = list(filter(lambda x: x > in_string, invocations))
    if not filtered_invocations:
        return ''
    return sorted(filtered_invocations)[0]
  
