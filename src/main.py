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
import sys
import argparse

from formatters.clang_format import clang_format
from formatters.hoist import hoist
from formatters.align import align


def run_formatters(content: str) -> str:
    content = clang_format(content)
    content = re.sub(
        "return (?P<value>[^(].*);",
        lambda match: "return ({});".format(match.group("value")),
        content
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
        "-i", "--confirm",
        action="store_true",
        help="Ask confirmation before overwritting any file"
    )
    arg_parser.add_argument(
        "filepaths",
        metavar="FILE",
        nargs="*",
        help="File to format, if no file is provided read STDIN"
    )
    args = arg_parser.parse_args()

    # clang_format_config_path = os.path.join(os.environ["HOME"], ".clang-format")
    # if not os.path.exists(clang_format_config_path):
    #     shutil.copyfile(".clang-format", clang_format_config_path)

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
