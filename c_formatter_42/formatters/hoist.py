# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    hoist.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: leo <leo@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/10/04 11:16:28 by cacharle          #+#    #+#              #
#    Updated: 2023/09/22 15:47:45 by leo              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import re

import c_formatter_42.formatters.helper as helper

DECLARATION_REGEX = re.compile(
    r"^\s*{t}\s+{d};$".format(t=helper.REGEX_TYPE, d=helper.REGEX_DECL_NAME)
)


@helper.locally_scoped
def hoist(content: str) -> str:
    r"""Hoist local variable and split assigned declaration

    Assignment splitting:
    {                   {
        int a = 1;  =>      int a;
                            a = 1;
    }                   }

    Variable hoisting:
    {                         {
        puts("bonjour");          int a;
        int a;            =>      char b;
        char b;                   puts("bonjour");
    }                         }

    Only one empty line after declarations
    {                         {
                                  int a;
        int a;                    char b;
        puts("bonjour");  ->
                                  puts("bonjour");
        char b;               }
    }
    """
    input_lines = content.split("\n")
    lines = []
    # Split assignment
    for line in input_lines:
        m = re.match(
            r"^(?P<indent>\s+)"
            r"(?P<type>{t})\s+"
            r"(?P<name>{d})\s+=\s+"
            r"(?P<value>.+);$".format(t=helper.REGEX_TYPE, d=helper.REGEX_DECL_NAME),
            line,
        )
        # If line is a declaration + assignment on the same line,
        # create 2 new lines, one for the declaration and one for the assignment
        # NOTE: edge case for array declarations which can't be hoisted (See #56)
        if (
            m is not None
            and re.match(r".*\[.*\].*", m.group("name")) is None
            and re.match(r"\s*(const|static)\s.*", line) is None
        ):
            lines.append(f"\t{m.group('type')}\t{m.group('name')};")
            lines.append(
                "{}{} = {};".format(
                    m.group("indent"),
                    m.group("name").replace("*", ""),  # replace '*' for pointers
                    m.group("value"),
                )
            )
        else:
            lines.append(line)

    # Split declarations from body and remove empty lines
    declarations = [line for line in lines if DECLARATION_REGEX.match(line) is not None]
    body = [line for line in lines if line not in declarations and line != ""]
    lines = declarations
    if len(declarations) != 0:
        lines.append("")
    print(declarations)
    print(body)
    lines.extend(body)
    return "\n".join(lines)
