cmake_minimum_required(VERSION 3.15)
project(PackageTest CXX)

find_package(prj_a_comp CONFIG REQUIRED)

add_executable(example src/example.cpp)
target_link_libraries(example prj_a_comp::ProjectAComp)
