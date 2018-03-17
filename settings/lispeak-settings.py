#!/usr/bin/env python2.7
# -*- coding: utf-8 -*- 
VERSION = 0.1

# Require lispeak module

from lispeak.common import *

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import gettext
gettext.textdomain('lispeak')
_ = gettext.gettext

class SettingsWindow:
    def __init__(self):
    
        glade_folder = get_glade_folder()

        self.lang_codes = {"English":"en", "Polski":"pl", "Español":"es", "Français":"fr", "Italiano":"it"}
        self.languages = self.lang_codes.keys()
        self.lang_decode = { self.lang_codes[l] : l for l in self.languages}
        self.engines = ["espeak","Google TTS","pico2wave"]
        self.userinfo = load_user_info()

        self.builder = Gtk.Builder()
        self.builder.add_from_file(glade_folder + "/settings.glade")
        self.builder.connect_signals(self)

        self.window = self.builder.get_object("window1")
        self.aboutDialog = self.builder.get_object("aboutDialog")
        self.addItems(self.builder.get_object("cmbEngine"), self.engines)
        self.addItems(self.builder.get_object("cmbLang"), self.languages)
        self.fillFields()
        self.window.show_all()

    def onClose(self, *args):
        Gtk.main_quit(args)
        #TODO run lispeak? or not?

    def onSwitchSpeakResponse(self, widget, enabled):
        self.userinfo['tts'] = str(enabled)
        save_user_info(self.userinfo)

    def onSwitchAutostart(self, widget, enabled):
        self.userinfo['autostart'] = str(enabled)
        enable_autostart(enabled)
        save_user_info(self.userinfo)

    def onLanguageChange(self, widget):
        self.userinfo['lang'] = self.lang_codes[widget.get_active_text()]
        save_user_info(self.userinfo)

    def onEngineChange(self, widget):
        self.userinfo['ttsengine'] = widget.get_active_text()
        save_user_info(self.userinfo)

    def openAbout(self,widget):
        self.aboutDialog.set_transient_for(self.builder.get_object("window1"))
        #FIXME image is blank
        response = self.aboutDialog.run()
        if response == Gtk.ResponseType.DELETE_EVENT or response == Gtk.ResponseType.CANCEL:
            self.aboutDialog.hide()

    def dialogBtnPressed(self,*args):
        print args

    def set_combo_active_text(self,combo, text):
        model = combo.get_model()
        for i in range(len(model)):
            if model[i][0] == text:
                combo.set_active(i)

    def addItems(self, obj, items):
        for e in items:
            obj.append_text(e)

    def fillFields(self):
        user_info = self.userinfo
        if "autostart" in user_info:
            self.builder.get_object("switchAutostart").set_active(user_info["autostart"] == "True")
        if "tts" in user_info:
            self.builder.get_object("switchTTS").set_active(user_info["tts"] == "True")
        if "ttsengine" in user_info:
            self.set_combo_active_text(self.builder.get_object("cmbEngine"), user_info["ttsengine"])
        else:
            self.builder.get_object("cmbEngine").set_active(0)
        if "lang" in user_info:
            try:
                self.set_combo_active_text(self.builder.get_object("cmbLang"), self.lang_decode[user_info["lang"]])
            except KeyError: # wrong or unsupported language
                self.builder.get_object("cmbLang").set_active(0)
        else:
            self.builder.get_object("cmbLang").set_active(0)


def open_dialog():
    app = SettingsWindow()
    Gtk.main()
    #FIXME if there is any exception, the Gtk windows close however the program remains alive...

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description=_('LiSpeak - Linux Voice Command And Control System - Settings panel'))
    parser.add_argument("--version",dest='version',action='store_true',default=False,help=_('Show version and exit'))
    args = parser.parse_args()
    if args.version:
        print "LiSpeak v.", VERSION
    else:
        open_dialog()

