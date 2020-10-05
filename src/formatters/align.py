# ############################################################################ #
#                                                                              #
#                                                         :::      ::::::::    #
#    align.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cacharle <me@cacharle.xyz>                 +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/10/04 09:56:31 by cacharle          #+#    #+#              #
#    Updated: 2020/10/05 10:10:51 by cacharle         ###   ########.fr        #
#                                                                              #
# ############################################################################ #


import re

import formatters.helper as helper


# def align_lines(prefixes, suffixes) -> [str]:
#     # individual alignments
#     alignments = [
#         len(prefix.replace("\t", " " * 4) // 4
#         for prefix in prefixes
#     ]
#     max_alignment = max(alignments, default=1)
#     # align according to greatest individual alignment
#     return [
#         prefix + "\t" * (max_alignment - alignment) + suffix)
#         for (prefix, suffix), alignment in zip(aligned, alignments)
#     ]

def align_scope(content: str, scope: str) -> str:
    """ Align content
        scope can be either local or global
          local:  for variable declarations in function
          global: for function prototypes
    """

    lines = content.split("\n")
    aligned = []
    # select regex according to scope
    if scope == "local":
        align_regex = (
            "^\t"
            r"(?P<prefix>{t})\s+"
            r"(?P<suffix>{d};)$"
        )
    elif scope == "global":
        align_regex = (
            r"^(?P<prefix>{t})\s+"
            r"(?P<suffix>({n}\(.*\);?)|({d}(;|(\s+=\s+.*))))$"
        )
    else:
        raise RuntimeError("scope should be 'global' or 'local'")
    align_regex = align_regex.format(
        t=helper.REGEX_TYPE,
        n=helper.REGEX_NAME,
        d=helper.REGEX_DECL_NAME
    )
    # get the lines to be aligned
    matches = [re.match(align_regex, line) for line in lines]
    aligned = [(i, match.group("prefix"), match.group("suffix"))
               for i, (line, match) in enumerate(zip(lines, matches))
               if match is not None]

    # if scope == "global":
    #     typedecl_regex       = (r"^(?P<prefix>\s*(typedef\s+)?(struct|enum|union))"
    #                             r"\s+(?P<suffix>[a-zA-Z]\w+)$")
    #     typedecl_close_regex = r"^(?P<prefix>})\s+(?P<suffix>[a-zA-Z]\w+;)$"
    #     in_type_scope = False
    #     for i, line in enumerate(lines):
    #         m = re.match(typedecl_regex, line)
    #         if m is not None:
    #             in_type_scope = True
    #             aligned.append((i, m.group("prefix"), m.group("suffix")))
    #             continue
    #         m = re.match(typedecl_close_regex, line)
    #         if m is not None:
    #             in_type_scope = False
    #             aligned.append((i, m.group("prefix"), m.group("suffix")))
    #             continue
    #         if in_type_scope:
    #             m = re.match(
    #                 r"^(?P<prefix>\s+{t})\s+"
    #                 r"(?P<suffix>{d};)$"
    #                 .format(t=helper.REGEX_TYPE, d=helper.REGEX_DECL_NAME),
    #                 line
    #             )
    #             if m is not None:
    #                 aligned.append((i, m.group("prefix"), m.group("suffix")))

    # get the minimum alignment required for each line
    min_alignment = max(
        [len(prefix.replace("\t", " " * 4)) // 4 + 1
         for _, prefix, _ in aligned],
        default=1
    )
    for i, prefix, suffix in aligned:
        alignment = len(prefix) // 4
        lines[i] = prefix + "\t" * (min_alignment - alignment) + suffix
        if scope == "local":
            lines[i] = "\t" + lines[i]
    return "\n".join(lines)


@helper.locally_scoped
def align_local(content: str) -> str:
    """ Wrapper for align_scope to use local_scope decorator """
    return align_scope(content, scope="local")


def align(content: str) -> str:
    """ Align the content in global and local scopes """
    content = align_scope(content, scope="global")
    content = align_local(content)
    return content
