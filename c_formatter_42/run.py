# ############################################################################ #
#                                                                              #
#                                                         :::      ::::::::    #
#    run.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cacharle <me@cacharle.xyz>                 +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/10/09 18:15:09 by cacharle          #+#    #+#              #
#    Updated: 2021/02/11 20:12:15 by charles          ###   ########.fr        #
#                                                                              #
# ############################################################################ #

from c_formatter_42.formatters.align import align
from c_formatter_42.formatters.clang_format import clang_format
from c_formatter_42.formatters.hoist import hoist
from c_formatter_42.formatters.line_breaker import line_breaker
from c_formatter_42.formatters.misc import (
    insert_void,
    parenthesize_return,
    remove_multiline_condition_space,
    space_before_semi_colon,
)
from c_formatter_42.formatters.preprocessor_directive import preprocessor_directive
from c_formatter_42.formatters.return_type_single_tab import return_type_single_tab


def run_all(content: str) -> str:
    """Run all formatters"""
    content = clang_format(content)
    content = preprocessor_directive(content)
    content = remove_multiline_condition_space(content)
    content = parenthesize_return(content)
    content = space_before_semi_colon(content)
    content = hoist(content)
    content = align(content)
    content = return_type_single_tab(content)
    content = insert_void(content)
    content = line_breaker(content)
    return content
