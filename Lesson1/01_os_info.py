# -*- coding: utf-8 -*-
import platform
import sys

# Этой программой собираю информацию об операционной системе и версии питона.

import platform
import sys

info = 'OS info is \n {}\n\nPython version is {} {}'.format(
    platform.uname(), sys.version, platform.architecture())
print(info)

with open('os_info.txt', 'w') as ff:
    ff.write(info)
# все работает!
