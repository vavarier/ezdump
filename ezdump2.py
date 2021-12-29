#!/bin/python3
import os
from sys import *

def creat_directory(argv):
    os.system("echo test");
def unpack_dump(argv):
    a = 0
if (len(argv) < 2):
    a = 0
    #print usage
if (int(argv[1]) == 1):
    creat_directory(argv)
elif (int(argv[1]) == 2):
    unpack_dump(argv)
else:
    a = 0
    #print usage
