#!/usr/bin/env python3

import os, sys, argparse

def main():
    '''
    if len(sys.argv) > 1:
        print("Hello, " + sys.argv[1] + " World!")
    else:
        print("Hello World!")
    '''
    file_search(sys.argv[1])

def file_search(target):
    cwd = os.getcwd()
    for dirpath, dirnames, filenames in os.walk(cwd):
        if target in filenames:
            print(os.path.join(dirpath, target))



if __name__ == "__main__":
    main()