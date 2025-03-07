from pathlib import Path

from conan import ConanFile
from conan.tools.cmake import cmake_layout, CMakeToolchain

class ProtoBufRecipe(ConanFile):
    name = "protobuf"
    settings = "os", "compiler", "build_type", "arch"
    '这个设置必须要有，否则会出现找不到 build_type 的错误。'

    def requirements(self):
        '依赖项'
        #self.requires("abseil/20240722.0")
        self.requires("abseil/20250127.0@third_party/develop")

    def layout(self):
        '这个函数必须要有，用于控制 conan 文件生成位置。'
        cmake_layout(self, build_folder="build_msvc")
    
    def generate(self):
        tc = CMakeToolchain(self) 
        tc.user_presets_path = False # prevent CMakeUserPresets.json from being generated
        for _, v in self.dependencies._data.items():
            pkg = str(v)[:str(v).find('/')]
            cur_dependency = self.dependencies[pkg]
            config_path = cur_dependency.cpp_info.get_property("config_path")
            config_name = cur_dependency.cpp_info.get_property("cmake_file_name")
            if config_path is not None and config_name is not None:
                tc.variables[config_name + "_DIR"] = (Path(cur_dependency.package_folder) / config_path).as_posix()
        tc.generate()
