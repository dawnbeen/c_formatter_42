# ############################################################################ #
#                                                                              #
#                                                         :::      ::::::::    #
#    helper.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cacharle <me@cacharle.xyz>                 +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/10/04 11:38:00 by cacharle          #+#    #+#              #
#    Updated: 2021/02/08 18:22:06 by charles          ###   ########.fr        #
#                                                                              #
# ############################################################################ #

import re


# regex for a type
REGEX_TYPE      = r"(?!return)([a-z]+\s+)*[a-zA-Z_]\w*"
# regex for a c variable/function name
REGEX_NAME      = r"\**[a-zA-Z_*()]\w*"
# regex for a name in a declaration context (with array and function ptr)
REGEX_DECL_NAME = r"\(?{name}(\[.*\])*(\)\(.*\))?".format(name=REGEX_NAME)


def locally_scoped(func):
    """ Apply the formatter on every local scopes of the content """

    def wrapper(content: str) -> str:
        def get_replacement(match):
            body = match.group("body").strip("\n")
            result = func(body)
            if result.strip() == "":
                return ")\n{\n}\n"
            return ")\n{\n" + result + "\n}\n"

        return re.sub(
            # `*?` is the non greedy version of `*`
            # https://docs.python.org/3/howto/regex.html#greedy-versus-non-greedy
            r"\)\n\{(?P<body>.*?)\n\}\n".replace(r"\n", "\n"),
            get_replacement,
            content,
            flags=re.DOTALL
        )
    return wrapper
