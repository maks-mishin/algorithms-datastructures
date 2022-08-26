// Source : https://leetcode.com/problems/contains-duplicate/
// Author : Maks Mishin
// Date   : 1/27/2022

#ifndef ALGORITHM_TASKS_CONTAINS_DUPLICATE_H
#define ALGORITHM_TASKS_CONTAINS_DUPLICATE_H

#include <iostream>
#include <vector>
#include <set>
#include <cassert>

using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        set<int> nums_set(nums.begin(), nums.end());
        return nums_set.size() == nums.size();
    }
};

void test_contains_duplicate() {
    Solution solution;

    vector<int> test_nums_1 = {1,2,3,1},
            test_nums_2 = {1,2,3,4},
            test_nums_3 = {1,1,1,3,3,4,3,2,4,2};
    assert(solution.containsDuplicate(test_nums_1));
    assert(!solution.containsDuplicate(test_nums_2));
    assert(solution.containsDuplicate(test_nums_3));

    std::cout << "Tests OK" << std::endl;
}

#endif //ALGORITHM_TASKS_CONTAINS_DUPLICATE_H
