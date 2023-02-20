cmake_minimum_required(VERSION 3.15)
project(prj_b CXX)

find_package(prj_a REQUIRED)

add_executable(prj_b src/prj_b.cpp src/main.cpp)
target_include_directories(prj_b PUBLIC include)
target_link_libraries(prj_b PRIVATE prj_a::prj_a)

install(TARGETS prj_b)
