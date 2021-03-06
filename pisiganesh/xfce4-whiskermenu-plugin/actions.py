#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import get
#from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

# if pisi can't find source directory, see /var/pisi/xfce4-whiskermenu-plugin/work/ and:
# WorkDir="xfce4-whiskermenu-plugin-"+ get.srcVERSION() +"/sub_project_dir/"

WorkDir = "."

def setup():

    shelltools.system("rpm2tar xfce4-whiskermenu-plugin-1.1.1-1.fc21.src.rpm")
    shelltools.system("tar -xf xfce4-whiskermenu-plugin-1.1.1-1.fc21.src.tar")
    shelltools.system("rm -f xfce4-whiskermenu-plugin.spec")
    shelltools.system("bzip2 -d xfce4-whiskermenu-plugin-1.1.1-src.tar.bz2")
    shelltools.system("tar -xf xfce4-whiskermenu-plugin-1.1.1-src.tar")
    
    shelltools.cd("xfce4-whiskermenu-plugin-1.1.1")
    cmaketools.configure("-DCMAKE_BUILD_TYPE=release", installPrefix="/usr")

def build():
    
    shelltools.cd("xfce4-whiskermenu-plugin-1.1.1")
    cmaketools.make()

def install():

    shelltools.cd("xfce4-whiskermenu-plugin-1.1.1")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

# Take a look at the source folder for these file as documentation.
#    pisitools.dodoc("AUTHORS", "BUGS", "ChangeLog", "COPYING", "README")

# If there is no install rule for a runnable binary, you can 
# install it to binary directory.
#    pisitools.dobin("xfce4-whiskermenu-plugin")

# You can use these as variables, they will replace GUI values before build.
# Package Name : xfce4-whiskermenu-plugin
# Version : 1.2.1
# Summary : Alternate Xfce Menu - Whisker Menu

# For more information, you can look at the Actions API
# from the Help menu and toolbar.

# By PiSiDo 2.0.0
