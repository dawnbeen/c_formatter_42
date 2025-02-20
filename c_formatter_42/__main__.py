#!/usr/bin/env python3

# ############################################################################ #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cacharle <me@cacharle.xyz>                 +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/10/04 09:53:21 by cacharle          #+#    #+#              #
#    Updated: 2020/10/04 09:53:21 by zouddach         ###   ########.fr        #
#                                                                              #
# ############################################################################ #

import argparse
import os
import sys
from pathlib import Path
from typing import List, Optional

from c_formatter_42.run import run_all


def process_file(filepath: Path, confirm: bool = False) -> bool:
    """Process a single file with formatting."""
    try:
        with filepath.open("r") as file:
            content = file.read()

        if confirm:
            result = input(f"Are you sure you want to overwrite {filepath}?[y/N] ")
            if result != "y":
                return True

        print(f"Formatting: {filepath}")
        with filepath.open("w") as file:
            file.write(run_all(content))
        return True
    except OSError as e:
        print(f"Error: {e.filename}: {e.strerror}", file=sys.stderr)
        return False


def process_path(
    path: Path, confirm: bool = False, ignore_dirs: Optional[List[str]] = None
) -> bool:
    """
    Process a path (file or directory) recursively.
    Formats .c and .h files in the directory.
    """
    ignore_dirs = ignore_dirs or []

    if path.is_file():
        if path.suffix in (".c", ".h"):
            return process_file(path, confirm)
        return True

    if path.is_dir():
        success = True
        for root, dirs, files in os.walk(path):
            dirs[:] = [
                d
                for d in dirs
                if not any(
                    str(Path(root) / d).find(ignore_dir) != -1
                    for ignore_dir in ignore_dirs
                )
            ]

            for file in files:
                if file.endswith((".c", ".h")):
                    filepath = Path(root) / file
                    success &= process_file(filepath, confirm)
        return success

    print(f"Error: {path} is not a file or directory", file=sys.stderr)
    return False


def main() -> int:
    arg_parser = argparse.ArgumentParser(
        prog="c_formatter_42",
        description="Format C source files according to the norm",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    arg_parser.add_argument(
        "-c",
        "--confirm",
        action="store_true",
        help="Ask confirmation before overwriting any file",
    )
    arg_parser.add_argument(
        "-i",
        "--ignore",
        nargs="+",
        default=[],
        help="Ignore specified folders (e.g. .git/ .vscode/)",
    )
    arg_parser.add_argument(
        "paths",
        metavar="PATH",
        nargs="*",
        help="Files or directories to format. If no path is provided, read STDIN",
    )
    args = arg_parser.parse_args()

    if len(args.paths) == 0:
        content = sys.stdin.read()
        print(run_all(content), end="")
        return 0

    success = True
    for path in args.paths:
        success &= process_path(Path(path), args.confirm, args.ignore)

    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
