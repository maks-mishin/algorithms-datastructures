// Source : https://www.codewars.com/kata/57cfdf34902f6ba3d300001e
// Author : Maks Mishin
// Date   : 1/26/2022

#ifndef ALGORITHM_TASKS_SORT_AND_STAR_H
#define ALGORITHM_TASKS_SORT_AND_STAR_H

#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

std::string twoSort(std::vector<std::string> vec_str)
{
    std::sort(vec_str.begin(), vec_str.end());
    std::string result = "";
    for (std::string::iterator it=vec_str[0].begin(); it != vec_str[0].end() - 1; it++) {
        result += *it;
        result += "***";
    }
    result += vec_str[0].back();
    std::cout << result << std::endl;
    return result;
}

#endif //ALGORITHM_TASKS_SORT_AND_STAR_H
