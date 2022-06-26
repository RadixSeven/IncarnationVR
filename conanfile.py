
import os
from conan import ConanFile
from conan.tools.google import Bazel, bazel_layout
from conan.tools.files import copy


class IncarnationVrConan(ConanFile):
    name = "incarnation_vr"
    version = "0.1"

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"

    # These paths end up being wrong if you move to the conandeps directory and if you use
    # ../src/*, the files in that directory will end up in the main root directory alongside WORKSPACE.bazel
    exports_sources = "src/*", "test/*", "WORKSPACE.bazel"

    generators = "BazelDeps", "BazelToolchain"

    requires = ["boost/1.76.0",  "openvr/1.16.8"]

    def layout(self):
        bazel_layout(self)

    def build(self):
        bazel = Bazel(self)
        bazel.configure()
        bazel.build(label="//src:main")

    def package(self):
        dest_bin = os.path.join(self.package_folder, "bin")
        build = os.path.join(self.build_folder, "bazel-bin", "src")
        copy(self, "src", build, dest_bin, keep_path=False)
        copy(self, "main.exe", build, dest_bin, keep_path=False)
        