# ############################################################################ #
#                                                                              #
#                                                         :::      ::::::::    #
#    align.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cacharle <me@cacharle.xyz>                 +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/10/04 09:56:31 by cacharle          #+#    #+#              #
#    Updated: 2021/02/11 20:13:11 by charles          ###   ########.fr        #
#                                                                              #
# ############################################################################ #

from __future__ import annotations

import re
import typing

if typing.TYPE_CHECKING:
    from typing import Literal

from c_formatter_42.formatters import helper

TYPEDECL_OPEN_REGEX = re.compile(
    r"""^(?P<prefix>\s*(typedef\s+)?   # Maybe a typedef
        (struct|enum|union))           # Followed by a struct, enum or union
        \s*(?P<suffix>[a-zA-Z_]\w+)?$  # Name of the type declaration
    """,
    re.X,
)
TYPEDECL_CLOSE_REGEX = re.compile(
    r"""^(?P<prefix>\})\s*             # Closing } followed by any amount of spaces
        (?P<suffix>([a-zA-Z_]\w+)?;)$  # Name of the type (if typedef used)
    """,
    re.X,
)


def align_scope(content: str, scope: Literal["local", "global"]) -> str:
    """Align content
    scope can be either local or global
      local:  for variable declarations in function
      global: for function prototypes
    """

    lines = content.split("\n")
    # select regex according to scope
    if scope == "local":
        align_regex = "^\t" r"(?P<prefix>{type})\s+" r"(?P<suffix>\**{decl};)$"
    elif scope == "global":
        align_regex = (
            r"^(?P<prefix>{type})\s+"
            r"(?P<suffix>({name}\(.*\)?;?)|({decl}(;|(\s+=\s+.*))))$"
        )
    align_regex = align_regex.format(
        type=helper.REGEX_TYPE, name=helper.REGEX_NAME, decl=helper.REGEX_DECL_NAME
    )
    lines_to_be_aligned = [re.match(align_regex, line) for line in lines]
    aligned = [
        (i, match.group("prefix"), match.group("suffix"))
        for i, match in enumerate(lines_to_be_aligned)
        if match is not None
        and match.group("prefix") not in ["struct", "union", "enum"]
    ]

    # Global type declaration (struct/union/enum)
    if scope == "global":
        in_type_scope = False
        for i, line in enumerate(lines):
            m = TYPEDECL_OPEN_REGEX.match(line)
            if m is not None:
                in_type_scope = True
                if m.group("suffix") is not None and "typedef" not in m.group("prefix"):
                    aligned.append((i, m.group("prefix"), m.group("suffix")))
                continue
            m = TYPEDECL_CLOSE_REGEX.match(line)
            if m is not None:
                in_type_scope = False
                if line != "};":
                    aligned.append((i, m.group("prefix"), m.group("suffix")))
                continue
            if in_type_scope:
                m = re.match(
                    r"^(?P<prefix>\s+{type})\s+"
                    r"(?P<suffix>\**{decl};)$".format(
                        type=helper.REGEX_TYPE, decl=helper.REGEX_DECL_NAME
                    ),
                    line,
                )
                if m is not None:
                    aligned.append((i, m.group("prefix"), m.group("suffix")))

    # Minimum alignment required for each line
    min_alignment = max(
        (len(prefix.expandtabs(4)) // 4 + 1 for _, prefix, _ in aligned),
        default=1,
    )
    for i, prefix, suffix in aligned:
        alignment = len(prefix.expandtabs(4)) // 4
        lines[i] = prefix + "\t" * (min_alignment - alignment) + suffix
        if scope == "local":
            lines[i] = (
                "\t" + lines[i]
            )  # Adding one more indent for inside the type declaration
    return "\n".join(lines)


@helper.locally_scoped
def align_local(content: str) -> str:
    """Wrapper for align_scope to use local_scope decorator"""
    return align_scope(content, scope="local")


def align(content: str) -> str:
    """Align the content in global and local scopes"""
    content = align_scope(content, scope="global")
    content = align_local(content)
    return content
