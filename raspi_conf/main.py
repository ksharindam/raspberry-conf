#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, os
from shutil import move
from tempfile import NamedTemporaryFile
from PyQt4 import QtCore, QtGui

sys.path.append(os.path.dirname(__file__))
from ui_window import Ui_window

config_file = '/boot/config.txt'
cmdline_file = '/boot/cmdline.txt'

class Window(QtGui.QDialog, Ui_window):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.checkOpengl.clicked.connect(self.toggleOpengl)
        self.checkUsbcurrent.clicked.connect(self.maximizeUsbcurrent)
        self.comboGpuram.activated.connect(self.changeGpuRam)
        self.comboAudio.activated.connect(self.changeAudioOutput)
        self.rebootButton.clicked.connect(self.reboot)
        self.gpu_ram = ['64', '128', '192']
        keys = ['gpu_mem', 'arm_freq', 'max_usb_current', 'dtoverlay=vc4-kms-v3d']
        values = getConfig(config_file, keys)
        if 'dtoverlay=vc4-kms-v3d' in values:
            self.checkOpengl.setChecked(True)
        if 'max_usb_current' in values:
            self.checkUsbcurrent.setChecked(bool( int(values['max_usb_current']) ))
        if 'gpu_mem' in values:
            self.comboGpuram.setCurrentIndex(self.gpu_ram.index(values['gpu_mem']))
        self.show()

    def toggleOpengl(self, checked):
        if checked:
            setConfig(config_file, 'dtoverlay=vc4-kms-v3d')
            setConfig(config_file, 'avoid_warnings', '2')
            move('/usr/share/X11/xorg.conf.d/99-fbturbo.conf', '/usr/share/X11/xorg.conf.d/99-fbturbo.conf~')
            str_replace(cmdline_file, ' quiet', '')
            str_replace(cmdline_file, ' splash', '')
            str_replace(cmdline_file, ' plymouth.ignore-serial-consoles', '')
        else:
            clearConfig(config_file, "dtoverlay=vc4-kms-v3d")
            move('/usr/share/X11/xorg.conf.d/99-fbturbo.conf~', '/usr/share/X11/xorg.conf.d/99-fbturbo.conf')

    def maximizeUsbcurrent(self, checked):
        """ maximizeUsbcurrent(bool checked) """
        if checked:
            setConfig(config_file, 'max_usb_current', '1')
        else:
            clearConfig(config_file, 'max_usb_current')

    def changeGpuRam(self, index):
        setConfig(config_file, 'gpu_mem', self.gpu_ram[index])

    def changeAudioOutput(self, index):
        outputs = ['0', '2', '1']
        os.system('amixer cset numid=3 ' + outputs[index])

    def reboot(self):
        os.system('init 6')


# Static functions to change config files

def setConfig(config_file, key, value=None):
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

def clearConfig(config_file, key):
    """ clearConfig(str config_file, str key)
        Adds a # before key-value line """
    with NamedTemporaryFile(delete=False) as tmp_source:
        with open(config_file, 'r') as source_file:
            for line in source_file:
                if line.startswith(key):
                    tmp_source.write('#'+line)
                else:
                    tmp_source.write(line)
    move(tmp_source.name, source_file.name)

def getConfig(config_file, keys):
    ''' getConfig(str config_file, list keys)
        Returns a dict of keys and values '''
    key_dict = {}
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

def main():
    app = QtGui.QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

