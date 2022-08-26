// Source : https://leetcode.com/problems/climbing-stairs/
// Author : Maks Mishin
// Date   : 2/1/2022

#ifndef ALGORITHM_TASKS_CLIMBING_STAIRS_H
#define ALGORITHM_TASKS_CLIMBING_STAIRS_H

class Solution {
public:
    int climbStairs(int n) {
        int first = 0, second = 1, fib = 0;
        for (int i = 0; i < n; ++i) {
            fib = first + second;
            first = second;
            second = fib;
        }
        return fib;
    }
};

#endif //ALGORITHM_TASKS_CLIMBING_STAIRS_H
