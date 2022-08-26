// Source : https://leetcode.com/problems/maximum-subarray/
// Author : Maks Mishin
// Date   : 2/3/2022

#ifndef ALGORITHM_TASKS_MAX_SUB_ARRAY_H
#define ALGORITHM_TASKS_MAX_SUB_ARRAY_H

#include <vector>

class Solution {
public:
    int maxSubArray(std::vector<int>& nums) {
        int max_sum = nums[0],
                min_sum = 0,
                part_sum = 0,
                current_sum = 0;

        for (auto num : nums) {
            part_sum += num;
            current_sum = part_sum - min_sum;
            if (current_sum > max_sum) {
                max_sum = current_sum;
            }
            if (part_sum < min_sum) {
                min_sum = part_sum;
            }
        }
        return max_sum;
    }
};

#endif //ALGORITHM_TASKS_MAX_SUB_ARRAY_H
