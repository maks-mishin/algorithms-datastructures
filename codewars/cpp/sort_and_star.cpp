// Source : https://www.codewars.com/kata/57cfdf34902f6ba3d300001e
// Author : Maks Mishin
// Date   : 1/26/2022

#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include "unit_test_framework.h"

std::string twoSort(std::vector<std::string> vec_str) {
    std::sort(vec_str.begin(), vec_str.end());
    std::string result;
    for (auto it = vec_str[0].begin(); it != vec_str[0].end() - 1; it++) {
        result += *it;
        result += "***";
    }
    result += vec_str[0].back();
    return result;
}

void TestTwoSort() {
    std::string actual = twoSort(
            std::vector<std::string>{
                "bitcoin", "take", "over", "the", "world", "maybe",
                "who", "knows", "perhaps"
            });
    std::string expected = "b***i***t***c***o***i***n";
    AssertEqual(actual, expected, "first test");

    expected = "a***r***e";
    actual = twoSort(std::vector<std::string>{ "turns", "out", "random", "test", "cases", "are", "easier", "than", "writing", "out", "basic", "ones" });
    AssertEqual(actual, expected, "second test");
}

int main() {
    TestRunner testRunner;
    testRunner.RunTest(TestTwoSort, "TestTwoSort");
    return 0;
}
