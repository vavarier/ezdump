#!/bin/python3
import os
from sys import *
import fileinput
class Colors:
    OK = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'

def already_there():
    print(Colors.WARNING + "There is already a kit are you sure you wanna creat new one ? [o,n]" + Colors.END);
    for line in stdin:
        if(line.rstrip() == 'o'):
            os.system("rm -rf dumpkit")
            break
        if (line.rstrip() == 'n'):
            exit (1)
        else:
            print(Colors.FAIL + "Wrong input" + Colors.END)
def creat_directory(argv):
    i = 2
    wait = 0;
    if os.path.exists("dumpkit"):
        already_there()
    os.system("mkdir dumpkit")
    os.system("mkdir dumpfile")
    while (i < len(argv)):
        os.system("cp -r " + argv[i] + " ./dumpfile");
        i += 1
    print(Colors.OK + "Copying dump_tools and files in kit" + Colors.END)
    os.system("cp -r dump_tools dumpkit")
    os.system("cp -r dumpfile dumpkit")
    print(Colors.OK + "Creating tar_file" + Colors.END)
    os.system("tar -czf dumpkit.tar dumpkit")
    os.system("rm -rf dumpkit")
    os.system("rm -rf dumpfile")
    print(Colors.OK + "Finish" + Colors.END)
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
