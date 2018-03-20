#!/usr/bin/env python2.7
# -*- coding: utf-8 -*- 

#
# Applet in system tray
# You can show a popup just sending a DBus message here
# Send a signal to change the icon
#

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk
gi.require_version('AppIndicator3', '0.1')
from gi.repository import AppIndicator3 as appindicator
gi.require_version('Notify', '0.7')
from gi.repository import Notify as notify
from common import *
import os

try:
    from dbus.mainloop.glib import DBusGMainLoop
except ImportError:
    from dbus.mainloop.qt.DBusQtMainLoop import DBusGMainLoop
    #if none exists, an ImportError will be throw

APPINDICATOR_ID="LiSpeak4"

SIG_WAIT=1
SIG_DONE=2
SIG_STOP=3
SIG_RECORD=4
SIG_RESULT=5
SIG_MSG=6

indicatorInstance = None

def msg_handler(*args,**keywords):
    """
    Dbus message handler
    @param path should be something like aaa/bb/ccc/SIGNAL
    """
    global indicatorInstance
    if indicatorInstance is not None:
        try:
            indicatorInstance.last_signal = int(keywords['path'].split("/")[4])
            if last_signal == SIG_MSG:
                indicatorInstance.notify( keywords['path'].split("/")[3] )
        except:
            pass

class LiSpeakIndicator:
    def __init__(self):
        
        self.ind = appindicator.Indicator(APPINDICATOR_ID, os.path.join(GLADE_TEMPLATE_FOLDER, "mic.png"),
                appindicator.CATEGORY_APPLICATION_STATUS)
        self.ind.set_status(appindicator.STATUS_ACTIVE)

        self.menu_setup()
        self.ind.set_menu(self.menu)
        self.progress = 0
        self.last_signal = None

        gobject.timeout_add(100, self.updateIcon)

    def menu_setup(self):
        self.menu = gtk.Menu()

        self.r_item = gtk.MenuItem("Restart Servers")
        self.r_item.connect("activate", self.restart)
        self.r_item.show()
        self.menu.append(self.r_item)
        
        self.r_item = gtk.MenuItem("Settings")
        self.r_item.connect("activate", self.settings)
        self.r_item.show()
        self.menu.append(self.r_item)
        
        separator = gtk.SeparatorMenuItem()
        separator.show()
        self.menu.append(separator)

        self.quit_item = gtk.MenuItem("Quit")
        self.quit_item.connect("activate", self.quit)
        self.quit_item.show()
        self.menu.append(self.quit_item)

    def main(self):
        notify.init(APPINDICATOR_ID)
        gtk.main()

    def quit(self, widget):
        #TODO
        #subprocess.call(["./stop"])
        notify.uninit()
        gtk.main_quit()
    
    def restart(self,widget):
        #TODO
        subprocess.call([LISPEAK_BIN])

    def openBrowser(self,widget):
        #TODO
        os.system(PWD + "/../Recognition/bin/open "+PWD+"/browser.py")
        
    def settings(self,widget):
        #TODO
        os.system(SETTINGS_BIN)
        
    def updateIcon(self):
        global last_signal
        reset = False
        if last_signal == SIG_DONE:
            self.ind.set_icon(os.path.join(GLADE_TEMPLATE_FOLDER, "mic.png"))
            last_signal = None
            reset = True
        if last_signal == SIG_RECORD:
            self.ind.set_icon(os.path.join(GLADE_TEMPLATE_FOLDER, "listen.png"))
            last_signal = None
            reset = True
        if last_signal == SIG_STOP:
            self.ind.set_icon(os.path.join(GLADE_TEMPLATE_FOLDER, "wait.png"))
            last_signal = None
            reset = True
        if reset == False and last_signal == SIG_WAIT:
            self.ind.set_icon(os.path.join(GLADE_TEMPLATE_FOLDER, "analyzing", "tmp-"+str(self.progress)+".gif"))
            self.progress += 1
            if self.progress == 8:
                self.progress = 0
        else:
            last_signal = None
        return True

    def notify(self, htmlTitle, htmlContent=None, icon=None):
        """
        Wrapper to notify.Notification 
        """
        #TODO should handle speak response, and some kind of queue
        notify.Notification.new(htmlTitle, htmlContent, icon).show()

if __name__ == "main":

    DBusGMainLoop(set_as_default=True)
    bus = dbus.SessionBus()
    bus.request_name("org.lispeak.Notify")
    bus.add_signal_receiver(handler_function=msg_handler, dbus_interface='org.lispeak',
                signal_name='Notify', interface_keyword='iface',    member_keyword='member', path_keyword='path')

    indicatorInstance = LiSpeakIndicator()
    gtk.main()


