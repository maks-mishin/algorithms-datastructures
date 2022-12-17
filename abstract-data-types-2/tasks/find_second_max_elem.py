def quicksort(nums):
    if len(nums) <= 1:
        return nums
    pivot = nums[len(nums) // 2]
    lower_pivot_elems = [n for n in nums if n < pivot]
    e_nums = [pivot] * nums.count(pivot)
    upper_pivot_elems = [n for n in nums if n > pivot]
    return quicksort(lower_pivot_elems) + e_nums + quicksort(upper_pivot_elems)


def find_second_max_elem(nums):
    sorted_nums = quicksort(nums)
    if len(sorted_nums) >= 2:
        return sorted_nums[-2]
    return None
