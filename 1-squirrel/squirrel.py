def squirrel(N: int) -> int:
    factorial = 1
    for i in range(N):
        factorial *= i + 1
    while factorial > 10:
        factorial = factorial // 10
    return factorial
