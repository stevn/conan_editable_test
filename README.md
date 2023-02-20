# Conan editable mode tests

Tested with:

- Conan client version: 1.59.0
- Windows 10
- Python 3.10.5

## Quick Reproduction of Error state (TLDR)

To reproduce run the following commands:

    cd project_a_comp
    conan editable add . prj_a_comp/1.0.0@test/develop
    conan install . -s:b build_type=Release -s:h build_type=Debug
    conan build .
    cd ../project_b_comp
    conan install . -s:b build_type=Release -s:h build_type=Debug
    conan build .

You will get a CMake Error:  Library 'prj_a_comp' not found in package.

I am not sure how to fix this via package info?

For more details on how this test was created, keep reading..

## Normal approach (without components)

This works as expected as far as I can tell.

### Setup project A

    mkdir project_a
    cd project_a
    conan new prj_a/1.0.0 -m cmake_lib

Make project A editable and build it:

    conan editable add . prj_a/1.0.0@test/develop
    conan install . -s:b build_type=Release -s:h build_type=Debug
    conan build .

### Build project B

    mkdir project_b
    cd project_b
    conan new prj_b/1.0.0 -m cmake_exe

Modify project B to require and link project A package (prj_a/1.0.0@test/develop).

Build project B (link against 'editable' project A):

    cd project_b
    conan install . -s:b build_type=Release -s:h build_type=Debug
    conan build .
    build/Debug/prj_b

### Success

It works!

## Component-based approach (broken)

This is probably broken as far as I can tell. It matches the 'normal' approach in all regards except that it uses components.

### Setup project A with components

    mkdir project_a_comp
    cd project_a_comp
    conan new prj_a_comp/1.0.0 -m cmake_lib

Modify conanfile.py to use component name for cppinfo: self.cpp_info.components[COMPONENT_NAME_PROJECT_A].libs = ["prj_a_comp"]

Modify test_package to link component (prj_a_comp::ProjectAComp) instead of whole package (prj_a_comp::prj_a_comp).

Make component-based project A editable and build it:

    cd project_a_comp
    conan editable add . prj_a_comp/1.0.0@test/develop
    conan install . -s:b build_type=Release -s:h build_type=Debug
    conan build .

### Build component-based project B with project A in editable mode

    mkdir project_b_comp
    cd project_b_comp
    conan new prj_b_comp/1.0.0 -m cmake_exe

Modify component-based project B to require and link component-based project A package (prj_a_comp/1.0.0@test/develop).

Make sure to link against the component this time (prj_a_comp::ProjectAComp) instead of the full package (prj_a_comp::prj_a_comp).

Build component-based project B (link against 'editable' component-based project A):

    cd project_b_comp
    conan install . -s:b build_type=Release -s:h build_type=Debug
    conan build .

### Error

The Conan build (`conan build .`) of component-based project B fails with the following error:

```bash

-- Conan: Component target declared 'prj_a_comp::ProjectAComp'
-- Conan: Target declared 'prj_a_comp::prj_a_comp'
CMake Error at build/generators/cmakedeps_macros.cmake:39 (message):
  Library 'prj_a_comp' not found in package.  If 'prj_a_comp' is a system
  library, declare it with 'cpp_info.system_libs' property
Call Stack (most recent call first):
  build/generators/prj_a_comp-Target-debug.cmake:24 (conan_package_library_targets)
  build/generators/prj_a_compTargets.cmake:26 (include)
  build/generators/prj_a_comp-config.cmake:16 (include)
  CMakeLists.txt:4 (find_package)


-- Configuring incomplete, errors occurred!
See also "conan_editable_test/project_b_comp/build/CMakeFiles/CMakeOutput.log".
ERROR: conanfile.py (prj_b_comp/1.0.0): Error in build() method, line 37
        cmake.configure()
        ConanException: Error 1 while executing cmake -G "Visual Studio 16 2019" -DCMAKE_TOOLCHAIN_FILE="conan_editable_test/project_b_comp/build/generators/conan_toolchain.cmake" -DCMAKE_POLICY_DEFAULT_CMP0091="NEW" "conan_editable_test\project_b_comp\."

```

Conan fails to find the library prj_a_comp for that component.

### Workaround: Build component-based project B with component-based project A in Conan cache

In order to build component-based project B, we can turn off the editable mode of component-based project A.

This can be used as workaround because Conan editable mode seems to be broken.

    conan editable remove prj_a_comp/1.0.0@test/develop
    cd project_a_comp
    conan create . test/develop -s:b build_type=Release -s:h build_type=Debug
    cd ../project_b_comp
    conan install . -s:b build_type=Release -s:h build_type=Debug
    conan build .

The build works. Conan create of project B also works.

This example shows that Conan components in general work correctly and are configured correctly in this test.

However, now we have disabled editable mode.

*So: It looks like the error only happens when combining both Conan features: editable mode + components.*
