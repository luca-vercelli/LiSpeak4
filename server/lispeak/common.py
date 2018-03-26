# -*- coding: utf-8 -*- 
VERSION = 0.1

import gettext
gettext.textdomain('lispeak')
_ = gettext.gettext

import os

#Is this needed? It works in Linux only.
#os.environ["PATH"] = ".:" + os.environ["PATH"]

def get_template_folder():
    """
    Guess where are stored Glade templates
    """
    global HOME
    for d in ['.', os.path.join(HOME, ".local", "share"), "/usr/local/share", "/usr/share"]:
        if os.path.isdir(d):
            if os.path.exists(os.path.join(d, "lispeak", "glade")):
                return d
    return "."

def add_to_syspath(path_or_paths):
    """
    Add given path/s to sys.path (i.e. os.environ["PYTHONPATH"] )
    """
    import sys
    if isinstance(path_or_paths, basestring):
        path = path_or_paths
        sys.path.append(path)
    else:
        paths = path_or_paths
        sys.path.extend(paths)

def add_to_path(path_or_paths):
    """
    Add given path/s to os.environ["PATH"]
    """
    separator = ";" if os.name == 'nt' else ':'
    if isinstance(path_or_paths, basestring):
        path = path_or_paths
        os.environ["PATH"] = path + separator + os.environ["PATH"]
    else:
        os.environ["PATH"] = separator.join(path_or_paths) + separator + os.environ["PATH"]

def add_all_possible_paths():
    """
    Guess PATH
    This is not needed if program is properly installed
    """
    for dir in ["server", "settings", "dictionary", "speech2text"]:
        add_to_path(os.path.join(".", dir))
        add_to_path(os.path.join("..", dir))

add_all_possible_paths()

HOME = os.path.expanduser("~")                    # This works in either Windows and Linux
CONFIG_DIR = os.path.join(HOME, ".lispeak4")      # os.path.join works in either Windows and Linux
CONFIG_FILE = os.path.join(HOME, ".lispeak4", "lispeak.conf") 
CONFIG_SECTION1 = "General"
AUTOSTART_FILE = HOME + "/.config/autostart/lispeak.desktop"    # Autostart feature is Linux specific
GLADE_TEMPLATE_FOLDER = get_template_folder()
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

