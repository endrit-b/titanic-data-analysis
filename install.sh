#! /usr/bin/env bash

echo "Testing whether virtualenv is installed..."
# test whether virtualenv is installed
ve=`command -v virtualenv`
if [ -z "$ve" ]; then
   echo "You need to install virtualenv?"
   echo -e "Install virtualenv? [y/n] \c "
   read word
   if [ $word == "y" ]; then
      echo "This will install virtualenv in your home directory"
      if [ "$(whoami)" != "root" ]; then
         echo "You need root access"
         exit 1
      fi
      echo "Installing virtualenv..."
      currdir=`pwd`
      cd $HOME
      echo `curl -O https://pypi.python.org/packages/source/v/virtualenv/virtualenv-1.10.1.tar.gz`
      echo `tar xvfz virtualenv-1.10.1.tar.gz`
      cd virtualenv-1.10.1
      echo `python3 setup.py install`
      cd $currdir
   fi
fi
# start virtual env and install flask
echo `virtualenv -p python3 venv`
currentDir=`pwd`
virtualenvPath='venv/bin/activate'
source $currentDir/$virtualenvPath 

pip install -r requirements.txt
echo "Installation complete."
