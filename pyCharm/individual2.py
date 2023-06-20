#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import argparse


def tree(directory, max_depth, dir_only, file_ext):
    print_directory(directory, max_depth, dir_only, file_ext, 0)


def print_directory(directory, max_depth, dir_only, file_ext, depth):
    if depth > max_depth:
        return

    prefix = "|   " * depth
    entries = os.scandir(directory)

    for entry in sorted(entries, key=lambda e: e.name):
        if entry.is_dir() and not entry.is_symlink():
            print(prefix + "|-- " + entry.name)
            if not dir_only:
                print_directory(entry.path, max_depth, dir_only, file_ext, depth + 1)
        elif not dir_only and entry.is_file():
            if not file_ext or entry.name.endswith(file_ext):
                print(prefix + "|-- " + entry.name)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analog of the 'tree' utility in Linux.")
    parser.add_argument("directory", nargs="?", default=".", help="Target directory (default: current directory)")
    parser.add_argument("--level", type=int, default=float("inf"), help="Maximum depth of tree traversal")
    parser.add_argument("--dir-only", action="store_true", help="Display directories only")
    parser.add_argument("--file-ext", help="Filter files by extension")

    args = parser.parse_args()

    directory = args.directory
    max_depth = args.level
    dir_only = args.dir_only
    file_ext = args.file_ext

    tree(directory, max_depth, dir_only, file_ext)
