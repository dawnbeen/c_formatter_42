# ############################################################################ #
#                                                                              #
#                                                         :::      ::::::::    #
#    hoist.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cacharle <me@cacharle.xyz>                 +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/10/04 11:16:28 by cacharle          #+#    #+#              #
#    Updated: 2020/10/04 12:34:19 by cacharle         ###   ########.fr        #
#                                                                              #
# ############################################################################ #

import re

from formatters import formatter
import formatters.helper as helper


@formatter
@helper.local_scope
def hoist(content: str) -> str:
    input_lines = content.split("\n")

    # split assignment
    for line in input_lines:
        m = re.match(r"^(?P<type>[a-z]*) (?P<name>[a-z]*) = (?P<value>..*);$", line)
        if m is not None:
            lines.append("{} {};".format(m.group("type"), m.group("name")))
            lines.append("{} = {};".format(m.group("name"), m.group("value")))
        else:
            lines.append(line)


    # for line in input_lines:
    #     m = re.match(r"^(?P<type>[a-z]*) (?P<name>[a-z]*);$", line)
    #     if m is not None:
