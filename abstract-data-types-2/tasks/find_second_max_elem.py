import math
import sys


def calc_first_second_largest(nums, index, list_largest):
    if index < 2:
        return
    if nums[index] > list_largest[0]:
        list_largest[1] = list_largest[0]
        list_largest[0] = nums[index]
    elif nums[index] > list_largest[1] and nums[index] != list_largest[0]:
        list_largest[1] = nums[index]
    calc_first_second_largest(nums, index - 1, list_largest)


def find_second_largest_elem(nums):
    list_largest = [nums[0], nums[1]] if nums[0] > nums[1] else [nums[1], nums[0]]
    calc_first_second_largest(nums, len(nums) - 1, list_largest)
    return list_largest[1]
