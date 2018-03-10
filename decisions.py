#!/usr/bin/env python3
"""
________________________________________________________________________

:PROJECT: simple_installer

*A simple user decision function library*

:details: This is a simple decision function library for asking user 
          descisions:
         - yes / no queries
         - text queries
         - simple help
         - default, predefined answers

:file:    decisions.py

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

import sys
import logging
from distutils.util import strtobool

__version__ = "0.0.1"

def query_yes_no(question, default_answer="yes", help=""):
    """Ask user at stdin a yes or no question
    
    :param question: question text to user
    :param default_answer: should be "yes" or "no"
    :param help: help text string
    :return:  :type: bool
    """
    if default_answer == "yes":
        prompt_txt = "{question} [Y/n] ".format(question=question)
    elif default_answer == "no" : # explicit no
        prompt_txt = "{question} [y/N] ".format(question=question)
    else:
        raise ValueError("default_answer must be 'yes' or 'no'!")

    while True:
        try:
            answer = input(prompt_txt)
            if answer:
                if answer=="?":
                    print(help)
                    continue
                else:
                    return strtobool(answer)
            else :
                return strtobool(default_answer)
        except ValueError:
            sys.stderr.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")
        except KeyboardInterrupt:
            logging.error("Query interrupted by user, exiting now ...")
            exit(0)

def query(question, default_answer="", help=""):
    """Ask user a question
    
    :param question: question text to user
    :param default_answer: any default answering text string
    :param help:  help text string
    :return: stripped answer string
    """
    prompt_txt = "{question} [{default_answer}] ".format(question=question, default_answer=default_answer)

    while True:
        answer = input(prompt_txt).strip()
        
        if answer :
            if answer=="?":
                print(help)
                continue
            else :
                return answer
        else :
            return default_answer


if __name__=="__main__":
    """simple usage and testing routine """

    answer_txt = query("What do you like ?", default_answer="Spam", help="HELP: Here you can say, what you like")

    answer_bool = query_yes_no("Do you really like |{0}| ?".format(answer_txt), help="HELP: Here you can confirm, what you like")

    if answer_bool:
        sys.stdout.write("Indeed, she really likes |{0}| !\n".format(answer_txt))
    else:
        sys.stdout.write("Well, what a pitty. She does not like {0} !\n".format(answer_txt))

    if query_yes_no("Anything else ?", default_answer="no"):
        answer_txt = query("What else do you like ?", default_answer="Eggs")

        sys.stdout.write("I will also get some |{0}| for you !\n".format(answer_txt))
    else:
        sys.stdout.write("You are welcome !\n")

