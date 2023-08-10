# ############################################################################ #
#                                                                              #
#                                                         :::      ::::::::    #
#    hoist.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cacharle <me@cacharle.xyz>                 +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/10/04 11:16:28 by cacharle          #+#    #+#              #
#    Updated: 2021/02/11 20:13:29 by charles          ###   ########.fr        #
#                                                                              #
# ############################################################################ #

import re

import c_formatter_42.formatters.helper as helper


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

    def match_declaration_assignment(s):
        return re.match(
            r"^(?P<indent>\s+)"
            r"(?P<type>{t})\s+"
            r"(?P<name>{d})\s+=\s+"
            r"(?P<value>.+);$".format(t=helper.REGEX_TYPE, d=helper.REGEX_DECL_NAME),
            s,
        )

    def is_declaration_assignment_array(s):
        m = match_declaration_assignment(s)
        if m is None:
            return False
        return re.match(r".*\[.*\].*", m.group("name")) is not None

    lines = []
    # split assignment
    for line in input_lines:
        m = match_declaration_assignment(line)
        if m is not None and not is_declaration_assignment_array(line):
            lines.append(f"\t{m.group('type')}\t{m.group('name')};")
            lines.append(
                "{}{} = {};".format(
                    m.group("indent"),
                    m.group("name").replace("*", ""),
                    m.group("value"),
                )
            )
        else:
            lines.append(line)

    # hoist declarations and filter empty lines
    decl_regex = r"^\s*{t}\s+{d};$".format(
        t=helper.REGEX_TYPE, d=helper.REGEX_DECL_NAME
    )
    declarations = [
        line
        for line in lines
        if re.match(decl_regex, line) is not None
        or is_declaration_assignment_array(line)
    ]
    body = [line for line in lines if line not in declarations and line != ""]
    lines = declarations
    if len(declarations) != 0:
        lines.append("")
    lines.extend(body)

    return "\n".join(lines)
