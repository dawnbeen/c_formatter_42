# ############################################################################ #
#                                                                              #
#                                                         :::      ::::::::    #
#    run.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cacharle <me@cacharle.xyz>                 +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/10/09 18:15:09 by cacharle          #+#    #+#              #
#    Updated: 2020/10/09 20:02:49 by charles          ###   ########.fr        #
#                                                                              #
# ############################################################################ #

import re

from formatters.clang_format import clang_format
from formatters.hoist import hoist
from formatters.align import align


def parenthesize_return(content: str) -> str:
    return re.sub(
        r"return\s+(?P<value>[^(].*)\s*;",
        lambda match: "return ({});".format(match.group("value").strip()),
        content,
        re.DOTALL
    )


def space_before_semi_colon(content: str) -> str:
    return re.sub(
        r"(?P<keyword>return|break|continue);",
        lambda match: "{} ;".format(match.group("keyword")),
        content
    )


def remove_multiline_condition_space(content: str) -> str:
    return re.sub(
        r"(?P<tabs>\t+) {1,3}(?P<rest>.*)",
        lambda match: "{}\t{}".format(
            match.group("tabs"),
            match.group("rest")),
        content
    )


def run_all(content: str) -> str:
    """ Run all formatters """
    content = clang_format(content)
    content = remove_multiline_condition_space(content)
    content = parenthesize_return(content)
    content = space_before_semi_colon(content)
    content = hoist(content)
    content = align(content)
    return content

