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
    os.system("cp -r yay-git dumpkit")
    os.system("cp -r dumpfile dumpkit")
    print(Colors.OK + "Creating tar_file" + Colors.END)
    os.system("tar -czf dumpkit.tar dumpkit")
    os.system("rm -rf dumpkit")
    os.system("rm -rf dumpfile")
    print(Colors.OK + "Finish" + Colors.END)
def unpack_dump(argv):
    if os.path.exists("dumpkit.tar"):
        print(Colors.OK + "Untar file" + Colors.END)
        os.system("tar -xf dumpkit.tar")
        os.system("cp -r dumpkit/dump_tools/ezdump dumpkit/dump_tools/pkg_lists dumpkit/dump_tools/yay-git .")
        os.system("chmod 777 ezdump")
        os.system("./ezdump")
        os.system("rm -rf ezdump pkg_lists")
    else:
        print(Colors.FAIL + "[FAIL] no dumpkit in actual folder" + Colors.END)

if (len(argv) < 2):
    print("type : 1 to creat kit 2 to unpack kit")
    print("usage :\n ./ezdump2.py 'type' 'all file you whant to keep'")
    exit(84)

if (int(argv[1]) == 1):
    creat_directory(argv)
elif (int(argv[1]) == 2):
    unpack_dump(argv)
else:
    print("type : 1 to creat kit 2 to unpack kit")
    print("usage :\n ./ezdump2.py 'type' 'all file you whant to keep'")
