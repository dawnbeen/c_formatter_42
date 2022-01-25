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
    ptn_no_value = r"return\s*;"
    ptn_surrounded = r"return\s+?(?P<value>\(.*\))\s*;"
    ptn_paren_leaded = r"return\s+\(?(?P<value>(?=\().*)\)?\s*;"
    ptn_other = r"return\s+(?P<value>.*)\s*;"

    if re.search(ptn_no_value, content):
        return content

    if re.search(ptn_surrounded, content):
        return content

    if re.search(ptn_paren_leaded, content):
        return re.sub(
            ptn_paren_leaded,
            lambda match: "return ({});".format(match.group("value").strip()),
            content,
            re.DOTALL,
        )

    return re.sub(
        ptn_other,
        lambda match: "return ({});".format(match.group("value").strip()),
        content,
        re.DOTALL,
    )


def space_before_semi_colon(content: str) -> str:
    return re.sub(
        r"(?P<keyword>return|break|continue);",
        lambda match: match.group("keyword") + " ;",
        content,
    )


def remove_multiline_condition_space(content: str) -> str:
    return re.sub(
        r"(?P<tabs>\t+) {1,3}(?P<rest>.*)",
        lambda match: "{}\t{}".format(match.group("tabs"), match.group("rest")),
        content,
    )


def insert_void(content: str) -> str:
    return re.sub(
        r"(?P<funcdef>[0-9a-zA-Z_]*\t+[0-9a-zA-Z_]*\s*)\(\s*\)",
        lambda match: "{}({})".format(match.group("funcdef"), "void"),
        content,
    )
