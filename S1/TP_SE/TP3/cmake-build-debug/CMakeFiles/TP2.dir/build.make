# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.26

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /Applications/CLion.app/Contents/bin/cmake/mac/bin/cmake

# The command to remove a file.
RM = /Applications/CLion.app/Contents/bin/cmake/mac/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/aicha/Documents/TP_SE/TP3

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/aicha/Documents/TP_SE/TP3/cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/TP2.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/TP2.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/TP2.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/TP2.dir/flags.make

CMakeFiles/TP2.dir/EXO1.c.o: CMakeFiles/TP2.dir/flags.make
CMakeFiles/TP2.dir/EXO1.c.o: /Users/aicha/Documents/TP_SE/TP3/EXO1.c
CMakeFiles/TP2.dir/EXO1.c.o: CMakeFiles/TP2.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/aicha/Documents/TP_SE/TP3/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/TP2.dir/EXO1.c.o"
	/Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT CMakeFiles/TP2.dir/EXO1.c.o -MF CMakeFiles/TP2.dir/EXO1.c.o.d -o CMakeFiles/TP2.dir/EXO1.c.o -c /Users/aicha/Documents/TP_SE/TP3/EXO1.c

CMakeFiles/TP2.dir/EXO1.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/TP2.dir/EXO1.c.i"
	/Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /Users/aicha/Documents/TP_SE/TP3/EXO1.c > CMakeFiles/TP2.dir/EXO1.c.i

CMakeFiles/TP2.dir/EXO1.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/TP2.dir/EXO1.c.s"
	/Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /Users/aicha/Documents/TP_SE/TP3/EXO1.c -o CMakeFiles/TP2.dir/EXO1.c.s

# Object files for target TP2
TP2_OBJECTS = \
"CMakeFiles/TP2.dir/EXO1.c.o"

# External object files for target TP2
TP2_EXTERNAL_OBJECTS =

libTP2.a: CMakeFiles/TP2.dir/EXO1.c.o
libTP2.a: CMakeFiles/TP2.dir/build.make
libTP2.a: CMakeFiles/TP2.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/aicha/Documents/TP_SE/TP3/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C static library libTP2.a"
	$(CMAKE_COMMAND) -P CMakeFiles/TP2.dir/cmake_clean_target.cmake
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/TP2.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/TP2.dir/build: libTP2.a
.PHONY : CMakeFiles/TP2.dir/build

CMakeFiles/TP2.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/TP2.dir/cmake_clean.cmake
.PHONY : CMakeFiles/TP2.dir/clean

CMakeFiles/TP2.dir/depend:
	cd /Users/aicha/Documents/TP_SE/TP3/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/aicha/Documents/TP_SE/TP3 /Users/aicha/Documents/TP_SE/TP3 /Users/aicha/Documents/TP_SE/TP3/cmake-build-debug /Users/aicha/Documents/TP_SE/TP3/cmake-build-debug /Users/aicha/Documents/TP_SE/TP3/cmake-build-debug/CMakeFiles/TP2.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/TP2.dir/depend

