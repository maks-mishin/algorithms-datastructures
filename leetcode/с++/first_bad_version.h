// Source : https://leetcode.com/problems/first-bad-version/
// Date   : 1/26/2022

#ifndef ALGORITHM_TASKS_FIRST_BAD_VERSION_H
#define ALGORITHM_TASKS_FIRST_BAD_VERSION_H

// The API isBadVersion is defined.
bool isBadVersion(int version);

// for solving of problem the dichotomy method is used
class Solution {
public:
    int firstBadVersion(int n) {
        int left = 1, right = n;
        while (left + 1 < right) {
            int mid = left + (right - left) / 2;
            if (isBadVersion(mid))
                right = mid;
            else
                left = mid;
        }
        if (isBadVersion(left))
            return left;
        return right;
    }
};

#endif //ALGORITHM_TASKS_FIRST_BAD_VERSION_H
