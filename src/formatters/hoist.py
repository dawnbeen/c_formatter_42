# ############################################################################ #
#                                                                              #
#                                                         :::      ::::::::    #
#    hoist.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cacharle <me@cacharle.xyz>                 +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/10/04 11:16:28 by cacharle          #+#    #+#              #
#    Updated: 2020/10/04 14:06:04 by cacharle         ###   ########.fr        #
#                                                                              #
# ############################################################################ #

import re

from formatters import formatter
import formatters.helper as helper
import formatters.regex as regex


@formatter
@helper.local_scope
def hoist(content: str) -> str:
    input_lines = content.split("\n")

    lines = []
    # split assignment
    for line in input_lines:
        m = re.match(
            r"^(?P<indent>\s+)"
            r"(?P<type>{t})\s+"
            r"(?P<name>{n})\s+=\s+"
            r"(?P<value>.+);$"
                .format(t=regex.TYPE, n=regex.NAME),
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
    declarations = [line for line in lines
                    if re.match(r"^\s*[a-z]*\s+[a-z]*;$", line) is not None]
    lines = declarations + [line for line in lines if line not in declarations]

    return "\n".join(lines)
