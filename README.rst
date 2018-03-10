simple_installer
================

A simple text based python application installer 

It contains
    - a simple user decision parser for yes-no and text queries
    - a simple system command interface to the mighty subprocess module
    

Project documentation
----------------------

Building the documentation (html)


first build the API documentation::

  cd docs
  sphinx-apidoc -o . ..

then generate the documents::

  make html
  
find the generated html documentation in docs/_build/html


setting sphinx up
__________________

!! remember to activate autodoc, todos and makefile creation::

  cd docs
  sphinx-quickstart





