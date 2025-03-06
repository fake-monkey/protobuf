from conan import ConanFile
from conan.tools.cmake import cmake_layout

class ProtoBufRecipe(ConanFile):
    name = "protobuf"
    settings = "os", "compiler", "build_type", "arch"
    '这个设置必须要有，否则会出现找不到 build_type 的错误。'

    generators = "CMakeDeps", "CMakeToolchain"
    '必须设置生成器，否则 Conan 不生成 conan_toolchain.cmake 文件'

    def requirements(self):
        '依赖项'
        self.requires("abseil/20250127.0@third_party/develop")

    def layout(self):
        '这个函数必须要有，用于控制 conan 文件生成位置。'
        cmake_layout(self, build_folder="build_msvc")
