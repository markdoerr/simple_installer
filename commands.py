#!/usr/bin/env python3
"""
________________________________________________________________________

:PROJECT: simple_installer

*A simpified system command caller based on subprocess*

:details: commands simplifies the call of system commands by providing 
          conveniance functions:
              - simple system command calling module

:file:    commands.py

:author:  mark doerr (mark@ismeralda.org) : 

:version: 0.0.1
:date: (creation)          20180310
:date: (last modification) 20180310

.. note:: some remarks 
.. todo:: - 
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

import subprocess
import logging

def call(command=""):
    ''' Convenient command call: it splits the command string into tokens (default separator: space)
    
    :param command: the command to be executed by the system
    '''
    try:
        cmd_lst = command.split()
        
        subprocess.run(cmd_lst, check=True)
    except subprocess.CalledProcessError as err:
        logging.error('ERROR:', err)
        
        
def run(command="", parameters=[]):
    '''This version is closer to the subprocess version
    
    :param command: the command to be executed by the system
    :param parameters: parameters of the this command
    '''
    try:
        subprocess.run([command]+parameters, check=True, shell=True)  #stdout=subprocess.PIPE
    except subprocess.CalledProcessError as err:
        logging.error('ERROR:', err)
    
