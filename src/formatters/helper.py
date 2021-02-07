# ############################################################################ #
#                                                                              #
#                                                         :::      ::::::::    #
#    helper.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cacharle <me@cacharle.xyz>                 +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/10/04 11:38:00 by cacharle          #+#    #+#              #
#    Updated: 2021/02/07 15:39:04 by charles          ###   ########.fr        #
#                                                                              #
# ############################################################################ #

import re


# regex for a type
REGEX_TYPE      = r"([a-z]+\s+)*[a-zA-Z]\w*"
# regex for a c variable/function name
REGEX_NAME      = r"\**[a-zA-Z]\w*"
# regex for a name in a declaration context (with array and function ptr)
REGEX_DECL_NAME = r"\(?{name}(\[\w+\])*(\)\(.*\))?".format(name=REGEX_NAME)


def locally_scoped(func):
    """ Apply the formatter on every local scopes of the content """

    def wrapper(content: str) -> str:
        return re.sub(
            # `*?` is the non greedy version of `*`
            # https://docs.python.org/3/howto/regex.html#greedy-versus-non-greedy
            r"\)\n\{\n(?P<body>.*?)\n\}\n".replace(r"\n", "\n"),
            lambda match: ")\n{\n" + func(match.group("body")) + "\n}\n",
            content,
            flags=re.DOTALL
        )
    return wrapper
