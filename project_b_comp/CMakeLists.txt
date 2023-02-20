cmake_minimum_required(VERSION 3.15)
project(prj_b_comp CXX)

find_package(prj_a_comp REQUIRED)

add_executable(prj_b_comp src/prj_b_comp.cpp src/main.cpp)
target_include_directories(prj_b_comp PUBLIC include)
target_link_libraries(prj_b_comp PRIVATE prj_a_comp::ProjectAComp)

install(TARGETS prj_b_comp)
