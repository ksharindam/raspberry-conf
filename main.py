#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Name = Rasp-Conf
Version = 1.0
Description = Graphical Configuration manager for Raspberry Pi 2
..................................................................................
   Copyright (C) 2017 Arindam Chaudhuri <ksharindam@gmail.com>
  
   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.
  
   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.
  
   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.
..................................................................................
"""

import sys
from os import system
from shutil import move
from tempfile import NamedTemporaryFile
from PyQt4 import QtCore, QtGui
from gui import Ui_window

config_file = '/boot/config.txt'
cmdline_file = '/boot/cmdline.txt'

class Window(QtGui.QDialog, Ui_window):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.checkOpengl.toggled.connect(self.toggleOpengl)
        self.checkOverclock.toggled.connect(self.toggleOverclock)
        self.checkUsbcurrent.toggled.connect(self.maximizeUsbcurrent)
        self.comboGpuram.currentIndexChanged.connect(self.changeGpuRam)
        self.rebootButton.clicked.connect(self.reboot)
        self.show()
        values = self.getConfig()
        if 'dtoverlay=vc4-kms-v3d' in values:
            self.checkOpengl.setChecked(True)
        if 'arm_freq' in values:
            if values['arm_freq'] == '1000': self.checkOverclock.setChecked(True)
        if 'max_usb_current' in values:
            if values['max_usb_current'] == '1': self.checkUsbcurrent.setChecked(True)
        if 'gpu_mem' in values:
            if values['gpu_mem'] == '128': self.comboGpuram.setCurrentIndex(1)
    def toggleOpengl(self, checked):
        if checked:
            self.setConfig('dtoverlay=vc4-kms-v3d')
            self.setConfig('avoid_warnings', '2')
            move('/usr/share/X11/xorg.conf.d/99-fbturbo.conf', '/usr/share/X11/xorg.conf.d/99-fbturbo.conf~')
            str_replace(cmdline_file, ' quiet', '')
            str_replace(cmdline_file, ' splash', '')
            str_replace(cmdline_file, ' plymouth.ignore-serial-consoles', '')
        else:
            self.clearConfig("dtoverlay=vc4-kms-v3d")
            move('/usr/share/X11/xorg.conf.d/99-fbturbo.conf~', '/usr/share/X11/xorg.conf.d/99-fbturbo.conf')
    def toggleOverclock(self, checked):
        if checked:
            self.setConfig('arm_freq', '1000')
            self.setConfig('core_freq', '500')
            self.setConfig('sdram_freq', '500')
            self.setConfig('over_voltage', '2')
        else:
            self.clearConfig('arm_freq')
            self.clearConfig('core_freq')
            self.clearConfig('sdram_freq')
            self.clearConfig('over_voltage')
    def maximizeUsbcurrent(self, checked):
        """ maximizeUsbcurrent(bool checked) """
        if checked:
            self.setConfig('max_usb_current', '1')
        else:
            self.clearConfig('max_usb_current')
    def changeGpuRam(self, index):
        if index == 0:
            self.setConfig('gpu_mem', '64')
        else:
            self.setConfig('gpu_mem', '128')
    def reboot(self):
        system('init 6')
    def setConfig(self, key, value=None):
        """ setConfig(str key, str value=None)
            This changes the value of a key """
        if value:
            value = '='+value
        else:
            value = ''
        value_changed = False
        with NamedTemporaryFile(delete=False) as tmp_source:
            with open(config_file, 'r') as source_file:
                for line in source_file:
                    if line.startswith('#'+key) or line.startswith(key):
                        tmp_source.write(key+value+'\n')
                        value_changed = True
                    else:
                        tmp_source.write(line)
                if not value_changed:
                    tmp_source.write(key+value+'\n')
        move(tmp_source.name, source_file.name)
    def clearConfig(self, key):
        """ clearConfig(str key)
            Removes a key-value line """
        with NamedTemporaryFile(delete=False) as tmp_source:
            with open(config_file, 'r') as source_file:
                for line in source_file:
                    if line.startswith(key):
                        tmp_source.write('#'+line)
                    else:
                        tmp_source.write(line)
        move(tmp_source.name, source_file.name)
    def getConfig(self):
        key_dict = {}
        keys = ['gpu_mem', 'arm_freq', 'max_usb_current', 'dtoverlay=vc4-kms-v3d']
        with open(config_file, 'r') as source_file:
            for line in source_file:
                if not line.startswith('#'):
                    for key in keys:
                        if line.startswith(key):
                            value = line.replace(key, '')
                            value = value.replace('=', '')
                            value = value.rstrip()
                            key_dict[key] = value
        return key_dict
def str_replace(filename, to_replace, replace_with):
    """ str_replace(str filename, str to_replace, str replace_with)"""
    with NamedTemporaryFile(delete=False) as tmp_source:
        with open(filename, 'r') as source_file:
            for line in source_file:
                line = line.replace(to_replace, replace_with)
                tmp_source.write(line)
    move(tmp_source.name, source_file.name)

app = QtGui.QApplication(sys.argv)
win = Window()
sys.exit(app.exec_())
