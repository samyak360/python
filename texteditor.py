import sys
import os
import pyglet #for background music
import shutil

def exit():
    sys.exit("text editor is closing...")

def read():
    try:
        name = input("Enter the file name: ")
        aim = open(name, "r")
        readfile = aim.read()
        print(readfile)
    except Exception as e:
        print("problem occurs : %s" % (e))


def trash():
    name = input("Enter the file name: ")
    try:
        os.unlink(name)
    except Exception as e:
        print("problem occurs : %s" % (e))


def compose():
    try:
        name = input("Enter the file name: ")
        aim = open(name, "a")
        while True:
            append = input()
            aim.write(append)
            aim.write("\n")
            if append.lower() == "menu":
                break
    except Exception as e:
        print("problem occurs : %s" % (e))


def cwd():
    try:
        print(os.getcwd())
        change = input("Change Y/N: ")
        if change.startswith("y"):
            path = input("New CWD: ")
            os.chdir(path)
    except Exception as e:
        print("problem occurs : %s" % (e))


def rename():
    try:
        name = input("Enter current file name: ")
        new = input("Enter new file name: ")
        shutil.move(name, new)
    except Exception as e:
        print("problem occurs : %s" % (e))


while True:
    print("Options: compose, read, cwd, exit, trash, rename")
    do = input("So, what are you wishing for today: ")
    if do.lower() == "compose":
        compose()
    elif do.lower() == "read":
        read()
    elif do.lower() == "trash":
        trash()
    elif do.lower() == "exit":
        exit()
    elif do.lower() == "cwd":
        cwd()
    elif do.lower() == "rename":
        rename()