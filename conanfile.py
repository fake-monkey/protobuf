from conan import ConanFile
from conan.tools import files

class ProtoBufRecipe(ConanFile):
    name = "protobuf"
    version = "30.0"
    user = "third_party"
    channel = "develop"
    settings = "os", "arch"
    
    def package_info(self):
        self.cpp_info.builddirs = ["cmake/protobuf","cmake/utf8_range"]
        self.cpp_info.set_property("cmake_find_mode", "none")

    def package(self):
        for d in ['bin*/*', 'include/*', 'lib*/*', 'cmake/*', 'conanfile.py']:
            files.copy(self, d, self.source_folder, self.package_folder, keep_path=True)
