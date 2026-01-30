cmake_minimum_required(VERSION 3.14)
project(testing)

set(CMAKE_CXX_STANDARD 17)

add_library(main_lib main.cpp)

include_directories(${GTEST_INCLUDE_DIRS})

add_executable(testing tests/main_test.cpp)
target_link_libraries(testing main_lib ${GTEST_LIBRARIES} pthread)

install(TARGETS testing)

include(CTest)
enable_testing()
add_test(NAME testing COMMAND testing)
