# ############################################################################ #
#                                                                              #
#                                                         :::      ::::::::    #
#    helper.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cacharle <me@cacharle.xyz>                 +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/10/04 11:38:00 by cacharle          #+#    #+#              #
#    Updated: 2020/10/04 11:58:34 by cacharle         ###   ########.fr        #
#                                                                              #
# ############################################################################ #

import re


def local_scope(func):
    def wrapper(content: str) -> str:
        return re.sub(
            r"\n\{\n(.*?)\n\}\n".replace(r"\n", "\n"),
            lambda match: func(match.group()),
            content,
            flags=re.DOTALL
        )
    return wrapper
