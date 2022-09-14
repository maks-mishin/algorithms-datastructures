def transform(nums: list, count_nums: int) -> list:
    result_list = []
    for i in range(count_nums):
        result_list.extend(
            [max(nums[j:i + j + 1]) for j in range(count_nums - i)]    
        )
    return result_list


def TransformTransform(nums: list, count_nums: int) -> bool:
    key = sum(transform(transform(nums, count_nums), count_nums))
    return key % 2 == 0
