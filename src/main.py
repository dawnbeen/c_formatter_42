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


import sys
import argparse

import formatters
from  formatters import *


def run_formatters(content: str) -> str:
    runned = [
        # formatters.FORMATTERS["clang_format"],
        formatters.FORMATTERS["hoist"],
        formatters.FORMATTERS["align"]
    ]
    for formatter in runned:
        content = formatter(content)
    return content


def main():
    formatters_names = formatters.FORMATTERS.keys()
    arg_parser = argparse.ArgumentParser(
        description="Align C source according to the norm",
        formatter_class=argparse.RawTextHelpFormatter
    )
    arg_parser.add_argument(
        "-i", "--confirm",
        action="store_true",
        help="Ask confirmation before overwritting any file"
    )
    arg_parser.add_argument(
        "-f", "--formatter",
        help="""\
Formatter to use, by default use all formatters
The available formatters are:
""" + " - " + "\n - ".join(formatters_names),
        choices=formatters_names
    )
    arg_parser.add_argument(
        "filepaths",
        metavar="FILE",
        nargs="*",
        help="File to align, if no file is provided read STDIN"
    )
    args = arg_parser.parse_args()

    # if args.formatter is not None:
    #     if args.formatter not in [x[0] for x in formatters.FORMATTERS]

    # print(formatters.FORMATTERS)

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
