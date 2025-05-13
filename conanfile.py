from pathlib import Path

from conan import ConanFile
from conan.tools.cmake import cmake_layout, CMakeToolchain

class ProtoBufRecipe(ConanFile):
    name = "protobuf"
    version = "30.0"
    user = "third_party"
    channel = "develop"
    settings = "os", "arch"
    '这个设置必须要有，否则会出现找不到 build_type 的错误。'
    
    def package_info(self):
        self.cpp_info.builddirs = ["cmake"]
        self.cpp_info.set_property("cmake_find_mode", "none")
    
    def package(self):
        self.copy("*", self.source_folder, self.package_folder, keep_path=True)
