#include "src/greeting.hpp"
#include "gtest/gtest.h"

TEST(greeting_test, greeting){
    EXPECT_EQ(greeting(), "Hello, World!");
}


