def transform(nums: list) -> list:
    count_nums = len(nums)
    result_list = []
    for i in range(count_nums):
        result_list.extend(
            [max(nums[j:i + j + 1]) for j in range(count_nums - i)]    
        )
    return result_list


def TransformTransform(nums: list, count_nums: int) -> bool:
    return sum(transform(transform(nums))) % 2 == 0
