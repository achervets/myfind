#!/usr/bin/env python3

import os, argparse

def main():
    args = argument_parser()
    file_search(args.name)

def argument_parser():
    parser = argparse.ArgumentParser(description="this script performs basic find functions on local filesystem")
    parser.add_argument("name", help = "the name of the file you are searching for (not absolute)")
    return parser.parse_args()

# function that does the actual searching using os.walk()
def file_search(name):
    cwd = os.getcwd()
    for dirpath, dirnames, filenames in os.walk(cwd):
        if name in filenames:
            print(os.path.join(dirpath, name))



if __name__ == "__main__":
    main()