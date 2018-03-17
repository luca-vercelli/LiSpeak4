#!/usr/bin/env python2.7
# -*- coding: utf-8 -*- 
VERSION = 0.1

import gettext
gettext.textdomain('lispeak')
_ = gettext.gettext

import os

#FIXME  paths should be set up by make, don't?
 
HOME = os.path.expanduser("~")                    # This works in either Windows and Linux
CONFIG_FILE = os.path.join(HOME, ".lispeak4")    # This works in either Windows and Linux
CONFIG_SECTION1 = "General"
AUTOSTART_FILE = HOME + "/.config/autostart/lispeak.desktop"    # Autostart feature is Linux specific
GLADE_TEMPLATE_LOCATION=['.', '~/.local/share/lispeak/glade', '/usr/local/share/lispeak/glade', '/usr/share/lispeak/glade']    # "." works in Windows, too.
MODE_FILE = "/var/run/lispeak/mode"                                # This path is Linux specific...
DEFAULT_MODE = "main"

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

def get_current_mode():
    """
    Read current mode from MODE_FILE
    """
    with open(MODE_FILE, 'r') as mode_file:
        mode = mode_file.read().replace('\n', '')
    return mode

def set_current_mode(mode = DEFAULT_MODE):
    """
    Write current mode to MODE_FILE
    """
    with open(MODE_FILE, 'w') as mode_file:
        mode_file.write(mode)

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

