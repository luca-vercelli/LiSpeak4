#!/usr/bin/env python2.7
# -*- coding: utf-8 -*- 
VERSION = 0.1

import gettext
gettext.textdomain('lispeak')
_ = gettext.gettext

import os

HOME = os.path.expanduser("~")					# This works in either Windows and Linux
CONFIG_FILE = os.path.join(HOME, ".lispeak4")	# This works in either Windows and Linux
CONFIG_SECTION1 = "General"
AUTOSTART_FILE = HOME + "/.config/autostart/lispeak.desktop"	# Autostart feature is Linux specific
GLADE_TEMPLATE_LOCATION=['.', '~/.local/share/lispeak/glade', '/usr/share/lispeak/glade']	# "." works in Windows, too.

def get_glade_folder():
    """
    Return the folder where you we can find 
    Glade templates and images
    """
    for path in GLADE_TEMPLATE_LOCATION:
        if os.path.isfile(os.path.join(path, "settings.glade")):
            return path
    
def load_user_info():
    """
    Load user info from configuration file
    @return dict
    """
    import ConfigParser
    defaults = {
        "autostart" : "False"
        }
    config = ConfigParser.ConfigParser(defaults)
    try:
        config.read(CONFIG_FILE)
        return dict(config.items(CONFIG_SECTION1))
    except:
        return defaults

def save_user_info(user_info_dict):
    """
    Write user info to configuration file
    """
    import ConfigParser
    config = ConfigParser.RawConfigParser()
    config.add_section(CONFIG_SECTION1)
    for key, value in user_info_dict.iteritems():
        config.set(CONFIG_SECTION1, str(key), str(value))
    with open(CONFIG_FILE, 'wb') as configfile:
        config.write(configfile)

class SettingsWindow:
    def __init__(self):
    
        glade_folder = get_glade_folder()

        self.languages = {"English":"en", "Polski":'pl', "Español":'es', "Français":'fr', "Italiano":"it"}
        self.languages2 = ["English", "Polski", "Español", "Français", "Italiano"]
        self.engines = ["espeak","Google TTS","pico2wave"]

        from gi.repository import Gtk
        self.builder = Gtk.Builder()
        self.builder.add_from_file(glade_folder + "/settings.glade")
        self.builder.connect_signals(self)
        self.window = self.builder.get_object("window1")
        self.window.set_title("LiSpeak Settings")
        self.about = self.builder.get_object("aboutdialog1")
        self.btnAbout = self.builder.get_object("btnAbout")
        self.btnAbout.connect("clicked", self.aboutOpen)
        self.notebook = self.builder.get_object("notebook1")
        self.btnClose = self.builder.get_object("btnClose")
        self.btnClose.connect("button-release-event",self.close)
        self.window.connect("destroy", self.close)
        self.addItems(self.builder.get_object("cmbEngine"), self.engines)
        self.addItems(self.builder.get_object("cmbLang"), self.languages2)
        self.fillFields(load_user_info())
        self.window.show_all()

    def close(self,a=None,b=None,c=None):
        #TODO each options should be saved on-the-fly, not on window close
        self.user_info = {}
        self.user_info["autostart"] = str(self.builder.get_object("chkStart").get_active())
        self.user_info["messages"] = str(self.builder.get_object("chkMessage").get_active())
        self.user_info["proxy"] = str(self.builder.get_object("chkProxy").get_active())
        self.user_info["proxyhost"] = self.builder.get_object("txtProxyhost").get_text()
        self.user_info["proxyport"] = self.builder.get_object("txtProxyport").get_text()
        self.user_info["tts"] = str(self.builder.get_object("chkTTS").get_active())
        self.user_info["ttsengine"] = str(self.builder.get_object("cmbEngine").get_active_text())
        self.user_info["lang"] = self.languages[str(self.builder.get_object("cmbLang").get_active_text())]
        self.user_info["continuous"] = str(self.builder.get_object("chkContinue").get_active())
        save_user_info(self.user_info)
        if self.user_info["autostart"] == "True":
            enable_autostart(True)
        else:
            enable_autostart(False)
        if self.user_info["continuous"] == "True":
            enable_continuous(True)
        else:
            enable_continuous(False)
        from gi.repository import Gtk
        Gtk.main_quit()
        #TODO run lispeak? or not?

    def aboutOpen(self,widget):
        self.about.show_all()

    def set_combo_active_text(self,combo, text):
        model = combo.get_model()
        for i in range(len(model)):
            if model[i][0] == text:
                combo.set_active(i)

    def addItems(self, obj, items):
        for e in items:
            obj.append_text(e)

    def fillFields(self, user_info):
        for e in ['proxyport','proxyhost']:
            if e in user_info:
                self.builder.get_object('txt'+e[0].upper()+e[1:]).set_text(user_info[e])
        if "autostart" in user_info:
            self.builder.get_object("chkStart").set_active(user_info["autostart"] == "True")
        if "messages" in user_info:
            self.builder.get_object("chkMessage").set_active(user_info["messages"] == "True")
        if "proxy" in user_info:
            self.builder.get_object("chkProxy").set_active(user_info["proxy"] == "True")
        if "continuous" in user_info:
            self.builder.get_object("chkContinue").set_active(user_info["continuous"] == "True")
        if "tts" in user_info:
            self.builder.get_object("chkTTS").set_active(user_info["tts"] == "True")
        if "ttsengine" in user_info:
            self.set_combo_active_text(self.builder.get_object("cmbEngine"), user_info["ttsengine"])
        else:
            self.builder.get_object("cmbEngine").set_active(0)
        if "lang" in user_info:
            languages_back = {"en":"English","pl":"Polski",'es':'Español','fr':'Français',"it":"Italiano"}
            self.set_combo_active_text(self.builder.get_object("cmbLang"), languages_back[user_info["lang"]])
        else:
            self.builder.get_object("cmbLang").set_active(0)

def enable_continuous(enable=True):
    """
    Enable/disable continuous mode
    @param state: True to enable, False to disable
    """
    #TODO
    pass

def enable_autostart(enable=True, path="/usr/bin"):
    """
    Enable/disable autostart at system startup
    @param state: True to enable, False to disable
    @path: common values are /usr/bin, /usr/local/bin, ~/bin
    """
    if enable:
        with open(AUTOSTART_FILE,"w") as f:
            f.write("""
[Desktop Entry]
Version="""+str(VERSION)+"""
Name=LiSpeak
GenericName=LiSpeak
Name[en_CA]=LiSpeak
Comment=LiSpeak is a voice command and control system
Exec="""+path+"""/lispeak-start
Terminal=false
Type=Application
Categories=Application;
""")
    else:
        import os
        if os.path.isfile(AUTOSTART_FILE):
            os.remove(AUTOSTART_FILE)


def open_dialog():
    import gi 
    gi.require_version('Gtk', '3.0')
    from gi.repository import Gtk
    app = SettingsWindow()
    Gtk.main()
    #FIXME if there is any exception, the Gtk windows close but the program remains alive...

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description=_('LiSpeak - Linux Voice Command And Control System - Settings panel'))
    parser.add_argument("--version",dest='version',action='store_true',default=False,help=_('Show version and exit'))
    args = parser.parse_args()
    if args.version:
        print "LiSpeak v.", VERSION
    else:
        open_dialog()

