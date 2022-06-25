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
