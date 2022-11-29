// Source : https://leetcode.com/problems/single-number-iii/
// Date   : 2/3/2022

#ifndef ALGORITHM_TASKS_SINGLE_NUMBER_III_H
#define ALGORITHM_TASKS_SINGLE_NUMBER_III_H

#include <vector>
#include <string>
#include <map>

class Solution {
public:
    std::vector<int> singleNumber(std::vector<int>& nums) {
        std::map<int, int> nums_count;
        std::vector<int> result;

        for (auto num : nums) {
            ++nums_count[num];
        }

        for (const auto& [num, count]: nums_count) {
            if (count == 1) {
                result.push_back(num);
            }
        }

        return result;
    }
};

#endif //ALGORITHM_TASKS_SINGLE_NUMBER_III_H
