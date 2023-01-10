# ############################################################################ #
#                                                                              #
#                                                         :::      ::::::::    #
#    preprocessor_directive.py                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: charles <me@cacharle.xyz>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/02/07 15:40:37 by charles           #+#    #+#              #
#    Updated: 2021/02/07 16:21:25 by charles          ###   ########.fr        #
#                                                                              #
# ############################################################################ #

import re


def preprocessor_directive(content: str) -> str:
    lines = content.split("\n")

    directive_regex = r"^\#\s*(?P<name>[a-z]+)\s?(?P<rest>.*)$"
    matches = [re.match(directive_regex, line) for line in lines]
    idented = [
        (i, match.group("name"), match.group("rest"))
        for i, match in enumerate(matches)
        if match is not None
    ]
    indent = 0
    for i, directive_name, directive_rest in idented:
        if directive_name in ["elif", "else", "endif"]:
            indent -= 1
        lines[i] = "#" + (" " * indent) + directive_name + " " + directive_rest
        lines[i] = lines[i].strip()
        if directive_name in ["if", "ifdef", "ifndef", "elif", "else", "endif"]:
            indent += 1
        if directive_name == "endif":
            indent -= 1

    # if newline doesn't follows preprocessor part, insert one
    try:
        lastline_index = idented[-1][0]
        if lines[lastline_index + 1] != "":
            lines.insert(lastline_index + 1, "")
    except IndexError:
        pass

    return "\n".join(lines)
