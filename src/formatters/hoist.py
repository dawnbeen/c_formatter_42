# ############################################################################ #
#                                                                              #
#                                                         :::      ::::::::    #
#    hoist.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cacharle <me@cacharle.xyz>                 +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/10/04 11:16:28 by cacharle          #+#    #+#              #
#    Updated: 2020/10/04 11:28:36 by cacharle         ###   ########.fr        #
#                                                                              #
# ############################################################################ #

import re

from formatters import formatter


def split_assignment(content: str) -> str:
    lines = []
    for line in content.split("\n"):
        m = re.match(r"^(?P<type>[a-z]*) (?P<name>[a-z]*) = (?P<value>..*);$", line)
        if m is not None:
            lines.append("{} {};".format(m.group("type"), m.group("name")))
            lines.append("{} = {};".format(m.group("name"), m.group("value")))
        else:
            lines.append(line)
    return "\n".join(lines)

@formatter
def hoist(content: str) -> str:
    return split_assignment(content)

