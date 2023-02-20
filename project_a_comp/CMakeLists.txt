cmake_minimum_required(VERSION 3.15)
project(prj_a_comp CXX)

add_library(prj_a_comp src/prj_a_comp.cpp)
target_include_directories(prj_a_comp PUBLIC include)

set_target_properties(prj_a_comp PROPERTIES PUBLIC_HEADER "include/prj_a_comp.h")
install(TARGETS prj_a_comp)
