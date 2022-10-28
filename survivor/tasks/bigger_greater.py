def swap_symbols(invocation: list, idx1: int, idx2: int) -> None:
    invocation[idx1], invocation[idx2] = invocation[idx2], invocation[idx1]


def is_impossible_magic(in_string: str) -> bool:
    """Return True if there are identical characters in the in_string"""
    return len(set(in_string)) == 1


def BiggerGreater(input_string: str) -> str:
    """Return invocation which is make from input_string"""
    if is_impossible_magic(input_string):
        return ''

    invocations = set()
    invocation = list(input_string)
    for i, ch1 in enumerate(input_string):
        for j, ch2 in enumerate(input_string):
            swap_symbols(invocation, j, i)
            invocations.add(''.join(invocation))
    
    filtered_invocations = list(
        filter(lambda x: x > input_string, invocations)
    )
    if not filtered_invocations:
        return ''
    return sorted(filtered_invocations)[0]
  
