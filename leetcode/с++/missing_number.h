// Source : https://leetcode.com/problems/missing-number/
// Date   : 1/30/2022

#ifndef ALGORITHM_TASKS_MISSING_NUMBER_H
#define ALGORITHM_TASKS_MISSING_NUMBER_H

#include <iostream>
#include <cassert>
#include <vector>
#include <set>
#include <algorithm>

class Solution {
public:
    int missingNumber(std::vector<int>& nums) {
        std::set<int> nums_set_one(nums.begin(), nums.end()), // set from source vector
        nums_set_two = {},
                result = {};

        // create full set from range 1 to n
        for (int i = 0; i <= nums.size(); ++i) {
            nums_set_two.insert(i);
        }

        // result - difference of two sets
        std::set_difference(nums_set_two.begin(), nums_set_two.end(),
                       nums_set_one.begin(), nums_set_one.end(), inserter(result, result.end()));
        return *result.begin();
    }
};

void testMissingNumber() {
    Solution solution;

    std::vector<int> test_case_1 = {3,0,1},
            test_case_2 = {0,1},
            test_case_3 = {9,6,4,2,3,5,7,0,1};
    assert(solution.missingNumber(test_case_1) == 2);
    assert(solution.missingNumber(test_case_2) == 2);
    assert(solution.missingNumber(test_case_3) == 8);
    std::cout << "Tests OK" << std::endl;
}

#endif //ALGORITHM_TASKS_MISSING_NUMBER_H
