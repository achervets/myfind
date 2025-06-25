#!/usr/bin/env python3

import os, argparse, re

def main():
    args = argument_parser()
    file_list = file_search(args)
    if not file_list:
        print("File Not Found")
    else:
        for file in file_list:
            print(file)

# parses arguments
def argument_parser():
    parser = argparse.ArgumentParser(description="this script performs basic find functions on local filesystem")
    parser.add_argument("--name", default="", help="the name of the file you are searching for (not absolute)")
    parser.add_argument("--dir", default=".", help="absolute directory to search in (default cwd)")
    parser.add_argument("-a", action="store_false")
    parser.add_argument("-r", action="store_false")
    parser.add_argument("-f", action="store_false")
    return parser.parse_args()

# searches filesystem using os.walk()
def file_search(args):
    file_list = []
    if args.name == "":
        return file_list
    regex_pattern = "^" + re.escape(args.name).replace(r"\*", ".*").replace(r"\?", ".") + "$"
    dir = os.path.abspath(args.dir)
    for dirpath, dirnames, filenames in os.walk(dir):
        # modifies the directory list in place to not include hidden directories
        if args.a:
            dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        for name in filenames:
            if re.match(regex_pattern, name):
                if args.f:
                    file_list.append(os.path.join(dirpath, name))
                else:
                    file_list.append(name)
            if args.r:
                return file_list
    return file_list



if __name__ == "__main__":
    main()