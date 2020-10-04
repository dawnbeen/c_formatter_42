# ############################################################################ #
#                                                                              #
#                                                         :::      ::::::::    #
#    hoist.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cacharle <me@cacharle.xyz>                 +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/10/04 11:16:28 by cacharle          #+#    #+#              #
#    Updated: 2020/10/04 15:23:04 by cacharle         ###   ########.fr        #
#                                                                              #
# ############################################################################ #

import re

import formatters.helper as helper
import formatters.regex as regex


@helper.local_scope
def hoist(content: str) -> str:
    input_lines = content.split("\n")

    lines = []
    # split assignment
    for line in input_lines:
        m = re.match(
            r"^(?P<indent>\s+)"
            r"(?P<type>{t})\s+"
            r"(?P<name>{d})\s+=\s+"
            r"(?P<value>.+);$"
            .format(t=regex.TYPE, d=regex.DECL_NAME),
            line
        )
        if m is not None:
            lines.append("\t{}\t{};".format(
                m.group("type"),
                m.group("name"))
            )
            lines.append("{}{} = {};".format(
                m.group("indent"),
                m.group("name"),
                m.group("value"))
            )
        else:
            lines.append(line)

    # hoist declarations
    decl_regex = r"^\s*{t}\s+{d};$".format(t=regex.TYPE, d=regex.DECL_NAME)
    declarations = [line for line in lines
                    if re.match(decl_regex, line) is not None]
    lines = (
        declarations
        + [""]
        + [line for line in lines
           if line not in declarations and line != ""]
    )

    return "\n".join(lines)
