#include <list>
#include <numeric>
#include "unit_test_framework.h"

// TODO: simplify solution
auto GetNewPeoplePosition(std::list<int>& peoples, std::list<int>::iterator& position,
                          const int step) {
    auto newPosition = position;
    for (int i = 0; i < step - 1; i++) {
        if (newPosition == peoples.end())
            newPosition = peoples.begin();
        newPosition++;
        if (newPosition == peoples.end())
            newPosition = peoples.begin();
    }
    return newPosition;
}

int josephusSurvivor(int countPeoples, int step) {
    std::list<int> peoples(countPeoples);
    std::iota(peoples.begin(), peoples.end(), 1);
    auto peoplePosition = peoples.begin();
    while (peoples.size() > 1) {
        peoplePosition = peoples.erase(
                GetNewPeoplePosition(peoples, peoplePosition, step)
        );
    }
    return peoples.back();
}

void TestExaples() {
    AssertEqual(josephusSurvivor(7, 3), 4, "survivor 4");
    AssertEqual(josephusSurvivor(11, 19), 10, "");
    AssertEqual(josephusSurvivor(1, 300), 1, "");
    AssertEqual(josephusSurvivor(14, 2), 13, "");
    AssertEqual(josephusSurvivor(100, 1), 100, "");

}

void TestBasic() {
    AssertEqual(josephusSurvivor(40, 3), 28, "survivor 4");
    AssertEqual(josephusSurvivor(2, 200), 1, "");
    AssertEqual(josephusSurvivor(5, 300), 1, "");
    AssertEqual(josephusSurvivor(7, 300), 7, "");
    AssertEqual(josephusSurvivor(300, 300), 265, "");
}

int main() {
    TestRunner testRunner;
    testRunner.RunTest(TestExaples, "TestExamples");
    testRunner.RunTest(TestBasic, "TestBasic");
    return 0;
}