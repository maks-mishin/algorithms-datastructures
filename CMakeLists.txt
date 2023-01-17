cmake_minimum_required(VERSION 3.16)
project(algorithms_datastructures)

set(CMAKE_CXX_STANDARD 17)

add_executable(
    algorithms_datastructures
    codewars/cpp/josefus_survivor.cpp
)
target_include_directories(
    algorithms_datastructures
    PRIVATE
    unit_test_framework
)