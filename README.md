## This repository holds a conan recipe for Ubitrack.

[Conan.io](https://conan.io) package for the [Ubitrack](https://github.com/Ubitrack/ubitrack) project

This is a special "meta-package" which includes all other TUM ubitrack packages as conan dependencies. By adding this package to your Conan project, you effectively get "All of Ubitrack" libraries with one `requires` statement.

### Preparations

Some dependencies are fetched from the bincrafters repository. If not already active, you should add their repository:

    $ conan remote add bincrafters "https://api.bintray.com/conan/bincrafters/public-conan"

All TUM Ubitrack related software packages are hosted on the [CAMPAR](http://campar.in.tum.de) conan repository. The repository can be added using the following command after installing conan and your favourite compiler.

    $ conan remote add camposs "https://conan.campar.in.tum.de/api/conan/conan-camposs"
    $ conan remote add ubitrack "https://conan.campar.in.tum.de/api/conan/conan-ubitrack"


## For Users: Use this package

### Basic setup

    $ conan install ubitrack/1.3.0@ubitrack/stable

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    ubitrack/1.3.0@ubitrack/stable

    [generators]
    txt

Complete the installation of requirements for your project running:</small></span>

    $ mkdir build && cd build && conan install ..
    
Note: It is recommended that you run conan install from a build directory and not the root of the project directory.  This is because conan generates *conanbuildinfo* files specific to a single build configuration which by default comes from an autodetected default profile located in ~/.conan/profiles/default .  If you pass different build configuration options to conan install, it will generate different *conanbuildinfo* files.  Thus, they shoudl not be added to the root of the project, nor committed to git. 

## For Packagers: Publish this Package

The example below shows the commands used to publish to ubitrack conan repository. To publish to your own conan respository (for example, after forking this git repository), you will need to change the commands below accordingly. 

## Build  

This is a header only library, so nothing needs to be built.

## Package 

    $ conan create . ubitrack/stable
    

## Upload

    $ conan upload ubitrack/1.3.0@ubitrack/stable --all -r ubitrack

### License
[Ubitrack](LICENSE)


## Install Notes for various platforms

### OSX

use homebrew to install the following dependencies

- git
- cmake
- libusb
- swig
