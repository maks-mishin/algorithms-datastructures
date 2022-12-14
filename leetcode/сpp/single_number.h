// Source : https://leetcode.com/problems/single-number/
// Date   : 1/30/2022

#ifndef ALGORITHM_TASKS_SINGLE_NUMBER_H
#define ALGORITHM_TASKS_SINGLE_NUMBER_H

#include <vector>
#include <map>

class Solution {
public:
    int singleNumber(std::vector<int>& nums) {
        std::map<int, int> nums_count;
        int result_num = 0;

        for (auto num : nums) {
            ++nums_count[num];
        }

        for (const auto& [num, count]: nums_count) {
            if (count == 1) {
                result_num = num;
                break;
            }
        }
        return result_num;
    }
};

#endif //ALGORITHM_TASKS_SINGLE_NUMBER_H
