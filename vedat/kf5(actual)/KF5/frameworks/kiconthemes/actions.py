#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools

def setup():
    pisitools.ldflags.add("-Wl,-rpath,/usr/lib")
    cmaketools.configure("-DCMAKE_BUILD_TYPE=Release \
                          -DLIB_INSTALL_DIR=lib \
                          -DQML_INSTALL_DIR=lib/qt5/qml \
                          -DPYTHON_EXECUTABLE=/usr/bin/python3 \
                          -DLOCALE_INSTALL_DIR=/usr/share/locale \
                          -DQT_PLUGIN_INSTALL_DIR=lib/qt5/plugins \
                          -DECM_MKSPECS_INSTALL_DIR=/usr/lib/qt5/mkspecs/modules \
                          -DBUILD_TESTING=OFF")

def build():
    cmaketools.make()

def install():
    cmaketools.install()
    
    pisitools.dodoc("README.md", "COPYING.LIB")