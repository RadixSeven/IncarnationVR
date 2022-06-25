# This software is (C) 2022 by Eric David Moyer
# licenced under GPL 3.0 or later. See README.md for more.
cc_binary(
    name = "main",
    srcs = ["main.cpp"],
    deps = ["greeting"],
)

cc_library(
    name = "greeting",
    srcs = [
        "greeting.cpp",
    ],
    hdrs = ["greeting.hpp"],
    visibility = ["//test:__pkg__"],
)
