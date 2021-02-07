# ############################################################################ #
#                                                                              #
#                                                         :::      ::::::::    #
#    misc.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: charles <me@cacharle.xyz>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/02/07 14:39:26 by charles           #+#    #+#              #
#    Updated: 2021/02/07 21:16:03 by charles          ###   ########.fr        #
#                                                                              #
# ############################################################################ #

import re


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
        lambda match: match.group("keyword") + " ;",
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
