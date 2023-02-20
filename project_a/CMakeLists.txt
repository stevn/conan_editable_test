cmake_minimum_required(VERSION 3.15)
project(prj_a CXX)

add_library(prj_a src/prj_a.cpp)
target_include_directories(prj_a PUBLIC include)

set_target_properties(prj_a PROPERTIES PUBLIC_HEADER "include/prj_a.h")
install(TARGETS prj_a)
