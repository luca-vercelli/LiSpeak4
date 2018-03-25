# -*- coding: utf-8 -*- 
VERSION = 0.1

import gettext
gettext.textdomain('lispeak')
_ = gettext.gettext

import os

#Is this needed? It works in Linux only.
os.environ["PATH"] = ".:" + os.environ["PATH"]

def get_template_folder():
    global HOME
    for d in ['.', os.path.join(HOME, ".local", "share"), "/usr/local/share", "/usr/share"]:
        if os.isdir(d):
            if os.exists(os.path.join(d, x)):
                return d
    return "."

HOME = os.path.expanduser("~")                    # This works in either Windows and Linux
CONFIG_DIR = os.path.join(HOME, ".lispeak4")      # os.path.join works in either Windows and Linux
CONFIG_FILE = os.path.join(HOME, ".lispeak4", "lispeak.conf") 
CONFIG_SECTION1 = "General"
AUTOSTART_FILE = HOME + "/.config/autostart/lispeak.desktop"    # Autostart feature is Linux specific
GLADE_TEMPLATE_FOLDER = findshare('/lispeak/glade')
MODE_FILE = os.path.join(HOME, ".lispeak4", "mode")
DEFAULT_MODE = "main"
SPEECH2TEXT = "speech2text"
DICTIONARY = "dictionary"
SETTINGS_BIN = "lispeak-settings"
LISPEAK_BIN = "lispeak"

#Setup CONFIG_DIR
if os.path.exists(CONFIG_DIR) and not os.path.isdir(CONFIG_DIR):
    os.remove(CONFIG_DIR)
if not os.path.exists(CONFIG_DIR):
    os.makedirs(CONFIG_DIR)

import locale
USER_INFO_DEFAULTS = {
        "autostart" : "False",
        "lang"      : locale.getdefaultlocale()[0][1:2],
        "tts"       : "False",
        "operator"  : _("Operator"),
        }

def load_user_info():
    """
    Load user info from configuration file
    @return dict
    """
    import ConfigParser
    global USER_INFO_DEFAULTS
    config = ConfigParser.ConfigParser(USER_INFO_DEFAULTS)
    try:
        config.read(CONFIG_FILE)
        return dict(config.items(CONFIG_SECTION1))
    except:
        return dict(USER_INFO_DEFAULTS)

def save_user_info(user_info_dict):
    """
    Write user info to configuration file
    """
    import ConfigParser
    global USER_INFO_DEFAULTS
    user_info_complete = dict()
    user_info_complete.update(USER_INFO_DEFAULTS)
    user_info_complete.update(user_info_dict)
    config = ConfigParser.RawConfigParser()
    config.add_section(CONFIG_SECTION1)
    for key, value in user_info_complete.iteritems():
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

def enable_autostart(enable=True):
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
Exec="""+LISPEAK_BIN+"""
Terminal=false
Type=Application
Categories=Application;
""")
    else:
        import os
        if os.path.isfile(AUTOSTART_FILE):
            os.remove(AUTOSTART_FILE)

