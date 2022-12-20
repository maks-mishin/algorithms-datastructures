def calc_first_second_largest(nums, index, list_largest):
    result_list = list_largest
    if index < 2:
        return list_largest

    if nums[index] >= list_largest[0]:
        result_list = (nums[index], list_largest[0])
    elif nums[index] >= list_largest[1] and nums[index] != list_largest[0]:
        result_list = (list_largest[0], nums[index])
    return calc_first_second_largest(nums, index - 1, result_list)


def find_second_largest_elem(nums):
    """Функция для нахождения второго максимального числа в списке"""

    init_list = (nums[0], nums[1]) if nums[0] > nums[1] else (nums[1], nums[0])
    two_largest_elems = calc_first_second_largest(nums, len(nums) - 1, init_list)
    return two_largest_elems[1]
