cmake_minimum_required(VERSION 3.16)
project(algorithms_datastructures)

set(CMAKE_CXX_STANDARD 17)

add_executable(
    main
    main.cpp
    unit_test_framework/unit_test_framework.h
)

target_include_directories(
    main
    PRIVATE
    unit_test_framework
)