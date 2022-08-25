def SumOfThe(N: int, data: list) -> int:
    result = filter(lambda num: num == sum(data) - num, data)
    sum_remain_nums = list(result)[0]
    return sum_remain_nums
