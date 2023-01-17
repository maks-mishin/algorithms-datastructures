// Author : Maks Mishin
// Date : 2/5/2022

#pragma once

#include <iostream>
#include <set>
#include <vector>
#include <sstream>
#include <map>

template <class T>
std::ostream& operator << (std::ostream& os, const std::vector<T>& v);

template <class T>
std::ostream& operator << (std::ostream& os, const std::set<T>& s);

template <class K, class V>
std::ostream& operator << (std::ostream& os, const std::map<K, V>& m);

template <class T, class U>
void AssertEqual(const T& t, const U& u, const std::string& hint);

void Assert(bool b, const std::string& hint);

class TestRunner {
public:
    template <class TestFunc>
    void RunTest(TestFunc func, const std::string& test_name);
    ~TestRunner();

private:
    int fail_count = 0;
};

template <class T>
std::ostream& operator << (std::ostream& os, const std::vector<T>& v) {
    os << "{";
    bool first = true;
    for(const auto& item : v) {
        if (!first) {
            os << ", ";
        }
        first = false;
        os << item;
    }
    return os << "}";
}

template <class T>
std::ostream& operator << (std::ostream& os, const std::set<T>& s) {
    os << "{";
    bool first = true;
    for(const auto& item : s) {
        if (!first) {
            os << ", ";
        }
        first = false;
        os << item;
    }
    return os << "}";
}

template <class K, class V>
std::ostream& operator << (std::ostream& os, const std::map<K, V>& m) {
    os << "{";
    bool first = true;
    for(const auto& kv : m) {
        if (!first) {
            os << ", ";
        }
        first = false;
        os << kv.first << ": " << kv.second;
    }
    return os << "}";
}

template <class T, class U>
void AssertEqual(const T& t, const U& u, const std::string& hint) {
    if (t != u) {
        std::ostringstream os;
        os << "Assertion failed: " << t << " != " << u
           << " Hint: " << hint;
        throw std::runtime_error(os.str());
    }
}

void Assert(bool b, const std::string& hint) {
    AssertEqual(b, true, hint);
}

template <class TestFunc>
void TestRunner::RunTest(TestFunc func, const std::string& test_name) {
    try {
        func();
        std::cerr << test_name << " OK" << std::endl;
    } catch (std::exception& e) {
        ++fail_count;
        std::cerr << test_name << " fail: " << e.what() << std::endl;
    } catch (...) {
        ++fail_count;
        std::cerr << "Unknown exception caught" << std::endl;
    }
}

TestRunner::~TestRunner() {
    if (fail_count > 0) {
        std::cerr << fail_count << " unit tests failed. Terminate" << std::endl;
        exit(1);
    }
}