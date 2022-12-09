// Source : https://leetcode.com/problems/binary-search/
// Date   : 1/26/2022

#ifndef ALGORITHM_TASKS_BINARY_SEARCH_H
#define ALGORITHM_TASKS_BINARY_SEARCH_H

#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <cassert>

class Solution {
public:
    int binary_search(std::vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size() - 1;

        int mid = 0;

        while (true) {
            mid = (left + right) / 2;
            if (target < nums[mid]) {
                right = mid - 1;
            }
            else if (target > nums[mid]) {
                left = mid + 1;
            }
            else
                return mid;

            if (left > right)
                return -1;
        }
    }
};

void test_binary_search() {
    Solution solution;
    std::vector<int> test_nums_first = { -1,0,3,5,9,12 };
    assert(solution.binary_search(test_nums_first, 9) == 4);

    std::vector<int> test_nums_second = { -1,0,3,5,9,12 };
    assert(solution.binary_search(test_nums_second, 2) == -1);

    std::cout << "Tests OK" << std::endl;
}

#endif //ALGORITHM_TASKS_BINARY_SEARCH_H
