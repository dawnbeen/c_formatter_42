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

from c_formatter_42.run import run_all


def main():
    arg_parser = argparse.ArgumentParser(
        prog="c_formatter_42",
        description="Format C source according to the norm",
        formatter_class=argparse.RawTextHelpFormatter
    )
    arg_parser.add_argument(
        "-c", "--confirm",
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

    if len(args.filepaths) == 0:
        content = sys.stdin.read()
        print(run_all(content), end="")
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
                    file.write(run_all(content))
            except OSError as e:
                print("Error: {}: {}".format(e.filename, e.strerror))


if __name__ == "__main__":
    main()
