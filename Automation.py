# This is an Automation Script to update pip, brew and python all at once. 

# Importing the necessary modules
import os
import sys

#Upgrading the Brew packages
os.system("brew update")
os.system("brew upgrade")

#Updating python to the latest version
os.system("brew install python")

#Updating Pip and its packages based on the current version of python installed

#getting the python version
python_version = sys.version

#Splitting the python version into its components so that the major and minor version can be pulled. 
specific_version = python_version.split(".")

#Updating Pip using the specific version of python installed. 
os.system(f"python{specific_version[0]}.{specific_version[1]} -m pip install --upgrade pip")