from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout

COMPONENT_NAME_PROJECT_A = "ProjectAComp"


class PrjACompConan(ConanFile):
    name = "prj_a_comp"
    version = "1.0.0"

    # Optional metadata
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of PrjAComp here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "src/*", "include/*"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def layout(self):
        cmake_layout(self)
        self.cpp.source.components[COMPONENT_NAME_PROJECT_A].includedirs = self.cpp.source.includedirs
        self.cpp.build.components[COMPONENT_NAME_PROJECT_A].libdirs = self.cpp.build.libdirs

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.components[COMPONENT_NAME_PROJECT_A].libs = ["prj_a_comp"]
