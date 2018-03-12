#!/usr/bin/env python2.7
# -*- coding: utf-8 -*- 

from common import *

SPEECH2TEXT = "speech2text"
DICTIONARY = "dictionary"
DICT_PREFIX = "dictionary/modes/it"        #FIXME

running = False
userinfo = None
speech2text_pid = None
mode = DEFAULT_MODE


def start_speech2text_service():
    """
    Start speech2text daemon, using current language
    @return out,err streams
    """
    global userinfo, speech2text_pid
    if speech2text_pid is not None:
        print "Something's wrong. speech2text_pid = ", speech2text_pid
        return
    import subprocess
    p = subprocess.Popen([SPEECH2TEXT, "-l", userinfo.lang], stdout=PIPE)
    speech2text_pid = p.pid
    return p.stdout, p.stderr

def stop_speech2text_service():
    """
    Kill speech2text daemon
    """
    global speech2text_pid
    import os
    os.kill(speech2text_pid)
    speech2text_pid = None

def run_dictionary(text_line):
    """
    Execute dictionary, using current language and mode
    @return output
    """
    global userinfo
    import subprocess, os
    dic_file = os.path.join([DICT_PREFIX, userinfo.lang, get_current_mode(), ".dic"])
    return subprocess.check_output([DICTIONARY, text_line, dic_file])

def execute_final_command(command):
    """
    This is quite bad... execute almost anything...
    @return out,err streams
    """
    import subprocess
    return subprocess.check_output(command)

def start():
    global running
    if running:
        print "LiSpeak server already running"
        return
        
    running = True
    
    set_current_mode()
    
    userinfo = load_user_info()
    
    while true:
        out, err = start_speech2text()
        
        while out is not None:
            command = run_dictionary(otu)
            execute_final_command(command)
            
            # Has the final command modified current mode?
            oldmode = mode
            mode = get_current_mode()
            if mode != oldmode:
                stop_speech2text_service()
                start_speech2text_service()
                

	
