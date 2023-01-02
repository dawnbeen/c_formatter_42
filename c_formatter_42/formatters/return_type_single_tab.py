# ############################################################################ #
#                                                                              #
#                                                         :::      ::::::::    #
#    return_type_single_tab.py                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: charles <me@cacharle.xyz>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/01/09 10:28:30 by charles           #+#    #+#              #
#    Updated: 2022/01/09 10:28:30 by charles          ###   ########.fr        #
#                                                                              #
# ############################################################################ #


import re

from c_formatter_42.formatters import helper


def return_type_single_tab(content: str) -> str:
    lines = content.split("\n")
    aligned = []
    align_regex = r"^(?P<prefix>{type})\s+" r"(?P<suffix>{name}\(.*\)?[^;])$"
    align_regex = align_regex.format(
        type=helper.REGEX_TYPE, name=helper.REGEX_NAME, decl=helper.REGEX_DECL_NAME
    )
    matches = [re.match(align_regex, line) for line in lines]
    aligned = [
        (i, match.group("prefix"), match.group("suffix"))
        for i, match in enumerate(matches)
        if match is not None
        and match.group("prefix") not in ["struct", "union", "enum"]
    ]
    for i, prefix, suffix in aligned:
        lines[i] = f"{prefix}\t{suffix}"
    return "\n".join(lines)
