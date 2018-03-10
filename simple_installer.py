#!/usr/bin/env python3
"""
________________________________________________________________________

:PROJECT: simple_installer

*A simple text based python application installer*

:details: This is a simple text based installer for python applications:
         - simple decision module
         - simple system command calling module
         - argparsing for command line options

:file:    simple_installer.py

:author:  mark doerr (mark@ismeralda.org) : 


:date: (creation)          20180310
:date: (last modification) 20180310

.. note:: some remarks 
.. todo:: - OS/platform handling

________________________________________________________________________

**Copyright**:
  This program is free software; you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation; either version 2 of the License, or
  (at your option) any later version.

  This file is provided "AS IS" with NO WARRANTY OF ANY KIND,
  INCLUDING THE WARRANTIES OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.

  For further Information see COPYING file that comes with this distribution.
________________________________________________________________________
"""

__version__ = "0.0.1"

import os
import sys
import platform
import argparse
import logging

from decisions import query_yes_no
import commands as cmd

def install_linux_app(application_name):
    logging.info("Installing {application_name} ...".format(application_name=application_name))
        
    cmd.call("ls")
    cmd.call("ls -1t")
    cmd.call("ls -A -l")
    
    cmd.run("ls",["-l","-A", "-t"])
    cmd.run("ps -Al | head ")
    cmd.run("ls -Al | grep command")
        
if __name__ == "__main__":
    """This is a small demo installer """
    logging.basicConfig(format='%(levelname)s| %(module)s.%(funcName)s:%(message)s', level=logging.DEBUG)
    #~ logging.basicConfig(format='%(levelname)s| %(module)s.%(funcName)s:%(message)s', level=logging.ERROR)
    
    application_name = "simple"
    platform_info = {}
    
    welcome_txt = "Simple installer\nInstall {application_name} now ?".format(application_name=application_name)
    
    parser = argparse.ArgumentParser(description="A simple text based installer framework for python")

    parser.add_argument('-g','--gui', action='store_true', help='activate installer with graphical user interface mode')
    parser.add_argument('-v','--version', action='version', version='%(prog)s ' + __version__)
        
    parsed_args = parser.parse_args()
    
    if (parsed_args.gui) :
        logging.info("trying to open installer GUI ....")
        logging.error("sorry, no GUI installed, exiting now ...")
        exit(0)
                
    if (not (parsed_args.gui) ):
        logging.info("text mode installation")
        
        # gathering information about the system - this might be interesting for more complex installations
        
        platform_info["os_type"] = os.name
        platform_info["os"] = platform.system()
        platform_info["os_release"] = platform.release()
        
        logging.info( platform_info["os_type"])  # returns os name in simple form - could be replaced by platform ....
        logging.info(platform_info["os"]) #returns the base system, in your case Linux
        logging.info(platform.release()) #returns release version
        
        if query_yes_no(welcome_txt, help="HELP: shall I start the installation now ?"):
            if platform.system() == "Linux":
                install_linux_app(application_name)
            else:
                logging.info("Please use a Linux operation system")
            
        else:
            logging.info("Have a nice day ... ;)")
    
