# base.py
# developer: @eggins

# This gives you a basic understanding of how I set all my new projects up.
# Everything here is what I would use as a base to any python project.

# initialise all libraries that are needed
import time, json, requests, random, colorama, threading
from time import sleep
from colorama import init
init()

# custom coded libraries
from classes.logger import logger
log = logger().log

# if you plan on using this script, please dont delete the below line
log("[@eggins] PyBase initalised. (github.com/eggins/pybase)", "info")
# if you plan on using this script, please dont delete the above line

# the below functions are all of the colours that are able to be used
# from within the logger functions
log("-------")
log("Success message.", "success")
log("Error message.", "error")
log("Info message.", "info")
log("Debug message.", "debug")
log("Yellow message.", "yellow")
log("LightGray message.", "lightgray")
log("LightPurple message.", "lightpurple")
log("-------")