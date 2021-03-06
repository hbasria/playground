#!/usr/bin/python
# -*- coding: utf-8 -*-
#

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    autotools.configure("--disable-scrollkeeper \
                         --disable-static \
                         --disable-update-mimedb \
                         --with-gtk=2.0")

    # fix unused-direct-shlib-dependency
    pisitools.dosed("libtool", "( -shared )", " -Wl,-O1,--as-needed\\1")



def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # remove needless gsettings convert file to avoid slow session start
    pisitools.removeDir("/usr/share/MateConf")

    pisitools.dodoc("README", "COPYING", "NEWS", "ChangeLog", "AUTHORS", "TODO")

    pisitools.remove("/usr/share/applications/mimeinfo.cache")