#!/usr/bin/env python3

# ############################################################################ #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cacharle <me@cacharle.xyz>                 +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/10/04 09:53:21 by cacharle          #+#    #+#              #
#    Updated: 2020/10/04 09:53:21 by cacharle         ###   ########.fr        #
#                                                                              #
# ############################################################################ #

import re
import os
import sys
import shutil
import argparse
import textwrap

from formatters.clang_format import clang_format
from formatters.hoist import hoist
from formatters.align import align


def append_to_path(home_dir, repo_dir, rc_file):
    """ Append the repo directory to a rc_file path variable """
    try:
        rc_path = os.path.join(home_dir, rc_file)
        already_installed = False
        with open(rc_path, "r") as file:
            if file.read().find("Added by c_formatter_42") != -1:
                already_installed = True
        if not already_installed:
            with open(rc_path, "a") as file:
                file.write(textwrap.dedent("""
                    # Added by c_formatter_42
                    export PATH="$PATH:{}"
                    """.format(repo_dir)
                ))
    except OSError as e:
        print("Error: Couldn't append to PATH: {}: {}".format(e.filename, e.strerror))


def run_formatters(content: str) -> str:
    """ Run all formatters """
    content = clang_format(content)
    content = re.sub(
        "return (?P<value>[^(].*);",
        lambda match: "return ({});".format(match.group("value")),
        content,
        re.DOTALL
    )
    content = hoist(content)
    content = align(content)
    return content


def main():
    arg_parser = argparse.ArgumentParser(
        description="Format C source according to the norm",
        formatter_class=argparse.RawTextHelpFormatter
    )
    arg_parser.add_argument(
        "-c", "--confirm",
        action="store_true",
        help="Ask confirmation before overwritting any file"
    )
    arg_parser.add_argument(
        "-i", "--install",
        action="store_true",
        help=textwrap.dedent("""\
            Copy the .clang-format in your home (required by clang-format).
            Add c_formatter_42 to your PATH in your .zshrc and .bashrc""")
    )
    arg_parser.add_argument(
        "filepaths",
        metavar="FILE",
        nargs="*",
        help="File to format, if no file is provided read STDIN"
    )
    args = arg_parser.parse_args()

    if args.install:
        home_dir = os.environ.get("HOME")
        if home_dir is None:
            print("HOME environment variable not set")
            sys.exit(1)
        repo_dir = os.path.realpath(os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            ".."
        ))
        append_to_path(home_dir, repo_dir, ".zshrc")
        append_to_path(home_dir, repo_dir, ".bashrc")
        # Copy .clang-format in user's home directory
        home_clang_file = os.path.join(home_dir, ".clang-format")
        if not os.path.exists(home_clang_file):
            shutil.copyfile(os.path.join(repo_dir, ".clang-format"), home_clang_file)
        sys.exit(0)

    if len(args.filepaths) == 0:
        content = sys.stdin.read()
        print(run_formatters(content), end="")
    else:
        for filepath in args.filepaths:
            try:
                with open(filepath, "r") as file:
                    content = file.read()
                if args.confirm:
                    result = input("Are you sure you want to overwrite {}?[y/N]"
                                   .format(filepath))
                    if result != "y":
                        continue
                print("Writting to {}".format(filepath))
                with open(filepath, "w") as file:
                    file.write(run_formatters(content))
            except OSError as e:
                print("Error: {}: {}".format(e.filename, e.strerror))


if __name__ == "__main__":
    main()
