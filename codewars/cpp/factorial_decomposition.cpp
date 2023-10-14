#include <iostream>
#include <vector>
#include <map>

std::string decomp(int n) {
    std::map<int, int> factorsCount;
    for (int i = 2; i <= n; ++i) {
        int copyNum = i;
        int factor = 2;
        while (copyNum != 1) {
            while(copyNum % factor == 0) {
                factorsCount[factor]++;
                copyNum /= factor;
            }
            factor++;
        }
        if (copyNum) factorsCount[copyNum]++;
    }
    std::string result;
    for (const auto p: factorsCount) {
        if (p.first == 1)
            continue;
        if (p.second == 1) {
            result += std::to_string(p.first) + " * ";
            continue;
        }
        result += std::to_string(p.first) + "^" + std::to_string(p.second) + " * ";
    }
    return result.substr(0, result.size() - 3);
}