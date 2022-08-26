// Source : https://leetcode.com/problems/minimum-index-sum-of-two-lists/
// Author : Maks Mishin
// Date   : 2/3/2022

#ifndef ALGORITHM_TASKS_FIND_RESTAURANT_H
#define ALGORITHM_TASKS_FIND_RESTAURANT_H

#include <vector>
#include <map>
#include <string>

class Solution {
public:
    std::vector<std::string> findRestaurant(std::vector<std::string>& list1,
            std::vector<std::string>& list2) {
        int sum = 0, min_sum = 2000;
        std::vector<std::string> list_common = {};
        std::map<std::string, int> map_list1;

        for(size_t i = 0; i < list1.size(); i++) {
            map_list1[list1[i]] = i;
        }

        for(size_t i = 0; i < list2.size() && i <= min_sum; i++) {
            if (map_list1.count(list2[i])) {
                sum = i + map_list1[list2[i]];
                if (sum < min_sum) {
                    min_sum = sum;
                    list_common.clear();
                    list_common.push_back(list2[i]);
                }
                else if (sum == min_sum) {
                    list_common.push_back(list2[i]);
                }
            }
        }
        return list_common;
    }
};

#endif //ALGORITHM_TASKS_FIND_RESTAURANT_H
