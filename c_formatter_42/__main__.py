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

import argparse
import sys

from c_formatter_42.run import run_all


def main() -> int:
    arg_parser = argparse.ArgumentParser(
        prog="c_formatter_42",
        description="Format C source according to the norm",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    arg_parser.add_argument(
        "-c",
        "--confirm",
        action="store_true",
        help="Ask confirmation before overwriting any file",
    )
    arg_parser.add_argument(
        "filepaths",
        metavar="FILE",
        nargs="*",
        help="File to format inplace, if no file is provided read STDIN",
    )
    args = arg_parser.parse_args()

    if len(args.filepaths) == 0:
        content = sys.stdin.read()
        print(run_all(content), end="")
        return 0

    for filepath in args.filepaths:
        try:
            with open(filepath, "r") as file:
                content = file.read()
            if args.confirm:
                result = input(f"Are you sure you want to overwrite {filepath}?[y/N]")
                if result != "y":
                    continue
            print(f"Writing to {filepath}")
            with open(filepath, "w") as file:
                file.write(run_all(content))
        except OSError as e:
            print(f"Error: {e.filename}: {e.strerror}", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
