#!/bin/env python3

# This is my attempt at figuring out how to do "plug ins".
# The notion is that I want to write an easily extensible monitoring system
# in python, and I want to be able to put code to test something in the
# plugins directory and then be able to refence it by "test_description"

import sys
import argparse
import os
from myFunction import myFunction

class Monitor:
    """ Monitor Stuff. """

    def __init__(self):
        """ Eventually replace this with commmandline options and a config file:"""
        self.plugin_dir = 'c:/cygwin64/home/Ortep/Documents/PluginExample/plugins/'
        self.plugins = {} # create a monitor level dictionary of the plugins.
        # print("this")

    def loadConfig(self):
        return NotImplmented

    def reloadPlugins(self):
        """This will call a reload on the plugins folder"""
        return 0

    def testFunct(s,myArg):
        print(myArg)

def main():
    print("Hello World")
    t = Monitor()
    myDict = {'a': t.testFunct}
    myDict['a']("Fred is a bitch")
    myFunction("seven is the loneliest number")
if __name__=='__main__': main()
