#!/usr/bin/env python2.7
# -*- coding: utf-8 -*- 

from lispeak.common import *

import gettext
gettext.textdomain('lispeak')
_ = gettext.gettext

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description=_('LiSpeak - Linux Voice Command And Control System - Settings panel'))
    parser.add_argument("--version", dest='version', action='store_true', default=False, help=_('Show version and exit'))
    args = parser.parse_args()
    if args.version:
        print "LiSpeak v.", VERSION
    else:
        from lispeak import server
        server.start()
