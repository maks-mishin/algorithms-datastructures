// Source : https://www.codewars.com/kata/559a28007caad2ac4e000083
// Author : Maks Mishin
// Date   : 1/28/2022

#ifndef ALGORITHM_TASKS_PERIMETER_SQUARES_RECTANGLE_H
#define ALGORITHM_TASKS_PERIMETER_SQUARES_RECTANGLE_H

typedef unsigned long long ull;
class SumFct
{
public:
    static ull perimeter(int n) {
        ull first = 1,
            second = 1,
            next_num,
            sum_seq = first + second;
        for (int i=2; i <= n; i++) {
            next_num = first + second;
            sum_seq += next_num;

            first = second;
            second = next_num;
        }
        return sum_seq*4;
    }
};

#endif //ALGORITHM_TASKS_PERIMETER_SQUARES_RECTANGLE_H
