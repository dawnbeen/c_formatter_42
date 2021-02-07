# ############################################################################ #
#                                                                              #
#                                                         :::      ::::::::    #
#    run.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cacharle <me@cacharle.xyz>                 +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/10/09 18:15:09 by cacharle          #+#    #+#              #
#    Updated: 2021/02/07 20:36:17 by charles          ###   ########.fr        #
#                                                                              #
# ############################################################################ #

from formatters.clang_format import clang_format
from formatters.hoist import hoist
from formatters.align import align
from formatters.preprocessor_directive import preprocessor_directive
from formatters.misc import (
    parenthesize_return,
    space_before_semi_colon,
    remove_multiline_condition_space
)


def run_all(content: str) -> str:
    """ Run all formatters """
    content = clang_format(content)
    content = preprocessor_directive(content)
    content = remove_multiline_condition_space(content)
    content = parenthesize_return(content)
    content = space_before_semi_colon(content)
    content = hoist(content)
    content = align(content)
    return content
