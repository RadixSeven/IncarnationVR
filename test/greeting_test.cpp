// This software is (C) 2022 by Eric David Moyer
// licenced under GPL 3.0 or later. See LICENSE.md for more.

#include "src/greeting.hpp"
#include "gtest/gtest.h"

TEST(greeting_test, greeting){
    EXPECT_EQ(greeting(), "Hello, World!");
}


