#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools
import os


class CxxOptsConan(ConanFile):
    name = "cxxopts"
    version = "v2.2.0"
    description = "Lightweight C++ command line option parser"
    # topics can get used for searches, GitHub topics, Bintray tags etc. Add here keywords about the library
    topics = ("conan", "cxxopts", "command line")
    url = "https://github.com/ashlander/cxxopts-conan.git"
    homepage = "https://github.com/jarro2783/cxxopts"
    author = "Inexor <info@inexor.org>"
    license = "BSD 2-Clause"
    no_copy_source = True

    # Packages the license for the conanfile.py
    exports = ["LICENSE"]

    # Custom attributes for Bincrafters recipe conventions
    _source_subfolder = "cxxopts"

    def source(self):
        git = tools.Git(folder=self._source_subfolder)
        git.clone("https://github.com/jarro2783/cxxopts")
        git.checkout(self.version)

    def package(self):
        include_folder = os.path.join(self._source_subfolder, "include")
        self.copy(pattern="LICENSE", dst="licenses", src=self._source_subfolder)
        self.copy(pattern="*", dst="include", src=include_folder)

    def package_id(self):
        self.info.header_only()
